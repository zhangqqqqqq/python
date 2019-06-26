# -*- coding:utf-8 -*-
from urllib import request
def fetch_data(url):
	with request.urlopen(url) as f:
		data=f.read()
	return json.loads(data)
