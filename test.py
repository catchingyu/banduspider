# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import urllib2
import sys
import json
import glob
import re

fund_info_list = ['Date', 'NetValue', 'AccuValue', 'DayIncrease', 'Bonus']


def getEveryDay(begin_date, end_date):
	date_list = []
	begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
	while begin_date <= end_date:
		date_str = begin_date.strftime("%Y-%m-%d")
		date_list.append(date_str)
		begin_date += datetime.timedelta(days=1)
	return date_list

def test2():
	# 获取两个日期间的所有日期
	print(getEveryDay('2017-01-01', '2017-01-11'))
def test1():
	bonusDay = "每份派现金0.0097元"
	# process the bonustofloat
	bonusDay=bonusDay[bonusDay.find('现金') + 6:bonusDay.rfind('元')]
	print bonusDay
	bonusDay=float(bonusDay)
	print bonusDay*50
def gen_fund_insert_command(tablename, info_dict):
	"""
	fund insert command
	"""
	info_list = fund_info_list
	t = []
	for il in info_list:
		if il in info_dict:
			t.append(info_dict[il])
		else:
			t.append('')
	t = tuple(t)
	command = (r"insert into " +  tablename + " values(?,?,?,?,?)", t)
	print command
	return command

def test3():
	pagehtml = '<a href="http://www.bandubb.com/wp-content/themes/begin/inc/go.php?url=http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490232&amp;idx=6&amp;sn=7f64064a05329d6d1dd600f20426e444&amp;chksm=900ee8c5a77961d38f5da85543fc4913c49471e047013bffd00184bccf7ae43e61c70c4a31b0&amp;scene=21#wechat_redirect"  target="_blank" rel="noopener noreferrer">【单读】许知远：春之祭+日瓦戈医生</a>'
	tr_re = re.compile(r'<p>(.*?)</p>')
	item_re = re.compile(
		r'<a href="(.*?)">(.*?)</a>',
		re.X)
	for line in tr_re.findall(pagehtml):
		print line + '\n'
		match = item_re.match(line)
		if match:
			entry = match.groups()
			print entry

def test4():
	line = '<a href="http://www.bandubb.com/wp-content/themes/begin/inc/go.php?url=http://mp.weixin.qq.com/s?__biz=MzA5MDE3MTE1NA==&amp;mid=2247490232&amp;idx=6&amp;sn=7f64064a05329d6d1dd600f20426e444&amp;chksm=900ee8c5a77961d38f5da85543fc4913c49471e047013bffd00184bccf7ae43e61c70c4a31b0&amp;scene=21#wechat_redirect"  target="_blank" rel="noopener noreferrer">【单读】许知远：春之祭+日瓦戈医生</a>'
	item_re = re.compile(
		r'<a href="(.*?);(.*?)">(.*?)</a>',
		re.I)
	match = item_re.match(line)
	if match:
		entry = match.groups()
		print entry[0], entry[2]

if __name__=="__main__":
	print "start..."
#	test4()
#	info_dict = {}
#	info_dict.update({fund_info_list[0]: 1})
#	info_dict.update({fund_info_list[1]: 2})
#	info_dict.update({fund_info_list[2]: 3})
#	info_dict.update({fund_info_list[3]: 4})
#	info_dict.update({fund_info_list[4]: 5})
	#gen_fund_insert_command("10000", info_dict)
#	test2()
	sys.exit(0)