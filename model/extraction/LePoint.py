import urllib, lxml.html
 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//article[@class="en-continu-li"]//a/@href') + doc.xpath('//div[@class="row keep-cols"]/figure/a/@href')
 
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//h2[@class="art-lead"]/text()') + doc.xpath('//div[@class="col plm"]//a/h2[@class="art-title"]/text()')
 
        return zip(article_titles, articles_href)
