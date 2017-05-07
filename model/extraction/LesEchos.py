import urllib, lxml.html
 
 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//div/article[@class="article-small article-medium"]//figure/a/@href')
 
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//div/article[@class="article-small article-medium"]//div[@class="titre"]/a/text()')
 
        return zip(article_titles, articles_href)
