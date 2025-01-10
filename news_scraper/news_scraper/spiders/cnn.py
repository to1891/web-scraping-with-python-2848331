from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle


class CnnSpider(SitemapSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    sitemap_urls = ['https://www.cnn.com/sitemap/news.xml']
    # sitemap_urls = ['https://www.cnn.com/sitemaps/article-2024-01.xml']

    def parse(self, response):
        article = NewsArticle()
        # <script data-rh="true">
        print("hello   --------")
        print(article)
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1/text()').get()
        article['description'] = response.xpath(
            '//meta[@name="description"]/@content').get()
        article['date'] = response.xpath(
            '//meta[@itemprop="datePublished"]/@content').get()
        article['author'] = response.xpath(
            '//meta[@itemprop="author"]/@content').get()
        if article['author']:
            article['author'] = article['author'].replace(', CNN', '')
        article['text'] = response.xpath(
            '//section[@data-zone-label="bodyText"]/div[@class="l-container"]//*/text()').getall()
        return article
