import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import requests
class ConsentHandlingSpider(scrapy.Spider):
    keywords_to_search = ['amazon', 'kdp', 'kindle direct publishing', 'books', 'author', 'midjouney', 'chatgpt']
    name = 'SearchGoogle'
    
    # start_urls = ['https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dself%2Bpublishing%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en%26allowcookies%3DACCEPTEER%2BALLE%2BCOOKIES&gl=FR&hl=en-US&cm=2&pc=n&src=1'] 
    start_urls = ['https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen']
    base_url = 'https://news.google.com/'




    def parse(self, response):
        # for element in keywords_dict:
        #     yield scrapy.Request(self.base_url + element, callback=self.parse_forward, cb_kwargs={'title':keywords_dict[element]})
        yield scrapy.Request(response.url, callback=self.bypass_consent)

    def bypass_consent(self,response):
        articles = response.css('c-wiz.FffXzd')
        myArticle = articles.css('.xrnccd')
        title = myArticle.css('h3')
        myTitles = title.css('a::text').getall()[:40]
        link = myArticle.css('a::attr(href)').getall()
        final_links_temp = link[:40]
        final_links_temp_dup = final_links_temp[::2]
        final_links = [row[2:] for row in final_links_temp_dup]

        keywords_dict = {link: title for link, title in zip(final_links, myTitles)}

        yield{
            'dict':keywords_dict,
            'url':response.url
        }


    def search_for_keywords(self,title, paragraphs, keywords):
        found_keywords = set()

        # Search for keywords in the title
        title_keywords = [keyword for keyword in keywords if keyword.lower() in title.lower()]
        found_keywords.update(title_keywords)

        # Search for keywords in each paragraph
        for paragraph in paragraphs:
            paragraph_keywords = [keyword for keyword in keywords if keyword.lower() in paragraph.lower()]
            found_keywords.update(paragraph_keywords)

        return found_keywords
    

    def parse_forward(self,response,title):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(response.url)

        final_url = driver.current_url

        driver.quit()

        yield scrapy.Request(final_url, callback=self.parse_article, cb_kwargs={'title':title})

    
    def parse_article(self,response,title):

        full_articles = response.css('p::text, p *::text').getall()


        # Call the function to search for keywords in the title and paragraphs
        found_keywords = self.search_for_keywords(title, full_articles, self.keywords_to_search)

        if found_keywords:
            yield {
                'url':response.url,
                'keywords':found_keywords
            }


