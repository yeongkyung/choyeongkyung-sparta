from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
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
    bakerys=[]
    for category in filter_list:
        bakery = list(db.bakery.find({category:True},{'_id':False}))
        bakerys.extend(bakery)
    # 리스트에 중복된 딕셔너리 제거하는 방법 찾아야 함
    return jsonify({'result': 'success','bakerys_list': bakerys})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)