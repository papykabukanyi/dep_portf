from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route("/work.html")
def work():
    return render_template("work.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/components.html")
def components():
    return render_template("components.html")

# @app.route("/liveresume.html")
# def liveresume():
#     return render_template("liveresume.html")







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

