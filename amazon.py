#! /usr/bin/env python3
import requests
from lxml import etree

""" Baby script to scrape the top 20 books on Amazon."""

def get_etree(url):
    urltext = requests.get(url).text
    return etree.HTML(urltext)

def amazon():
    url = "http://www.amazon.com/gp/bestsellers/books/ref=sv_b_2"
    tree = get_etree(url)

    rank_xpath = './/*[@class="zg_rankNumber"]//text()'
    rank = (tree.xpath(rank_xpath))

    title_xpath = './/*[@class="zg_title"]/a//text()'
    title = (tree.xpath(title_xpath))

    byline_xpath = './/*[@class="zg_byline"]//text()'
    byline = tree.xpath(byline_xpath)
    author = []

    for item in byline:
        item = item.replace("\n", "")
        item = item.replace("by ", "")
        author.append(item)

    # for i in range(0,20):
    #     print (rank[i], title[i])
    #     print ("By: ", author[i])

    for rank, title, author in zip(rank, title, author):
        print (rank, title)
        print (author)


if __name__ == '__main__':
    amazon()