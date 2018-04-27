# -*- coding: utf-8 -*-

def buildURL(url, component):
	url = url.strip().strip('/')
	return url + '/' + component + '/?format=json'
