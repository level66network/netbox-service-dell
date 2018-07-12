# netbox-service-dell
## Dell Support Service APIs
You need to request access to the Dell Warranty Status API to be able to make API calls. More information can be found [here](https://techdirect.dell.com/portal.30/Login.aspx).
## NetBox
### Preparation
#### Custom fields
You need to create the following custom fields and attatch them to the object type dcim > device. This formular can be found under Username > Admin > Extras > Custom fields.
* service_until / Date
* service_type / Text
#### API access
You need to create a User Token with read and write access. This option can be found under Username > Profile > API Tokens > Add a token.
### Export templates
#### Maintenance Report
* Content type: dcim > device
* Name: Maintenance Report
* Mime type: xhtml+xml
* File extension: html

Template code:
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
		<meta name="viewport" content="width=device-width, initial-scale=1">
	</head>
	<body>
		<h1>Device - Maintenance Report</h1>
		<table class="pure-table" style="width:100%;">
			<thead>
				<th>Hostname</th>
				<th>Serial</th>
				<th>Service Type</th>
				<th>Service duration</th>
				<th>Location</th>
			</thead>
			<tbody>
			{% for device in queryset %}
			<tr>
				<td>{{ device.name }}</td>
				<td>{{ device.serial }}</td>
				<td>{% if device.cf.service_type %}{{ device.cf.service_type }}{% else %}<font color="red">{{ device.cf.service_type }}</font>{% endif %}</td>
				<td>{{ device.cf.service_until }}</td>
				<td>{{ device.site.name }} > {{ device.rack.name }}{% if device.position %} > U{{ device.position }}{% endif %}</td>
			</tr>
			{% endfor %}
			</tbody>
		</table>
	</body>
</html>
```

## Python 2.7
Install requirements via:
```bash
pip2 install -r requirements.txt
```
