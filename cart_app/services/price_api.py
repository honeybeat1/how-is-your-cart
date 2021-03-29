import requests
import urllib.request
import pandas as pd
import jinja2
import json
from datetime import datetime

api_template = jinja2.Template("{{ date.strftime('%Y-%m-%d') }}")


def get_products(date):
	""" 날짜(date)가 주어지면 해당 날짜의 모든 품목 가격 데이터가 담긴
		DataFrame을 리턴합니다. 데이터가 없을 경우 None으로 리턴합니다. """
	# 품목 카테고리 리스트
	categories = ['100', '200', '300', '400', '500', '600']
	result = pd.DataFrame()

	for category in categories:
		format_date = api_template.render(date=date)
		url = "http://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList" +\
		"&p_cert_key=bceaf385-9d34-4a75-9c6f-0607eb325485&p_cert_id=pje1740&p_returntype=json" +\
		"&p_product_cls_code=01" +\
		"&p_regday=" + format_date +\
		"&p_item_category_code=" + category
		response = urllib.request.urlopen(url) 
		json_str = response.read().decode("utf-8")
		obj = json.loads(json_str)
		try:
			df = pd.DataFrame(obj['data']['item'])
		# 가격 데이터가 없는 주말, 공휴일일 경우
		except TypeError:
			return
		df = df.drop(['kind_code', 'rank_code', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'], axis=1)
		
		# 가격 데이터만 int로 바꿔주기
		dprlist = ['dpr1', 'dpr2','dpr3', 'dpr4', 'dpr5', 'dpr6', 'dpr7']
		for i in dprlist:
			df[i] = df[i].str.replace(',','').replace('-',0).astype(int)
		result = result.append(df)
		
	return result
