# -*- coding: utf-8 -*-
import scrapy, pymysql
from pprint import pprint
from ..items import NewItem

db_name = 'boatlistradmins_newdb2020boats'
user = 'root'
passwd='root'
host='localhost'
port=3306
import argparse
import base64
import csv
import datetime
import glob
import hashlib
import http.client
import json
import mimetypes
import os
import random
import re
import string
import sys
import time
import urllib.request
import warnings
import webbrowser
from threading import Thread
from urllib import request

import pymysql
import requests
import unicodecsv as csvv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def ins_delete_update(query):
    try:
        db = pymysql.connect(db=db_name, user=user,
                             passwd=passwd, host=host, port=port)
        db.autocommit = True
        cur = db.cursor()
        query = str(query).replace("\xa0", "").replace(
            "N'", "'").replace("\\'", "'")
        cur.execute(query)
        aa = ""
    except Exception as ex1:
        print(str(ex1))


def SelectionQuery(query):
    try:
        cnxn = pymysql.connect(
            db=db_name, user=user, passwd=passwd, host=host, port=port)
        cursor = cnxn.cursor()
        cursor.execute(query)
        allresult = cursor.fetchall()
        return allresult
    except:
        print('fail')
    return ''


def InserUserGetID(seller, phone, address):
    user_id = ''
    try:
        user_login = ''
        seller = seller.replace('\\n', '')
        user_login = str(seller).replace(' ', '').lower()
        m = hashlib.md5()
        m.update(user_login.encode('utf-8'))
        user_pass = ''
        user_pass = m.hexdigest()
        user_nicename = ''
        user_nicename = str(seller).replace(' ', '')
        user_email = ''
        user_email = user_login+"@boatlistr.com"
        user_url = ''
        user_registered = datetime.datetime.now()
        user_activation_ke = user_pass
        user_status = 0
        display_name = ''
        display_name = seller

        checkuser = SelectionQuery(
            "SELECT ID FROM `wp_users` where user_login='"+str(user_login).replace("'", "''")+"'")
        if(len(checkuser) == 0):
            ins_delete_update("INSERT INTO `wp_users` (`user_login` ,`user_pass` ,`user_nicename` ,`user_email` ,`user_url` ,`user_registered` ,`user_activation_key` ,`user_status` ,`display_name`) VALUES (N'"+str(user_login).replace("'", "''")+"' ,N'"+str(user_pass).replace("'", "''")+"' ,N'"+str(user_nicename).replace(
                "'", "''")+"' ,N'"+str(user_email).replace("'", "''")+"' ,N'"+str(user_url).replace("'", "''")+"' ,N'"+str(user_registered).replace("'", "''")+"' ,N'"+str(user_activation_ke).replace("'", "''")+"' ,N'"+str(user_status).replace("'", "''")+"' ,N'"+str(display_name).replace("'", "''")+"')")

            getUserID = SelectionQuery("select ID from `wp_users` where user_login=N'"+str(
                user_login).replace("'", "''")+"' and `user_pass`=N'"+str(user_pass).replace("'", "''")+"'")

            user_id = str(getUserID[0][0])
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'nickname' ,N'"+str(user_login).replace("'", "''")+"')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'first_name' ,N'"+str(seller).replace("'", "''")+"')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'last_name' ,'')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'description' ,'')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'rich_editing' ,'true')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'syntaz_heighlighting' ,'true')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'comment_shortcuts' ,'false')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'admin_color' ,'fresh')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'use_ssl' ,'0')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'show_admin_bar_front' ,'true')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'locale' ,'')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'wp_capabilities' ,'a:1:{s:6:\"author\";b:1;}')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'wp_user_level' ,'2')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'user_address' ,N'"+str(address).replace("'", "''")+"')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'_user_address' ,'field_5e663d5d17041')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'user_phone_no' ,N'"+str(phone).replace("'", "''")+"')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(
                user_id).replace("'", "''")+"' ,'_user_phone_nouser_phone_no' ,'field_5e663d9b17041')")
            ins_delete_update("INSERT INTO `wp_usermeta` (`user_id` ,`meta_key` ,`meta_value`) VALUES (N'" +
                              str(user_id).replace("'", "''")+"' ,'dismissed wp pointers' ,'')")
        else:
            user_id = str(checkuser[0][0])
    except Exception as d:
        print(str(d))

    return user_id


