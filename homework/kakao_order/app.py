from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      

@app.route('/')
def home():
    return render_template('order.html')

@app.route('/order', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']
    
    addorder = {
        'name':name_receive,
        'quantity':quantity_receive,
        'address':address_receive,
        'phonenumber':phonenumber_receive,
    }

    db.orders.insert_one(addorder)

    return jsonify({'result':'success', 'msg': '주문이 완료되었습니다'})


@app.route('/order', methods=['GET'])
def read_order():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)