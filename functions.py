# -*- coding: utf-8 -*-

def extendURL(url, extend):
	"""Extend a URL by the given extend."""
	url = url.strip().strip('/') + '/' + extend.strip().strip('/')
	return url

def dellServiceCode(code):
	"""Maps the codes to short descriptions."""
	if code == 'PO':
		return 'Parts only'
	elif code == 'NU':
		return 'ProSupport NBD'
	elif code == 'PG':
		return 'ProSupport Plus NBD'
	elif code == 'ND':
		return 'Onsite Service NBD'

def dellCompareServiceCode(code1, code2):
	"""Returns the better code."""
	weights = {
		False: 0,
		'PO': 10,
		'NU': 20,
		'PG': 30,
		'ND': 40,
	}
	if weights[code1] >= weights[code2]:
		return code1
	else:
		return code2
