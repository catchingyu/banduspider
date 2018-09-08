# !/usr/bin/python 
# -*- coding: utf-8 -*-
# -*- coding: gdb -*-

import time
import datetime
import glob
import urllib2
import urllib
import json
import sys
import re
import sqlite3
import random
import threading
import os


def download_audiofile_fromURL(mediaURL):
	print mediaURL
	urllib.urlretrieve(mediaURL, "./" + 'xuzhiyuan' + '.mp3')
	return

#https://res.wx.qq.com/voice/getvoice?mediaid=MzA5MDE3MTE1NF8yMjQ3NDg0NzEy
def get_audiofile(itemURL):
	pre_url = 'https://res.wx.qq.com/voice/getvoice?mediaid='
	try:
		print 'Downloading itemURL'+ itemURL + '\n'
#		response = urllib2.urlopen(itemURL)
		response = urllib2.urlopen(itemURL)
	except urllib2.HTTPError, e:
		print e
		return ''
	except StandardError, e:
		print e
		return ''
	json_page_value = response.read().decode('utf-8')
	#print json_page_value
	#<span id="voice_play_MzA5MDE3MTE1NF8yMjQ3NDkwMjMw_0" aria-labelledby="播放开关" class="db share_audio_switch"><em class="icon_share_audio_switch" role="button"></em></span>
	#https://res.wx.qq.com/voice/getvoice?mediaid=MzA5MDE3MTE1NF8yMjQ3NDkwMjMw
	tr_re = re.compile(r'<p>(.*?)</p>')
	item_re = re.compile(
		r'voice_encode_fileid="(.*?)">')
	for line in tr_re.findall(json_page_value):
		#print line + '\n'
		match = item_re.search(line)
		#print match
		if match:
			entry = match.groups()
			print entry[0]
			download_audiofile_fromURL(pre_url + entry[0])
	return

#get pageinfo and return the name and URL
#http://www.bandubb.com/wp-content/themes/begin/inc/go.php?url=http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490366&amp;idx=6&amp;sn=1f7c685c0d943b92a28239cecb375c4a&amp;chksm=900ee943a7796055c8e3900da847c03edf90fe6c17e82f096aa7f16fbed4e901092b788f9c20&amp;scene=21#wechat_redirect
#  【单读】许知远：开罗之声
#http://www.bandubb.com/wp-content/themes/begin/inc/go.php?url=http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490232&amp;idx=6&amp;sn=7f64064a05329d6d1dd600f20426e444&amp;chksm=900ee8c5a77961d38f5da85543fc4913c49471e047013bffd00184bccf7ae43e61c70c4a31b0&amp;scene=21#wechat_redirect
def process_pageinfo(pagehtml):
	tr_re = re.compile(r'<p>(.*?)</p>')
	item_re = re.compile(
		r'<a href="(.*?)"  target(.*?)>(.*?)</a>',
		re.I)
	for line in tr_re.findall(pagehtml):
		#print line + '\n'
		match = item_re.match(line)
		if match:
			entry = match.groups()
			print entry[0], entry[2]

def get_audiolistURL(albumURL):
	try:
		print 'Downloading albumURL'+ albumURL + '\n'
		response = urllib2.urlopen(albumURL)
	except urllib2.HTTPError, e:
		print e
		return ''
	except StandardError, e:
		print e
		return ''
	json_page_value = response.read().decode('utf-8')
	#print json_page_value
	return json_page_value



def main(argv):
#	html = get_audiolistURL("http://www.bandubb.com/dandu/27732.html")
#	itemURL = 'http://www.bandubb.com/wp-content/themes/begin/inc/go.php?url=http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490232&amp;idx=6&amp;sn=7f64064a05329d6d1dd600f20426e444&amp;chksm=900ee8c5a77961d38f5da85543fc4913c49471e047013bffd00184bccf7ae43e61c70c4a31b0&amp;scene=21#wechat_redirect'
	itemURL = 'http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490232&amp;idx=6&amp;sn=7f64064a05329d6d1dd600f20426e444&amp;chksm=900ee8c5a77961d38f5da85543fc4913c49471e047013bffd00184bccf7ae43e61c70c4a31b0&amp;scene=21'
#	process_pageinfo(html)
	get_audiofile(itemURL)
	sys.exit(0)

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf-8')
	main(sys.argv)




