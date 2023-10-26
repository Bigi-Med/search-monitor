import scrapy
import requests
class SearchAuthGuild(scrapy.Spider):
    name='SearchAuthGuild'
    start_urls=["https://authorsguild.org/news/?sort=date-DESC"]

    def parse(self,response):
        header = """Host: authorsguild.org
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
        Accept: */*
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate, br
        Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        X-Requested-With: XMLHttpRequest
        Content-Length: 78
        Origin: https://authorsguild.org
        Connection: keep-alive
        Referer: https://authorsguild.org/news/?sort=date-DESC
        Cookie: ssi--sessionId=b3a913b1-4fe8-7ed2-b8ba-ce800b7b337a; _ga_EWNVVVK1M3=GS1.1.1698259218.6.1.1698259762.0.0.0; _ga=GA1.1.617756737.1694859902; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; CookieLawInfoConsent=ey2JuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOnRydWUsInBlcmZvcm1hbmNlIjp0cnVlLCJhbmFseXRpY3MiOnRydWUsImFkdmVydGlzZW1lbnQiOnRydWUsIm90aGVycyI6dHJ1ZX0=; viewed_cookie_policy=yes; ssi--lastInteraction=1698259216929
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: same-origin
        TE: trailers"""

        body = """action=search__news_listing&sort=date-DESC&keyword=&page=1&security=362cf84d77"""

        header_lines = header.split('\n')

# Create a dictionary from the lines
        headers = {}
        for line in header_lines:
            if line.strip():  # Skip empty lines
                key, value = line.split(': ', 1)
                key=key.strip()
                value=value.strip()
                headers[key] = value

        final_body = {}
        for line in final_body:
            if line.strip():  # Skip empty lines
                key, value = line.split('= ', 1)
                key=key.strip()
                value=value.strip()
                final_body[key] = value

        newResponse = requests.post('https://authorsguild.org/wp/wp-admin/admin-ajax.php',data=final_body,headers=headers)
        # test = newResponse.css('.ajax-results . result-card').get()

        # print(headers)
        print(newResponse)

        # yield{
        #     'test':test
        # }