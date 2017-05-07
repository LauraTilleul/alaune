#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, lxml.html

def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    articles_href = doc.xpath('//article[@data-vr-contentbox]/a/@href')
    
    doc=lxml.html.document_fromstring(data)
    articles_titles = doc.xpath('//article[@data-vr-contentbox]//h2[@class="title "]/text()')
    
    return zip(articles_titles, articles_href)
