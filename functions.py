# -*- coding: utf-8 -*-

def extendURL(url, extend):
	url = url.strip().strip('/') + '/' + extend.strip().strip('/')
	return url
