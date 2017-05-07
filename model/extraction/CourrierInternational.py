# -*- coding:utf-8 -*-

import urllib, lxml.html

def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()

	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//main/div/a/@href')

	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//main/div/a/article//h1/text()')

        return zip(article_titles, articles_href)
