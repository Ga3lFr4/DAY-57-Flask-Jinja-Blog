from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index.html", posts=blog_posts)

@app.route('/post/<int:id>')
def get_post(id):
    blog_posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    post_index = id - 1
    post = blog_posts[post_index]
    post_title = post["title"]
    post_text = post["body"]
    return render_template("post.html", title=post_title, body=post_text)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
