# importing libraries 
from flask import Flask, request
from flask_mail import Mail, Message 
import subprocess
import logging
import os
import json
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__) 
CORS(app)
mail = Mail(app) # instantiate the mail class 

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'medbigi2000@gmail.com'
app.config['MAIL_PASSWORD'] = 'ahuf jzbw osrc liyv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

scrapy_project_path = os.path.join(os.path.dirname(__file__))

google_dict={
    'https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Damazon%2Bkdp%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dkindle%2Bdirect%2Bpublishing%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dself%2Bpublishing%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dai%2Bbook%2Blawsuit%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dai%2Bwriting%2Blawsuit%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dai%2Bcreated%2Bbook%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
    'https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen':'https://consent.google.com/ml?continue=https://news.google.com/search?q%3Dauthor%26hl%3Den-US%26gl%3DUS%26ceid%3DUS:en&gl=FR&hl=en-US&cm=2&pc=n&src=1',
}

# message object mapped to a particular URL ‘/’ 
def get_recipients_from_file(file_path):
    with open(file_path, 'r') as file:
        recipients = file.read().splitlines()
    return recipients


@app.route("/") 
def index():
    recepientsList=get_recipients_from_file('email.txt')
    output_file_path = os.path.join(scrapy_project_path, 'changes.json')
    changed=[]
    changed_urls=""
    print(output_file_path)
    spider_name = "MonitorAmazonKDP"
   
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-O", "changes.json"], stderr=subprocess.STDOUT)
    
    with open(output_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for i in range(0,len(data)):
        if data[i]['change']:
            changed.append(data[i]['change'])


    for i in range(0,len(changed)):
        if i<len(changed)-1:
            changed_urls+=list(changed[i].keys())[0]+ ", "
        if i==len(changed)-1:
            changed_urls+=list(changed[i].keys())[0]

        

    msg = Message( 
                'Change summary', 
                sender ='medbigi2000@gmail.com', 
                recipients = recepientsList
                ) 
    

    if len(changed)!=0:
        msg.body = "The following urls have changed: \n" + changed_urls
    else:
        msg.body = "No changes in the past 24 hours."
    mail.send(msg)

    return 'sent'


@app.route('/email')
def setEmail():
    new_email = request.args.get('new')
    with open('email.txt', 'a') as file:
        file.write(new_email + '\n')
    return 'added'

@app.route('/publisher')
def publisher():
    spider_name="SearchPbw"
    output_file_path = os.path.join(scrapy_project_path, 'resultPbw.json')
    output = subprocess.check_output(['scrapy', 'crawl', spider_name, "-O", "resultPbw.json"], stderr=subprocess.STDOUT)

    app.logger.debug(output)

    with open(output_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    return data

@app.route('/guardian')
def guardian():
    spider_name="SearchGuardian"
    output_file_path = os.path.join(scrapy_project_path, 'resultGuardian.json')
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-O", "resultGuardian.json"], stderr=subprocess.STDOUT)

    with open(output_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    return data

@app.route('/google')
def google():
    spider_name="SearchGoogle"
    output_file_path = os.path.join(scrapy_project_path, 'resultGoogle.json')
    params = request.args.get('url')
    # url_to_scrape = google_dict[params]
    url_to_scrape = params
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-O", "resultGoogle.json",'-a','url='+url_to_scrape], stderr=subprocess.STDOUT)
    with open(output_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    return data



if __name__ == '__main__': 
    app.run(host='0.0.0.0') 
