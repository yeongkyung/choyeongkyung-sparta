from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def bakery_list():
    # 1. bakery 목록 전체 검색
    bakery = list(db.bakery.find({},{'_id':False})
    # 2. 성공하면 success 메시지와 함께 bakery_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','bakery_list':bakery})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)