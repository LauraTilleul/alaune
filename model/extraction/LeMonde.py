#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, lxml.html

def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    articles_href = doc.xpath('//article[contains(@class, "titre_une")]/a/@href')
    
    doc=lxml.html.document_fromstring(data)
    articles_titles = doc.xpath('//h1[contains(@class, "tt3 ")]/text()')

    return zip(articles_titles, articles_href)
