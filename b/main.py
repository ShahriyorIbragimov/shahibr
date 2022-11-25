from flask import Flask, render_template, request
import webview
# from models import Users

app = Flask(__name__,static_folder='./static',template_folder='./templates')

@app.route("/", methods = ["GET","POST"])
def mainpage ():
    # if request.method == "POST":
    #     email = request.form("em")
    #     password = request.form("pw")
    #     print(email)
    #     print(password)
    #     new_users = Users(email=email, password=password)
    #     new_users.save()

    return render_template("index.html")

@app.route("/about")
def aboutpage ():
    return render_template("about.html")

@app.route("/Success")
def Spage ():
    return render_template("Success.html")

webview.create_window("My First Exe",app,width=600,height=500,resizable=True)
webview.start()
