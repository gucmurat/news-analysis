# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:56:40 2022

@author: Murat
"""

from scrapy.spiders import XMLFeedSpider
from bs4 import BeautifulSoup
from newspaper import Article
import datetime

class NewsSpider(XMLFeedSpider):
    name = 'news'
    start_urls = ['https://www.theguardian.com/business/economics/rss', #theguardian /20 news-last 3 days
                  # 'https://www.economist.com/finance-and-economics/rss.xml', #economist /100 news-last 4 months
                  'https://feeds.a.dj.com/rss/RSSMarketsMain.xml', #wall-street-journal /20 news-last 3 days
                  'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258', #cnbc-economy /30 news-last 10 days
                  'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664', #cnbc-finance /30 news-last 5 days
                  'https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml', #nytimes /20 news-last 10 days
                  # # 'http://rss.cnn.com/rss/money_news_international.rss', #cnn
                  'https://www.reutersagency.com/feed/?best-sectors=economy&post_type=best', #reuters-economy /10 news-last 4 months
                  'https://www.reutersagency.com/feed/?best-sectors=commodities-energy&post_type=best', #reuters-energy /10 news-last 1 month
                  'https://www.investing.com/rss/news_14.rss', #investing-economy /10 news-last 3 days
                  # 'http://feeds.marketwatch.com/marketwatch/StockstoWatch/', #stocks /10 news-last 2 months
                  
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/14-Economic%20Research%20And%20Reports/feedTitle/GlobeNewswire%20-%20Economic%20Research%20And%20Reports',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/5-Bankruptcy/feedTitle/GlobeNewswire%20-%20Bankruptcy',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/6-Bond%20Market%20News/feedTitle/GlobeNewswire%20-%20Bond%20Market%20News',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/7-Business%20Contracts/feedTitle/GlobeNewswire%20-%20Business%20Contracts',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/9-Company%20Announcement/feedTitle/GlobeNewswire%20-%20Company%20Announcement',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/77-Exchange%20Members/feedTitle/GlobeNewswire%20-%20Exchange%20Members',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/17-Financing%20Agreements/feedTitle/GlobeNewswire%20-%20Financing%20Agreements',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/80-Investment%20Fund%20Information/feedTitle/GlobeNewswire%20-%20Investment%20Fund%20Information',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/83-Investment%20Opinion/feedTitle/GlobeNewswire%20-%20Investment%20Opinion',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/81-Market%20Research%20Reports/feedTitle/GlobeNewswire%20-%20Market%20Research%20Reports',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/62-Net%20Asset%20Value/feedTitle/GlobeNewswire%20-%20Net%20Asset%20Value',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/39-Stock%20Market%20News/feedTitle/GlobeNewswire%20-%20Stock%20Market%20News',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/43-Technical%20Analysis/feedTitle/GlobeNewswire%20-%20Technical%20Analysis',
                  # 'https://www.globenewswire.com/RssFeed/subjectcode/68-Trading%20Information/feedTitle/GlobeNewswire%20-%20Trading%20Information',
                  ]
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = {}
        try:
            article = Article(self.get_link(node))
            article.download()
            article.parse()
        except:
            pass
        article.nlp()
        item['date'] = str(article.publish_date.strftime('%Y-%m-%d')),
        item['title'] = self.get_title(node)
        item['author'] = article.authors
        item['link'] = self.get_link(node)
        item['content'] = article.text
        item['summary'] = article.summary
        return item

    def get_title(self, node):
        return node.xpath('title/text()').extract_first() or ""

    def get_link(self, node):
        return node.xpath('link/text()').extract_first() or ""

    def get_content(self, node):
        raw_html = node.xpath('description/node()').extract_first()
        if not raw_html:
            return []
        soup = BeautifulSoup(raw_html, 'lxml')
        results = ''
        for child in soup.body.children:
            item = self.get_item(child)
            if item:
                results+=item
        return results

    def get_item(self, soup):
        if soup.name == 'p':
            return self.get_text(soup)
        elif soup.name == 'div' and soup.find('ul'):
            return self.get_links(soup)
        else:
            return None

    def get_text(self, soup):
        text = soup.text.strip()
        if text:
            return text
        else:
            return None

    def get_links(self, soup):
        links = []
        for li in soup.ul.find_all('a'):
            link = li.get('href')
            links.append(link)
        return {"type": "links",
                "content": links}