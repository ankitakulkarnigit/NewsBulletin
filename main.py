from newsapi import NewsApiClient
from flask import Flask , render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
newsapi = NewsApiClient(api_key='03bcfb11eafb4ab2a9a787551ee1e86d')
sources = newsapi.get_sources()

@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): 
    top_headlines = newsapi.get_top_headlines()
    return render_template('index.html', top_headlines=top_headlines, country=sources)

@app.route("/form")
def form():
    head_title = "Today's Headlines"
    return render_template('form.html', sources=sources, head_title=head_title)

@app.route('/form-handler', methods=['POST'])
def handle_data():
    head_title = "Search result for " + request.form['keyword']
    all_articles = newsapi.get_everything(q=request.form['keyword'],
                                      sources=request.form['sources'],
                                      from_param=request.form['from-date'],
                                      to=request.form['to-date'],
                                      language='en',
                                      sort_by='relevancy')
    return render_template('index.html', top_headlines=all_articles, head_title=head_title)

app.run(debug = True) 