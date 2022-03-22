from flask import Flask, render_template , request, session, redirect, flash
from datetime import datetime
import pywhatkit


app = Flask(__name__)
app.secret_key = 'the random string'
@app.route("/", methods=["GET","POST"])
def home():
    if(request.method=="POST"):
        time1 = request.form.get("time1")
        time2 = request.form.get("time2")
        phone_no= request.form.get("phone")
        message = request.form.get("message")
        pywhatkit.sendwhatmsg(phone_no, message, time1, time2)
    return render_template("contact.html")


app.run()