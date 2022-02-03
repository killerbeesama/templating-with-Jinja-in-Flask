import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/guess/<username>")
def guess(username):
    agify_r = requests.get(f"https://api.agify.io?name={username}").json()
    ag = agify_r['age']
    genderize_r = requests.get(f"https://api.genderize.io?name={username}").json()
    nam = genderize_r['name']
    gen = genderize_r['gender']
    return render_template("index.html",name=nam, age=ag, gender=gen)

@app.route("/blog")
def blog():
    r = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html",data=r)

app.run(debug=True)