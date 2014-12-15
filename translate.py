#!/usr/bin/env python

import urllib, sys, os, json, io

if len(sys.argv) < 2:
	print('usage: %s word' % os.path.basename(sys.argv[0]))
	exit()

filename = os.path.join(os.path.expanduser('~'), '.fyrc')
conf = open(filename, 'rwb+')

try:
	opts =  sys.argv[1]
	if opts == '--install':
		key = raw_input('input baidu api key:')
		conf.writelines(key)
		os.popen('cp %s /usr/bin/fy' % sys.argv[0])	
	else:
		cid = conf.readline().strip()
		word = ' '.join(sys.argv[1:])
		url = "http://openapi.baidu.com/public/2.0/bmt/translate" + \
		"?client_id=%s&q='%s'&from=auto&to=auto" % (cid, word);
		resp = urllib.urlopen(url).read()
		json_obj = json.loads(resp)
		results = json_obj['trans_result']
		for elt in results:
			print('src : %s' % elt['src'])
			print('dst : %s' % elt['dst'])
finally:
	conf.close()
