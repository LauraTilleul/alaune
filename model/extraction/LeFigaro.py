# -*- coding:utf-8 -*-
 
import urllib, lxml.html
 
 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//h1[@class="fig-profil-headline"]/a/@href') + doc.xpath('//section[contains(@class, "fig-profil ")]/div/h2/a/@href')
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//h1[@class="fig-profil-headline"]/a/text()') + doc.xpath('//section[contains(@class, "fig-profil ")]/div/h2/a/text()')
	
        return zip(article_titles, articles_href)
