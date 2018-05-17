import requests
import json
from datetime import datetime

import configuration
import functions

netboxHeaders = {'content-type': 'application/json', 'Authorization': 'Token ' + configuration.NETBOX['API_TOKEN']}
dellHeaders = {'content-type': 'application/json'}
devicesURL = functions.extendURL(configuration.NETBOX['API_URL'], '/dcim/devices/')

"""Fetch Netbox devices and check http status code."""
r = requests.get(devicesURL, headers=netboxHeaders, verify=configuration.NETBOX['API_SSL_VERIFY'])
if r.status_code == 200:
	requestReturnJSON = json.loads(r.text)
	if requestReturnJSON['count'] > 0:
		"""Iterate through all devices."""
		for device in requestReturnJSON['results']:
				"""Check if manufacturer is in the list of manufacturers to check."""
				if device['device_type']['manufacturer']['slug'] in configuration.NETBOX['MANUFACTURER_SLUGS']:
					"""Check if serial has 7 characters."""
					if len(device['serial']) == 7:
						print "Checking device with serial " + device['serial'] + " against Dell API."
						r = requests.get(functions.extendURL(configuration.DELL['API_URL'], '/support/assetinfo/v4/getassetwarranty/' + device['serial'] + '?apikey=' + configuration.DELL['API_KEY']), headers=dellHeaders)
						"""Check http status code."""
						if r.status_code == 200:
							dellJSON = json.loads(r.text)
							serviceCode = ''
							serviceDate = ''
							for service in dellJSON['AssetWarrantyResponse'][0]['AssetEntitlementData']:
								service['EndDate'] = datetime.strptime(service['EndDate'], '%Y-%m-%dT%X')
								if service['EndDate'] > datetime.now():
									serviceCode = functions.dellCompareServiceCode(serviceCode, service['ServiceLevelCode'])
									serviceDate = service['EndDate']
							"""Prepare data to update the device in Netbox."""
							serviceDate = serviceDate.strftime('%Y-%m-%d')
							serviceName = functions.dellServiceCode(serviceCode)
							patchData = '{"custom_fields": {"service_until": "' + serviceDate + '", "service_type": "' + serviceName + '"}}'
							r = requests.patch(functions.extendURL(configuration.NETBOX['API_URL'], '/dcim/devices/' + str(device['id']))+'/', data=patchData, headers=netboxHeaders, verify=configuration.NETBOX['API_SSL_VERIFY'])
							if r.status_code != 200:
								print 'Error updating values in Netbox.'
						else:
							print 'Error with the Dell API.'
else:
	exit('Netbox request not working! HTTP status code: ' + r.status_code)
