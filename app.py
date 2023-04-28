from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

#Home page route
@app.route("/")
def home():
	return render_template("index.html")

#products page route
@app.route("/product")
def product():
	return render_template("product.html")

#abouts us page route	
@app.route("/about_us")
def about_us():
	return render_template("aboutUs.html")

#account page route
@app.route("/account")
def account():
	return render_template("account.html")

#financial page route
@app.route("/financial")
def financial():
    return render_template("financial.html")

#payment page route
@app.route("/payment")
def payment():
      return render_template("payment.html")

#route to add a new user details (INSERT) to register database
@app.route("/adduser", methods = ['POST','GET'])
def adduser():
	#add user data from POST submitted by the register form
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm-pass']

            #connect to Register database and insert data to register table
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO register(email,password,confirm_password) VALUES(?,?,?)",(email,password,confirm_password))

                con.commit()
                msg = "User succesfully registered, Login to start shopping!!"
        except:
                con.rollback()
                msg = "Error in registeration"
        finally:
            con.close()
            #redirect the user to products page to continue shopping
            return render_template("account.html", msg = msg)
    
@app.route("/userlogin", methods = ['POST','GET'])
def userlogin():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE email = ? AND password = ?", (email, password))
                data = cur.fetchone()
                if data:
                    # if email and password match, redirect to products page                   
                    msg = "Logged in Succesfully"
                    return render_template("product.html")
                else:
                    # if email and password don't match, show error message
                    msg = "Incorrect email or password, please try again."
                
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template("product.html",msg=msg)
         
            
#route to add address and payment details (INSERT) to address and payment database
@app.route("/addaddress", methods = ['POST','GET'])
def addaddress():
	#add user address and payment from POST submitted by the shipment and payment form
    if request.method == 'POST':
        try:
            name = request.form['Name']
            email = request.form['Email']
            address = request.form['Address']
            city = request.form['City']
            state = request.form['option']
            zip = request.form['Zip-code']

            card = request.form['Credit-card-number']
            exp_month = request.form['Exp-Month']
            year = request.form['option']
            cvv = request.form['CVV']

            #connect to database and insert data to address and payment table
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()

                cur.execute("INSERT INTO address(name,email,address,city,state,zip) VALUES(?,?,?,?,?,?)",(name,email,address,city,state,zip))
                con.commit()

                cur.execute("INSERT INTO payment(card,exp_month,year,cvv) VALUES(?,?,?,?)",(card,exp_month,year,cvv))
                con.commit()

                msg = "Your order is placed. Thank you for shopping with us!"
        except:
                con.rollback()
                msg = "Error in payment details"
        finally:
            con.close()
            #redirect the user to home page
            return render_template("index.html", msg = msg)

if __name__ == "__main__":
    app.run(debug=True)