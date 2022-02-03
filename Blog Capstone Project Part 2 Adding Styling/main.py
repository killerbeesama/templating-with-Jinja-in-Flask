from flask import Flask,render_template,request
from datetime import datetime
import requests

requested_post = requests.get("<url>").json()

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route("/")
def home():
    return render_template("index.html",data=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        data = request.form
        print(data['name'])
        print(data['email'])
        print(data['phonenumber'])
        print(data['message'])
        return render_template("contact.html",successful=True)
    else:
        return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    num_post = None
    for post in requested_post:
        if post['id'] == post_id:
            num_post = post
    return render_template("post.html", post=num_post)


if __name__ == "__main__":
    app.run(debug=True)