def downloadImage(link, path):
    try:
        with open(path, 'wb') as handle:
            response = requests.get(link, stream=True)
            if not response.ok:
                print(str(response))
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
    except:
        print('Error in Image Downloading....')

def InsertTerms(name, slug, taxonomy, post_id):
    term_id = ''
    checkterms = SelectionQuery("SELECT term_id FROM `wp_terms` where name='"+str(
        name).replace("'", "''")+"' AND slug='"+str(slug).replace("'", "''")+"'")
    print(checkterms)
    if(len(checkterms) == 0):
        ins_delete_update("INSERT INTO `wp_terms` (`name` ,`slug` ,`term_group`) VALUES (N'" +
                          str(name).replace("'", "''")+"' ,N'"+str(slug).replace("'", "''")+"' ,'0')")
        getMaxID = SelectionQuery("SELECT max(term_id) FROM wp_terms")
        print(getMaxID)
        term_id = str(getMaxID[0][0])
    else:
        term_id = str(checkterms[0][0])
    term_taxonomy_id = ''
    checktax = SelectionQuery(
        "select term_taxonomy_id  from wp_term_taxonomy where term_id='"+term_id+"'")
    if(len(checktax) == 0):
        ins_delete_update("INSERT INTO `wp_term_taxonomy` (`term_id` ,`taxonomy` ,`description` ,`parent` ,`count`) VALUES (N'" +
                          str(term_id).replace("'", "''")+"' ,N'"+str(taxonomy).replace("'", "''")+"' ,'' ,'0' ,'0')")
        getMaxIDterm = SelectionQuery(
            "SELECT max(term_taxonomy_id) FROM wp_term_taxonomy")
        term_taxonomy_id = str(getMaxIDterm[0][0])
    else:
        term_taxonomy_id = str(checktax[0][0])
    ins_delete_update("INSERT INTO `wp_term_relationships` (`object_id` ,`term_taxonomy_id` ,`term_order`) VALUES ('" +
                      str(post_id).replace("'", "''")+"' ,'"+str(term_taxonomy_id).replace("'", "''")+"' ,'0')")


