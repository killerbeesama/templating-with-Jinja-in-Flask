from flask import Flask,render_template
from post import Post

post = Post()
posts = post.get_post()

app = Flask(__name__)

@app.route("/")
def blog():
    return render_template("index.html", data=posts)

@app.route("/<int:num>")
def read_blog(num):
    return render_template("post.html", data=posts, blog_post=num)

if __name__ == "__main__":
    app.run(debug=True)