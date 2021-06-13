from flask import Flask, render_template,request
import requests

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

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
