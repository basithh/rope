from flask import Flask, render_template,request
import requests
import xmltodict, json
import requests

abc = requests.get("https://news.google.com/news/rss")
final = xmltodict.parse(abc.text) 
news = []
news_brand = []

for i in final['rss']['channel']['item']:
  slit = i['title'].split(' - ')
  news.append(slit[0])
  news_brand.append(slit[1])
news_a = []

for i in news:
  r = requests.post(url= 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d8835d26-0739-4fb1-b737-f89434de6e65/v3/translate?version=2018-05-01',auth=('apikey','UB3ywwG25aA-_99H1LoCDb9zocK_zC4kEMcp0BanFYIe'),headers= {'Content-Type': 'application/json','User-Agent':'PostmanRuntime/7.28.0'},json={"text": [i], "model_id":"en-ml"}).json()
  z = requests.post(url= 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d8835d26-0739-4fb1-b737-f89434de6e65/v3/translate?version=2018-05-01',auth=('apikey','UB3ywwG25aA-_99H1LoCDb9zocK_zC4kEMcp0BanFYIe'),headers= {'Content-Type': 'application/json','User-Agent':'PostmanRuntime/7.28.0'},json={"text": [i], "model_id":"en-ta"}).json()
  q = requests.post(url='https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/bb593022-7298-4d19-bf15-3d42c42b6f76/v3/tone?version=2017-09-21',auth=('apikey','WMpWmAqNfjjgLpb0DsbXp154wyfm3hAK37EnsWbG-G_u'),headers= {'Content-Type': 'application/json','User-Agent':'PostmanRuntime/7.28.0'},json={'text':i}).json()
  news_a.append({
      'news':i,
      'tamil':r['translations'][0]['translation'],
      'mal':z['translations'][0]['translation'],
      'tone':q['document_tone']['tones']
  })



app = Flask(__name__)
def converter(abc):
    abc.replace(' ','+')
    r = requests.get(f'https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/bb593022-7298-4d19-bf15-3d42c42b6f76/v3/tone?version=2017-09-21&text={abc}',auth=('apikey','WMpWmAqNfjjgLpb0DsbXp154wyfm3hAK37EnsWbG-G_u'))
    return r.json()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=[ 'POST'])
def login():
    abc = request.form['Name']
    return converter(abc)

@app.route('/news')
def register():
    return render_template('register.html',newf=news_a)

if __name__ == '__main__':
    app.run()
