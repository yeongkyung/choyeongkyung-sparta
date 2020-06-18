from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import json
import requests
from bs4 import BeautifulSoup

def remove_dupe_dicts(l):
    return [dict(t) for t in {tuple(d.items()) for d in l}]


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