def InsertTermsLocation(taxonomy, post_id, parent, p_slug, child, c_slug):

    term_id = ''
    checkterms = SelectionQuery("SELECT term_id FROM `wp_terms` where name='"+str(
        parent).replace("'", "''")+"' AND slug='"+str(p_slug).replace("'", "''")+"'")
    if(len(checkterms) == 0):
        ins_delete_update("INSERT INTO `wp_terms` (`name` ,`slug` ,`term_group`) VALUES (N'" +
                          str(parent).replace("'", "''")+"' ,N'"+str(p_slug).replace("'", "''")+"' ,'0')")
        getMaxID = SelectionQuery("SELECT max(term_id) FROM wp_terms")
        term_id = str(getMaxID[0][0])
    else:
        term_id = str(checkterms[0][0])
    term_taxonomy_id = ''
    checktax = SelectionQuery(
        "select term_taxonomy_id  from wp_term_taxonomy where term_id='"+term_id+"'")
    if(len(checktax) == 0):
        ins_delete_update("INSERT INTO `wp_term_taxonomy` (`term_id` ,`taxonomy` ,`description` ,`parent` ,`count`) VALUES (N'" +
                          str(term_id).replace("'", "''")+"' ,N'"+str(taxonomy).replace("'", "''")+"' ,'' ,'0' ,'0')")
        getMaxIDterm = SelectionQuery(
            "SELECT max(term_taxonomy_id) FROM wp_term_taxonomy")
        term_taxonomy_id = str(getMaxIDterm[0][0])
    else:
        term_taxonomy_id = str(checktax[0][0])
    # getMaxIDtermID=SelectionQuery("SELECT max(term_id) FROM wp_term_taxonomy")
    # parent_id=str(getMaxIDtermID[0][0])
    parent_id = term_id
    ins_delete_update("INSERT INTO `wp_term_relationships` (`object_id` ,`term_taxonomy_id` ,`term_order`) VALUES ('" +
                      str(post_id).replace("'", "''")+"' ,'"+str(term_taxonomy_id).replace("'", "''")+"' ,'0')")
    # child
    term_id1 = ''
    checkterms1 = SelectionQuery("SELECT term_id FROM `wp_terms` where name='"+str(
        child).replace("'", "''")+"' AND slug='"+str(c_slug).replace("'", "''")+"'")
    if(len(checkterms1) == 0):
        ins_delete_update("INSERT INTO `wp_terms` (`name` ,`slug` ,`term_group`) VALUES (N'" +
                          str(child).replace("'", "''")+"' ,N'"+str(c_slug).replace("'", "''")+"' ,'0')")
        getMaxID = SelectionQuery("SELECT max(term_id) FROM wp_terms")
        term_id1 = str(getMaxID[0][0])
    else:
        term_id = str(checkterms1[0][0])
    term_taxonomy_id1 = ''
    checktax1 = SelectionQuery(
        "select term_taxonomy_id  from wp_term_taxonomy where term_id='"+term_id1+"'")
    if(len(checktax1) == 0):
        ins_delete_update("INSERT INTO `wp_term_taxonomy` (`term_id` ,`taxonomy` ,`description` ,`parent` ,`count`) VALUES (N'"+str(
            term_id1).replace("'", "''")+"' ,N'"+str(taxonomy).replace("'", "''")+"' ,'' ,N'"+str(parent_id).replace("'", "''")+"' ,'0')")
        getMaxIDterm = SelectionQuery(
            "SELECT max(term_taxonomy_id) FROM wp_term_taxonomy")
        term_taxonomy_id1 = str(getMaxIDterm[0][0])
    else:
        term_taxonomy_id1 = str(checktax1[0][0])
    # getMaxIDtermID=SelectionQuery("SELECT max(term_id) FROM wp_term_taxonomy")
    # parent_id=str(getMaxIDtermID[0][0])
    # parent_id=term_id
    ins_delete_update("INSERT INTO `wp_term_relationships` (`object_id` ,`term_taxonomy_id` ,`term_order`) VALUES ('" +
                      str(post_id).replace("'", "''")+"' ,'"+str(term_taxonomy_id1).replace("'", "''")+"' ,'0')")

