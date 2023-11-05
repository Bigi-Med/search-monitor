import scrapy
import json


class MonitorAmazonKDP(scrapy.Spider):
    name="MonitorAmazonKDP"
    start_urls=["https://kdp.amazon.com/en_US/help/topic/G200672390","https://kdp.amazon.com/en_US/help/topic/G200743940","https://kdp.amazon.com/en_US/help/topic/G200952510","https://kdp.amazon.com/en_US/help/topic/G200652170","https://kdp.amazon.com/en_US/help/topic/G202173620","https://kdp.amazon.com/en_US/help/topic/G201097560","https://kdp.amazon.com/en_US/help/topic/G200743940","https://kdp.amazon.com/en_US/help/topic/G200672400","https://kdp.amazon.com/en_US/help/topic/G6GTK3T3NUHKLEFX","https://kdp.amazon.com/en_US/help/topic/G202187870","https://kdp.amazon.com/en_US/help/topic/G202192170","https://kdp.amazon.com/en_US/help"]
    # start_urls=["http://localhost:8000/guinea.html","http://localhost:8001/guinea2.html","https://kdp.amazon.com/en_US/help/topic/G200952510","https://kdp.amazon.com/en_US/help/topic/G200652170","https://kdp.amazon.com/en_US/help/topic/G202173620","https://kdp.amazon.com/en_US/help/topic/G201097560","https://kdp.amazon.com/en_US/help/topic/G200743940","https://kdp.amazon.com/en_US/help/topic/G200672400","https://kdp.amazon.com/en_US/help/topic/G6GTK3T3NUHKLEFX","https://kdp.amazon.com/en_US/help/topic/G202187870","https://kdp.amazon.com/en_US/help/topic/G202192170","https://kdp.amazon.com/en_US/help"]
    BASE_FILE_PATH="myResultsAmazon.json"
    url_dict={}
    change_dict={}

    def compare(self, new_article,response_url):
        self.change_dict.clear()
        with open(self.BASE_FILE_PATH, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)



        # Extract the existing articles from the data
        existing_articles = data[response_url]

        if len(existing_articles) != len(new_article):
            data[response_url] = new_article
            with open('myResultsAmazon.json', 'w') as json_file:
                json.dump(data, json_file, 
                                indent=4,  
                                separators=(',',': '))
            self.change_dict[response_url]='Change'
        else:
            for i in range(len(new_article)):
                if new_article[i] != existing_articles[i]:
                    data[response_url] = new_article
                    with open('myResultsAmazon.json', 'w') as json_file:
                        json.dump(data, json_file, 
                                        indent=4,  
                                        separators=(',',': '))
                    self.change_dict[response_url]='Change'
                    break
        
        
        return self.change_dict


    def parse(self,response):
        article=response.css('.a-section.a-spacing-large.help-body *::text').getall()

        # cleaning the articles

        article = [line.replace('\n','') for line in article]
        article = [line.replace('\t','') for line in article]
        article = [line.replace('\r','') for line in article]

        article = [item for item in article if item.strip() !=""]
        
        self.url_dict[response.url]=article
        
        self.compare(article,response.url)
        
        print("*******************************************TEST***************************")
        # print(change)

        # TRUE: CHANGE EXISTS
        # FALSE: NO CHANGE

        yield{
            'change':self.change_dict
        }



        # with open('myResultsAmazon.json', 'w') as json_file:
        #     json.dump(self.url_dict, json_file, 
        #                         indent=4,  
        #                         separators=(',',': '))

