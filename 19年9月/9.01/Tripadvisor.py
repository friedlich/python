#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-09-01 14:46:10
# Project: TripAdvisor

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {
    }

    client = pymongo.MongoClient('localhost')
    db = client['trip']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.tripadvisor.cn/Attractions-g186338-Activities-London_England.html#FILTERED_LIST',
                   callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.listing_title > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

        next = response.doc('.unified.pagination .nav.next').attr.href
        self.crawl(next, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        name = response.doc('.h1').text()
        ranking = response.doc('.popIndexValidation.header_popularity ').text()
        rating = response.doc('a > .reviewCount').text()
        address = response.doc('.contactInfo > .address > span > span:nth-child(2)').text()
        phone = response.doc('.contactInfo > .contact > .is-hidden-mobile > div').text()
        duration = response.doc('.centerWell > div > div > div > div > div:nth-child(4) > div').text()
        introduction = response.doc('.centerWell > div > div > div > div > div:nth-child(2) > span').text()
        return {
            "url": url,
            "name": name,
            "ranking": ranking,
            "rating": rating,
            "address": address,
            "phone": phone,
            "duration": duration,
            "introduction": introduction
        }

    def on_result(self, result):
        if result:
            self.save_to_mongo(result)

    def save_to_mongo(self, result):
        if self.db['london'].insert(result):
            print('saved to mongo', result)