def process_item(item):

    checkexist = SelectionQuery("SELECT ID, post_author FROM `wp_posts` WHERE  post_title='"+item['title'].replace(
        "'", "''")+"' and post_name='"+item['specification']['slug'].replace("'", "''")+"'")
    
            
    if(len(checkexist) == 0):
        AuthorID = ''
        try:
            AuthorID = InserUserGetID(item['specification']['seller'], item['specification']['MobileNo'], item['specification']['Address'])
        except Exception as error:
            print(error)
        post_date = str(datetime.datetime.now())
        post_date_gmt = str(datetime.datetime.now())
        post_excerpt = ''
        post_status = 'publish'
        comment_status = 'closed'
        ping_status = 'closed'
        post_password = ''
        to_ping = ''
        pinged = ''
        post_modified = ''
        post_modified_gmt = ''
        post_modified_gmt = str(datetime.datetime.now())
        post_modified = post_modified_gmt
        post_content_filtered = ''
        post_parent = '0'
        guid = ''
        menu_order = '0'
        post_type = 'boats'
        post_mime_type = ''
        ins_delete_update("INSERT INTO `wp_posts` (`post_author` ,`post_date` ,`post_date_gmt` ,`post_content` ,`post_title` ,`post_excerpt` ,`post_status` ,`comment_status` ,`ping_status` ,`post_password` ,`post_name` ,`to_ping` ,`pinged` ,`post_modified` ,`post_modified_gmt` ,`post_content_filtered` ,`post_parent` ,`guid` ,`menu_order` ,`post_type` ,`post_mime_type`) VALUES (N'"+str(AuthorID).replace("'", "''").replace("'", "''")+"' ,N'"+str(post_date).replace("'", "''")+"' ,N'"+str(post_date_gmt).replace("'", "''")+"' ,N'"+str(item['description']).replace("'", "''")+"' ,N'"+str(item['title']).replace("'", "''")+"' ,N'"+str(post_excerpt).replace("'", "''")+"' ,N'"+str(post_status).replace("'", "''")+"' ,N'"+str(comment_status).replace("'", "''")+"' ,N'"+str(ping_status).replace("'", "''")+"' ,N'"+str(post_password).replace("'", "''")+"' ,N'"+str(item['specification']['slug']).replace("'", "''")+"' ,N'"+str(to_ping).replace("'", "''")+"' ,N'"+str(pinged).replace("'", "''")+"' ,N'"+str(post_modified).replace("'", "''")+"' ,N'"+str(post_modified_gmt).replace("'", "''")+"' ,N'"+str(post_content_filtered).replace("'", "''")+"' ,N'"+str(post_parent).replace("'", "''")+"' ,N'"+str(guid).replace("'", "''")+"' ,N'"+str(menu_order).replace("'", "''")+"' ,N'"+str(post_type).replace("'", "''")+"' ,N'"+str(post_mime_type).replace("'", "''")+"')")
        getMaxID = SelectionQuery("SELECT max(ID) FROM wp_posts")
        post_parent = str(getMaxID[0][0])
    else:
        post_parent = str(checkexist[0][0])
        AuthorID = checkexist[1]
        print('already exists')
    post_id = post_parent
    try:
        co = 1
        AllImages = item['pics']

        ii = 0
        for dct in AllImages:
            try:
                for key, value in dct.items():
                    ImageURL = value
                post_type = 'attachment'
                LocalImage = ImageURL
                im1 = ImageURL.split('/')
                im = im1[-1]
                # Set Download path here http://boatlistr.com/demo/wp-content/uploads/
                ImageURL='http://boatlistr.com/demo/wp-content/uploads/'+str(im)
                print(LocalImage)
                
                
                downloadImage(LocalImage,
                                './uploads/' + str(im))
                
                
                ins_delete_update("INSERT INTO `wp_posts` (`post_author` ,`post_date` ,`post_date_gmt` ,`post_content` ,`post_title` ,`post_excerpt` ,`post_status` ,`comment_status` ,`ping_status` ,`post_password` ,`post_name` ,`to_ping` ,`pinged` ,`post_modified` ,`post_modified_gmt` ,`post_content_filtered` ,`post_parent` ,`guid` ,`menu_order` ,`post_type` ,`post_mime_type`) VALUES (N'"+str(AuthorID).replace("'", "''").replace("'", "''")+"' ,N'"+str(post_date).replace("'", "''")+"' ,N'"+str(post_date_gmt).replace("'", "''")+"' ,'' ,N'boatimage"+str(co)+" "+item['title']+"' ,N'"+str(post_excerpt).replace("'", "''")+"' ,N'Inherit' ,N'open' ,N'"+str(ping_status).replace("'", "''")+"' ,N'"+str(post_password).replace("'", "''")+"' ,N'boatimage"+str(co)+" "+item['specification']['seller'].replace('\\n', '').replace("'", "''")+"' ,'' ,N'"+str(pinged).replace("'", "''")+"' ,N'"+str(post_modified).replace("'", "''")+"' ,N'"+str(post_modified_gmt).replace("'", "''")+"' ,N'"+str(post_content_filtered).replace("'", "''")+"' ,N'"+str(post_parent).replace("'", "''")+"' ,N'"+str(ImageURL).replace("'", "''")+"' ,N'"+str(menu_order).replace("'", "''")+"' ,N'"+str(post_type).replace("'", "''")+"' ,N'image/jpeg')")
                co = co+1

                if(ii == 0):
                    Image = ImageURL
                    ii = ii+1
            except Exception as df:
                print(df)
    except Exception as error:
        print(error)

    for key, value in (item['specification'].items()):
        Types = key
        Values = value
        meta_key = ''
        meta_key = Types
        meta_value = ''
        meta_value = Values
        if not Values:
            continue
        if(' ft' in meta_value):
            spMetaValueft = meta_value.split('ft')[0]
            spMetaValuein = meta_value.split(
                'ft')[1].replace("in", "")
            meta_keyft = meta_key.replace('.', '')+"_ft"
            meta_keyin = meta_key.replace('.', '')+"_in"
            ins_delete_update("INSERT INTO `wp_postmeta` (`post_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(post_id).replace(
                "'", "''")+"' ,N'"+str(meta_keyft).lstrip().rstrip().replace(" ", "_").lower()+"' ,N'"+str(spMetaValueft).strip().replace("'", "''")+"')")
            if not spMetaValuein.strip():
                spMetaValuein = '0'
            ins_delete_update("INSERT INTO `wp_postmeta` (`post_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(post_id).replace(
                "'", "''")+"' ,N'"+str(meta_keyin).lstrip().rstrip().replace(" ", "_").lower()+"' ,N'"+str(spMetaValuein).strip().replace("'", "''")+"')")
            continue

        if type(meta_value) == type([]):            
            meta_value = ', '.join(meta_value)
        if(meta_key.strip().lstrip().rstrip() == "Price"):
            meta_key = "base_"+meta_key
        ins_delete_update("INSERT INTO `wp_postmeta` (`post_id` ,`meta_key` ,`meta_value`) VALUES (N'"+str(post_id).replace(
            "'", "''")+"' ,N'"+str(meta_key).lstrip().rstrip().replace(" ", "_").lower()+"' ,N'"+str(meta_value).replace("'", "''")+"')")
        if(Types == "Engine Type"):
            InsertTerms(Values, Values.lower(), Types.replace(
                ' ', '_').lower(), post_id)
        if(Types == "Fuel Type"):
            InsertTerms(Values, Values.lower(), Types.replace(
                ' ', '_').lower(), post_id)
        if(Types == "Hull Material"):
            InsertTerms(Values, Values.lower(), Types.replace(
                ' ', '_').lower(), post_id)
        if(Types == "Fuel Tanks"):
            InsertTerms(Values, Values.lower(), Types.replace(
                ' ', '_').lower(), post_id)
        if(Types == "Location"):
            child = ''
            parent = ''
            try:
                child = Values.split(',')[0]
                parent = Values.split(',')[1]
            except:
                fg = ''
            InsertTermsLocation("boat_"+Types.replace(' ', '_').lower(
            ), post_id, parent, parent.lower(), child, child.lower())

        if(Types == "Class"):
            InsertTerms(Values, Values.lower(
            ), "boat_"+Types.replace(' ', '_').lower(), post_id)
        if(Types == "Type"):
            InsertTerms(Values, Values.lower(
            ), "boat_"+Types.replace(' ', '_').lower(), post_id)
    
    
