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
    bakerys = list(db.bakery.find({},{'_id':False}))
    return jsonify({'result': 'success','bakerys_list': bakerys})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)