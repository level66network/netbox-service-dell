# -*- coding: utf-8 -*-

def extendURL(url, extend):
	"""Extend a URL by the given extend."""
	url = url.strip().strip('/') + '/' + extend.strip().strip('/')
	return url

def dellServiceCode(code):
	"""Maps the codes to short descriptions."""
	if code == 'PO':
		return 'Parts only'
	elif code == 'KH':
		return 'Keep Your Hard drive Service'
	elif code == 'UD':
		return 'VMware Workload'
	elif code == 'RB':
		return 'Carry-in'
	elif code == 'NU' or code == 'NI':
		return 'ProSupport NBD'
	elif code == 'PG':
		return 'ProSupport Plus NBD'
	elif code == 'SW':
		return 'Software Maintainance'
	elif code == 'ND':
		return 'Onsite Service NBD'
	elif code == '8I' or code == '8U':
                return 'ProSupport 8H'
	elif code == '4I' or code == '4U':
		return 'ProSupport 4H'
	elif code == 'PQ':
		return 'ProSupport Plus 4H'
	elif code == '78':
		return '8 Hour 7x24 Compellent Support'
	elif code == '74':
		return '4 Hour 7x24 Compellent Support'
	else:
		return ''

def dellCompareServiceCode(code1, code2):
	"""Returns the better code."""
	weights = {
		False: 0,
		'UD': 0,
		'KH': 0,
		'PO': 10,
		'RB': 15,
		'NU': 45,
		'NI': 20,
		'SW': 30,
		'ND': 30,
		'PG': 40,
		'NU': 45,
		'78': 45,
		'8I': 45,
		'8U': 45,
		'74': 50,
		'4I': 50,
		'4U': 50,
		'PQ': 60
	}
	"""Prevent error if service does not exsits."""
	try:
		if weights[code1] >= weights[code2]:
			return code1
		else:
			return code2
	except IndexError:
		return code1