class MainSpider(scrapy.Spider):
    name = 'main'
    urls = []

    def start_requests(self):
        with open('Link.txt', 'r') as links:
            self.urls = links.read().split('\n')
            yield scrapy.Request(url=self.urls[0], callback=self.check)
    
    def next_url(self, response):
        self.urls = self.urls[1:]
        if not self.urls:
            pass
        with open('Link.txt', 'w') as links:
            links.write('\n'.join(self.urls))
        return scrapy.Request(url=self.urls[0], callback=self.check)

        
    def check(self, response):
        title = response.xpath('//div[@class="inner"]/h1/text()').extract_first()
        if not title:
            with open('failed_links.txt', 'a') as fails:
                fails.write(response.url + '\n') 
            yield self.next_url(response)
            # print('no title')
            # yield scrapy.Request(url=response.url, callback=self.parse_halfpage, dont_filter=True)
        else:
            yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)
        
    def parse(self, response):
        boat = {}
        boat['title'] = response.xpath('//div[@class="inner"]/h1/text()').extract_first()
        boat['description'] = response.xpath('//div[@class="desc-text"]').extract_first().replace('<a data-more="More…" data-less="Show Less…" class="show-more__toggle" href="javascript:void(0);">Show More…</a>', '')
        boat['pics'] = []
        
        for img in response.xpath('//div[@class="carousel"]/ul/li'):
            boat['pics'].append({img.xpath('.//@data-alt').extract_first() : img.xpath('.//@data-src_w0').extract_first().split('?')[0]})        
        boat['specification'] = {}
        boat['specification']['slug'] = response.url.split('/')[-2]
        

        
        specification = response.xpath('//section[@class="boat-info"]')
        tables = specification.xpath('.//div[contains(@class, "collapsible")]')
        rows = tables.xpath('.//tr')
        for row in rows:
            value = row.xpath('.//td/text()').extract_first()
            if 'li' in row.extract():
                value = row.xpath('.//li/text()').extract()
            if '\n' in value:
                value = value.replace('\n', ' ')
            if ' x ' in value:
                value = value.split(' x ')[-1]
            if len(value) == 1 and type(value) == type([]):
                value = value[0]
            if 'gal' in value:
                value = value.replace('gal', '').strip()
            if len(value) == 1 and type(value) == type([]):
                value = value[0]
            if type(value) == type(' '):
                value.replace('\n', '')
            boat['specification'][row.xpath('.//th/text()').extract_first().strip()] = value

        
        presented_info = response.xpath('//div[@class="col-left"]')
        
        seller_info = presented_info.xpath('.//div[@class="contact-info"]/div[@class="seller-info"]')
        boat['specification']['seller'] = seller_info.xpath('.//h3/text()').extract_first().strip('\n').strip()
        
        boat['specification']['city'] = seller_info.xpath('.//div[@class="city"]/text()').extract_first().split(',')[0].strip('\n').strip()
        
        boat['specification']['country'] = seller_info.xpath('.//div[@class="city"]/text()').extract()[-1].replace('\n', '')
        
        if seller_info.xpath('.//div[@class="number"]/text()').extract_first():
            boat['specification']['MobileNo'] = seller_info.xpath('.//div[@class="number"]/text()').extract_first().replace("tel:", "").replace("1-855-AHOYMATE (", "").replace(")", "").replace("(", "").replace("Call Now", "").replace("\\n", "")
        boat['specification']['Address'] = ', '.join(seller_info.xpath('.//div[@class="street"]/text()').extract()).strip()
        
        process_item(boat)
        yield self.next_url(response)
    
    def parse_halfpage(self, response):
        boat = {}
        
        boat['title'] = response.xpath('//h2[@class="oem-page__title oem-page__title--no-margin"]/text()').extract_first()
        specification = response.xpath('//section[@id="specifications"]')
        rows = specification.xpath('.//div[@class="description-list__row"]')
        showmore = response.xpath('//div[@class="show-more__content"]')
        rows += showmore.xpath('.//div[@class="description-list__row"]')
        boat['specification'] = {}
        for row in rows:
            boat['specification'][row.xpath('.//dt/text()').extract_first().strip()] = row.xpath('.//dd/text()').extract_first().strip()
        boat['specification']['slug'] = response.url.split('/')[-2]
            
        process_item(boat) 
        yield self.next_url(response) 