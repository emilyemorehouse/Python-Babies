#! /usr/bin/env python3
import requests
from lxml import etree

""" Baby script to scrape the current stock value."""

def get_etree(url):
    urltext = requests.get(url).text
    return etree.HTML(urltext)

def ticker():
    print ("Input the 3 character ticker symbol. Type 'exit' to quit.")
    ticker = input().strip()
    while ticker != "exit":
        url = "http://www.google.com/finance?q=" + ticker
        tree = get_etree(url)
        current_val_xpath = '//*[@class="pr"]/span//text()'
        current_val = tree.xpath(current_val_xpath)
        print (current_val)
        ticker = input().strip()

if __name__ == '__main__':
    ticker()