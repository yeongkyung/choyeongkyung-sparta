from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import json
import requests

def remove_dupe_dicts(l):
    return [dict(t) for t in {tuple(d.items()) for d in l}]


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')    

@app.route('/report', methods=['POST'])
def saving():
    bakery_name = request.form['name_give']
    bakery_comment = request.form['comment_give']
    report = {'name': bakery_name, 'comment': bakery_comment}

    db.reports.insert_one(report)

    return jsonify({'result': 'success'})

@app.route('/places', methods=['GET'])
def bakery_list():
    filter = request.args.get('filter')
    filter_list = filter.split(',')
    bakerys = []
    for category in filter_list:
        bakery = list(db.bakery.find({category: True}, {'_id': False}))
        bakerys.extend(bakery)
    # 리스트에 중복된 딕셔너리 제거
    bakerys_list = remove_dupe_dicts(bakerys)
    return jsonify({'result': 'success', 'bakerys_list': bakerys_list})


@app.route('/reviews', methods=['GET'])
def insta_crawl():
    keyword = request.args.get('filter')

    #이미지 크롤링
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path="choyeongkyung-sparta/bread_map/python_selenium_crawl/webdriver/chromedriver.exe", chrome_options=chrome_options)
    url ="https://www.instagram.com/explore/tags/"+str(keyword)
    
    driver.get(url)
    sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    reviews = soup.select('div.EZdmt > div > div > div')

    image_list = []
    for image in reviews:
        image_tag = image.select_one('a > div > div > img')['src']
        image_list.append(image_tag)
    driver.close()
    return jsonify({'result': 'success', 'image_list': image_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
