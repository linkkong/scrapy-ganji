# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class qichacha_detail(scrapy.Item):
    name = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    faren = scrapy.Field()
    zhuceziben = scrapy.Field()
    zhuceshijian = scrapy.Field()
    status = scrapy.Field()
    gszch = scrapy.Field()
    zuzhicode = scrapy.Field()
    xinyongcode = scrapy.Field()
    category = scrapy.Field()
    hangye = scrapy.Field()
    yingye = scrapy.Field()
    hezhun = scrapy.Field()
    dengji = scrapy.Field()
    regaddress = scrapy.Field()
    jingying = scrapy.Field()
    success = scrapy.Field()
    ID = scrapy.Field()

class ganji_cate(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    parent = scrapy.Field()
    level = scrapy.Field()

class qianzhan_detail(scrapy.Item):
    companyname = scrapy.Field()
    tel = scrapy.Field()
    address = scrapy.Field()
    fuwutese = scrapy.Field()
    tigongfuwu = scrapy.Field()
    fuwufanwei = scrapy.Field()
    lianxiren = scrapy.Field()
    shangjiadizhi = scrapy.Field()
    yingyeshijian = scrapy.Field()
    website = scrapy.Field()
    jianjie = scrapy.Field()
    ID = scrapy.Field()
    cate = scrapy.Field()
    table = scrapy.Field()
class qianzhan_list(scrapy.Item):
    url = scrapy.Field()
    city = scrapy.Field()
class xc_linedetail(scrapy.Item):
    ID = scrapy.Field()
    title = scrapy.Field()
    fenlei = scrapy.Field()
    bianhao = scrapy.Field()
    chufadi = scrapy.Field()
    qijia = scrapy.Field()
    chanpintese = scrapy.Field()
    fuwubaozhang = scrapy.Field()
    lingshoushang = scrapy.Field()
    xingchenggaiyao = scrapy.Field()
    tuijian = scrapy.Field()
    chanpintese2 = scrapy.Field()
    chanpingaiyao = scrapy.Field()
    xingcheng = scrapy.Field()    
    zilifeiyong = scrapy.Field()
    feiyongbaohan = scrapy.Field()
    yudingxuzhi = scrapy.Field()
    chanpinshuoming = scrapy.Field()
    weiyuetiaokuan = scrapy.Field()
    chuxingxuzhi = scrapy.Field()
    anquanzhinan = scrapy.Field()
    yudingxianzhi = scrapy.Field()
    yudingshuoming = scrapy.Field()
    duotu = scrapy.Field()
    zhusu = scrapy.Field()
    tianshu = scrapy.Field()
