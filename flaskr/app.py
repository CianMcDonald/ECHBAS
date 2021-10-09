from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os.path

#Setup Flask
app = Flask(__name__)

#Route to Default Page (# python -m flask run (to run app))
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    page = 'index.html'
    # use post to send user's data
    if request.method == 'POST':
    #Connect to db
        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()
        # get data entered by user
        email = request.form['email']
        password = request.form['password']

        # for admin to check in terminal
        #print(email, password)

        # query used to verify that the email and password is in our database
        verify_query = "SELECT email, password FROM users WHERE email='"+ email +"' AND password='"+ password +"'"
        cursor.execute(verify_query)
        
        # if the result is zero the passsword/email is incorrect (not in the db)
        result = cursor.fetchall()
        if len(result) == 0:
            # retry login
            error = "Sorry! Your email or password is incorrect."
            page = 'index.html'
        else:
            print("yay")
            # if its right bring them to their homepage
            page = 'home.html'
    return render_template(page,  error=error)

