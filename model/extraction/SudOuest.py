# -*- coding:utf-8 -*-
 
import urllib, lxml.html
 
# targetURL = 'http://www.sudouest.fr/'
# passe en parametre depuis le script de la requete
 
def unes(targetURL):
	file = urllib.urlopen("http://www.sudouest.fr/")
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//section[@class="articles essentiel "]//div[@class="article-wrapper"]/a/@href') + doc.xpath('//section[@class="articles default "]//div[@class="article-wrapper"]/a/@href')

 
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//section[@class="articles essentiel "]//div[@class="article-wrapper"]/a/h2/text()') + doc.xpath('//section[@class="articles default "]//div[@class="article-wrapper"]/a/h2/text()')
 
        return zip(article_titles, articles_href)
