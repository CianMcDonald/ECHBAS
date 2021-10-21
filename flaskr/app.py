from flask import Flask, render_template, request, redirect, flash
import qrcode
import sqlite3
import os

QR_FOLDER = os.path.join('static', 'qr_photos')

#Setup Flask
app = Flask(__name__)
#set the UPLOAD FOLDER (this is the default images folder) to a new folder where qrs are saved
app.config['UPLOAD_FOLDER'] = QR_FOLDER

def QRgen(ppsno, fname, sname):
    """
    Function that creates the image of the qr with the fullname and pps of the person
    and saves this image to the static images folder
    """
    # Creat the qr code image
    qr = qrcode.QRCode(
        version = 1,
        box_size = 15,
        border = 5
    )
    #setting the data in qr code
    qrdata = fname + "," + sname + "," + ppsno
    #add the data
    qr.add_data(qrdata)
    #make the qr code
    qr.make(fit=True)
    img = qr.make_image(fill = 'black', back_color = "white")
    #save image to new static folder qr_photos
    img.save('static/qr_photos/qrdata.png')
    
#Route to Default Page (# python -m flask run (to run app))
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Function that runs checks the user logging is correct and displays home page
    with qr code.
    """
    user_image=None
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
        verify_query = "SELECT email, password, ppsno, fname, sname FROM users WHERE email='"+ email +"' AND password='"+ password +"'"
        cursor.execute(verify_query)
        
        # if the result is zero the passsword/email is incorrect (not in the db)
        result = cursor.fetchall()
        if len(result) == 0:
            # retry login
            error = "Sorry! Your email or password is incorrect."
            page = 'index.html'
        else:
            # get all data for qr
            for row in result:
                print(result)
                ppsno = row[2]
                fname = row[3]
                sname = row[4]
            # generate qr code
            QRgen(ppsno, fname, sname)
            # if its right bring them to their homepage
            page = 'home.html'
            # set the image on homepage to qr code
            user_image = 'static/qr_photos/qrdata.png'
    return render_template(page, user_image=user_image, error=error)

