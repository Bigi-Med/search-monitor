# importing libraries 
from flask import Flask 
from flask_mail import Mail, Message 
import subprocess
import os
import json

app = Flask(__name__) 
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
output_file_path = os.path.join(scrapy_project_path, 'changes.json')

# message object mapped to a particular URL ‘/’ 
@app.route("/") 
def index():
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
                recipients = ['medbigi2000@gmail.com'] 
                ) 
    

    if len(changed)!=0:
        msg.body = "The following urls have changed: \n" + changed_urls
    else:
        msg.body = "No changes in the past 24 hours."
    mail.send(msg)

    return 'sent'

if __name__ == '__main__': 
    app.run(host='0.0.0.0') 
