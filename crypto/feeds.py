from urllib.request import urlopen
import urllib.request
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import json
import re
import os
import time
import ssl
import datetime
from datetime import datetime
from time import gmtime, strftime
from xml.sax.saxutils import unescape

def retrive_url(url):
    url_request = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    url_read = urlopen(url_request).read()
    return url_read

def date_convert_timezone(date_input):
    date_split = re.split('\s+', date_input)
    week, day, month, year, time = date_split[0:5]
    time = time.split(':')
    if len(time) == 2:
        hour, minute = time[0:2]
        second = '00'
    else:
        hour, minute, second = time[0:3]

    pubdate_convert = week + ' ' + day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute + ':' + second + ' ' + '+0000'
    return pubdate_convert

def compareDate(t1,t2): #get earlier time
    pubdate_exist_format = time.strptime(t1, '%a, %d %b %Y %H:%M:%S %z')
    pubdate_newfound_format = time.strptime(t2, '%a, %d %b %Y %H:%M:%S %z')

    if (pubdate_exist_format <= pubdate_newfound_format) == True: #if a new identical article is published later than 'exist', keep 'exist'.
        result = 'keep old source'
    else:
        result = 'update original source'

    return result

def rssfeed_generator(jsonfilename_for_converting, customize_feedname, feeds_link, rss_description):#translate json to XML for rss
    with open(jsonfilename_for_converting, 'r') as f:                                #require vaiable: exsiting exist
        existing20 = json.load(f)
        f.close()

    rss_xml = ET.Element('rss', version="2.0")
    channel_xml = ET.SubElement(rss_xml, 'channel')

    ET.SubElement(channel_xml, "title").text = customize_feedname
    ET.SubElement(channel_xml, "link").text = feeds_link
    ET.SubElement(channel_xml, "description").text = rss_description
    ET.SubElement(channel_xml, "lastBuildDate").text = (strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    for feeds in existing20:
        item_xml = ET.SubElement(channel_xml, 'item')
        ET.SubElement(item_xml, "title").text = '<![CDATA[ ' +feeds['title'] + ' ]]>'
        ET.SubElement(item_xml, "pubDate").text = feeds['pubDate']
        ET.SubElement(item_xml, "link").text = feeds['link']
        ET.SubElement(item_xml, "guid", isPermaLink="false").text = feeds['guid']
        ET.SubElement(item_xml, "description").text = '<![CDATA[ ' + feeds['description'] + ' ]]>'

    rss_xml1= ElementTree.tostring(rss_xml, encoding='utf8', method='xml')
    rss_xml2 = rss_xml1.decode()
    rss_xml3 = unescape(rss_xml2)
    return rss_xml3

def sumfeeds_generator(feedslist_url):
    summarry_feeds = []
    script_list = re.findall('(http.*?)\\\n',
                             (retrive_url(feedslist_url)).decode('utf-8'))
    for newsfeed_url in script_list:
        try:  # skip empty xml url
            feeds_str = retrive_url(newsfeed_url)
        except:
            pass
        else:
            try:
                feeds_xml = ET.fromstring(feeds_str)
            except BaseException:
                pass
            else:
                items = feeds_xml.findall('channel/item')
                for item in items:
                    json_sub = {}
                    try:
                        if item.find('title').text == None:
                            json_sub['title'] = 'None'
                        else:
                            json_sub['title'] = item.find('title').text
                    except AttributeError:
                        json_sub['title'] = 'N/A'
                    try:
                        if item.find('pubDate').text == None:
                            json_sub['pubDate'] = (strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
                        else:
                            date1 = item.find('pubDate').text
                            json_sub['pubDate'] = date_convert_timezone(date1)
                    except AttributeError:
                        json_sub['pubDate'] = (strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
                    try:
                        if item.find('link').text == None:
                            json_sub['link'] = 'None'
                        else:
                            json_sub['link'] = item.find('link').text
                    except AttributeError:
                        json_sub['link'] = 'N/A'
                    try:
                        if item.find('guid').text == None:
                            json_sub['guid'] = 'None'
                        else:
                            json_sub['guid'] = item.find('guid').text
                    except AttributeError:
                        json_sub['guid'] = 'N/A'
                    try:
                        if item.find('description').text == None:
                            json_sub['description'] = 'None'
                        else:
                            json_sub['description'] = item.find('description').text
                    except AttributeError:
                        json_sub['description'] = 'N/A'
                    summarry_feeds.append(json_sub)
    return summarry_feeds

def f_availability_checking(filename, file_type):
    if filename in os.listdir(os.curdir):
        with open(filename,'r') as f:
            file_content = json.load(f)
            f.close()
    else:
        if file_type == 'dict':
            file_content = {}
        elif file_type == 'list':
            file_content = []
    return file_content

def add_new_feeds_into_database(summarry_feeds,data_storage_dic):
    for item in summarry_feeds:
        if item.get('title') not in data_storage_dic.keys():
            data_storage_dic[item.get('title')] = item
        else:
            t1 = data_storage_dic[item.get('title')].get('pubDate')  # existing item's pubDate
            t2 = item.get('pubDate')  # new found item's pubDate
            if compareDate(t1, t2) == 'keep old source':
                pass
            elif compareDate(t1, t2) == 'update original source':
                data_storage_dic[item.get('Title')] = item
    return data_storage_dic

def json_generator(filename, data_put_in):
    with open(filename, 'w') as file:
        json.dump(data_put_in, file, indent=2)
        file.close()

def get_kw_from_url(kd_url):
    try:
        keywords = (retrive_url(kd_url)).decode()
    except:
        keywords = None
    else:
        if keywords.endswith('\n') is True:
            keywords = keywords[0:(len(keywords) - 1)]
        else:
            pass
    return keywords

def feed_selecion_for_client(keywords, data_storage_dic, existing_select_feeds_for_client):
    keywords_list = keywords.split('\n')
    for keyword2 in keywords_list:
        keyword2_cap = keyword2.capitalize()
        keyword2_allcap = keyword2.upper()
        for key in data_storage_dic.keys():
            feed = data_storage_dic[key]
            if (keyword2 in feed['title']) or (keyword2_cap in feed['title']) or (keyword2_allcap in feed['title']) or \
                    (keyword2 in feed['link']) or (keyword2_cap in feed['link']) or (keyword2_allcap in feed['link']):
                if (feed['title'] in str(existing_select_feeds_for_client)):
                    pass
                else:
                    existing_select_feeds_for_client.append(feed)
                    print('news found for Vyrde :')
                    print(feed['title'])
                    print('===================================')
        existing_select_feeds_for_client = sorted(existing_select_feeds_for_client, key=lambda x: datetime.strptime(x['pubDate'], '%a, %d %b %Y %H:%M:%S %z'),
                           reverse=True)
    return existing_select_feeds_for_client
#===================================================================================================================
#===================================================================================================================
ssl._create_default_https_context = ssl._create_unverified_context

while True:
    print('wait for 300s')
    #time.sleep(300)
    sum_feeds = sumfeeds_generator('http://35.237.98.100/index/sources-index.txt')

    #generate_unduplicate_feeds_dictionary_of_list(dic)

    dic = f_availability_checking('allfeeds.json', 'dict')

    add_new_feeds_into_database(sum_feeds, dic)

    json_generator('allfeeds.json', dic)

    existing_vyrde_feeds = f_availability_checking('vyrde.json', 'list')

    keywords = get_kw_from_url('http://35.237.98.100/index/keywords-index.txt')

    if keywords == None: pass
    else:
        vyrde_selcet_feed = feed_selecion_for_client(keywords, dic, existing_vyrde_feeds)

    json_generator('vyrde.json', existing_vyrde_feeds)

    json_generator('vyrde_20_for_xml.json', existing_vyrde_feeds[0:20])

    vyrde_xml = rssfeed_generator('vyrde_20_for_xml.json', 'Vyrde news feed', 'https://vyrde.io', ' ')

    vyrder20_file = open('xml_vyrde_20_newsfeed.xml', 'w')
    vyrder20_file.write(vyrde_xml)
    vyrder20_file.close()
