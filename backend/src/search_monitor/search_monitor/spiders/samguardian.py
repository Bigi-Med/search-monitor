import scrapy

class SearchGuardian(scrapy.Spider):
    name = "SearchGuardian"
    keywords_to_search = ['amazon', 'kdp', 'kindle direct publishing', 'books', 'author', 'midjouney', 'chatgpt']
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/books"]
    base_url="https://www.theguardian.com"

    def parse(self, response):
        book_section = response.css('section#books')
        links = book_section.css('ul li .dcr-45mok7 a::attr(href)').getall()

        for url in links:
            yield scrapy.Request(self.base_url + url, callback=self.parse_book,cb_kwargs={'full_url': self.base_url + url})

       
    
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
    
    def parse_book(self, response,full_url):
        title = response.css('h1::text').get()
        paragraphs = response.css('p::text, p *::text').getall()

        found_keywords = self.search_for_keywords(title, paragraphs, self.keywords_to_search)

        
        if found_keywords:
            yield {
                'found': found_keywords,
                'url':full_url
                }

    