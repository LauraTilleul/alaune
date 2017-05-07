import urllib, lxml.html


def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    titres= doc.xpath("//div[@class='main-article']//article/h2/a/text()")
    titres+= doc.xpath('//div[@class="title-wrapper"]//a/text()')
    titres+= doc.xpath('//div[@class="title-river"]//a/text()')
    
    liens = doc.xpath('//div[@class="main-article"]/article/h2/a/@href')
    liens+= doc.xpath('//div[@class="title-wrapper"]//a/@href')
    liens+= doc.xpath('//div[@class="title-river"]//a/@href')
   
    return zip(titres, liens)
