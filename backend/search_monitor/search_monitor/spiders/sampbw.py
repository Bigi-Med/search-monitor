import scrapy


class SearchPublisherWeekly(scrapy.Spider):
    keywords_to_search = ['amazon', 'kdp', 'kindle direct publishing', 'books', 'author', 'midjouney', 'chatgpt']
    name = "SearchPbw"
    allowed_domains = ["publishersweekly.com"]
    start_urls = ["https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/index.html","https://www.publishersweekly.com/pw/by-topic/industry-news/index.html"]


    def parse(self, response):

        articles = response.css('.article-list')
        article_div_list = articles.css('ul')
        articleToScrape = set(article_div_list.css('a::attr(href)').getall()) #extract link to full article

        for article in articleToScrape:
            full_url = "https://www.publishersweekly.com/" + article
            yield scrapy.Request(full_url, callback=self.parse_article,cb_kwargs={'full_url': full_url})
        

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
    
    def parse_article(self, response,full_url):

        full_body = response.css('.article')
        title = full_body.css('h1::text').get()
        articles = full_body.css('p.article::text').getall()

        # Call the function to search for keywords in the title and paragraphs
        found_keywords = self.search_for_keywords(title, articles, self.keywords_to_search)

        if(found_keywords):
            yield {
                'found': found_keywords,
                'url':full_url
                }
            
            