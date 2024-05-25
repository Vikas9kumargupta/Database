from flask import Flask, render_template, request, jsonify

from db.create import createTables, createUser, createProduct
from db.GetUsers import getAllusers, getSpecificUsers
from db.UserOperation import approveUserAccess,blockUserAccess,levelUpdateUserAccess

app = Flask(__name__)

@app.route('/createUser',methods = ['POST'])
def create_user():

    name =  request.form['name']
    password= request.form['password']
    email = request.form['email']
    address= request.form['address']
    phone = request.form['phone']
    pincode  = request.form['pincode']

    dbRes=createUser(name=name, Email=email, Address=address, Phone=phone,password=password,PinCode=pincode)
    
    if dbRes==True:  
        return jsonify({'success':200,"message":"Successfully created"})
    else:
       return jsonify({'success':400,"message":"unable to create User"}) 

@app.route('/createProduct',methods = ['POST'])
def create_product():

    productName = request.form['productName']
    price = request.form['price']
    category = request.form['category']
    stock = request.form['stock']
    isActive = request.form['isActive']

    prodRes = createProduct(prodName = productName, price = float(price), Category= category, Stock= int(stock), isActive = bool(isActive))

    print(prodRes)
    if prodRes==True:  
        return jsonify({'success':200,"message":"Successfully created"})
    else:
       return jsonify({'success':400,"message":"unable to create User"})



@app.route('/getAllUsers', methods=['GET'])
def getAllUser():
    return getAllusers()

@app.route('/getSpecificUser', methods=['GET'])
def getSpecificUser():
    userID = request.form['userID']
    return getSpecificUsers(userId=str(userID))

@app.route('/approveUserAccess', methods=['PATCH'])
def approveUser_Access():
    userId= request.form['userID']
    approved= request.form['approved']
    approveUserAccess(id=userId, approved=approved)
    return "Access Approve Updated Successfully"

@app.route('/blockUserAccess', methods=['PATCH'])
def blockUser_Access():
    userId= request.form['userID']
    blocked= request.form['blocked']
    blockUserAccess(id=userId, blocked= blocked)
    return "Access Blocked Updated Successfully"


@app.route('/levelUpdateUserAccess', methods=['PATCH'])
def updateUser_Access():
    userId= request.form['userID']
    level = request.form['Level']
    levelUpdateUserAccess(id=userId, level=level)
    return "Access Level Updated successfully"

if __name__ == "__main__":
    createTables()
    app.run()