from os import name
from flask.wrappers import Request
import razorpay

from flask import Flask,render_template,request
from razorpay.resources import payment
app= Flask(__name__)

@app.route('/')
def mainpage():
    return render_template("website.html")

@app.route('/pay', methods=['POST'])
def pay():
    global payment,name,amount
    name = request.form.get('username')
    amount = request.form.get('amount')
    client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY","YOUR_RAZORPAY_SECRET"))

    data = { "amount": int(amount)*100, "currency":"INR", "receipt": "#101" }
    payment = client.order.create(data=data)
    return render_template("pay.html",payment=payment)

if __name__  == "__main__":
    app.run(debug=True)

