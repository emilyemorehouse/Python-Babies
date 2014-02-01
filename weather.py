#! /usr/bin/env python3
import requests
from lxml import etree

""" Baby script to scrape the current weather."""

def get_etree(url):
    urltext = requests.get(url).text
    return etree.HTML(urltext)

def weather():
    print ("Input the 3 character city symbol. Type 'exit' to quit.")
    city = input().strip()
    while city != "exit":
        url = "http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=" + city
        tree = get_etree(url)
        current_temp_xpath = '//current_observation/temperature_string//text()'
        current_temp = tree.xpath(current_temp_xpath)
        print (current_temp)
        city = input().strip()

if __name__ == '__main__':
    weather()

