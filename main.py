from flask import Flask, render_template, request

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

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

@app.route("/resume.html")
def resume():
    return render_template("resume.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        # Process form data (e.g., store in database, send email, etc.)
        return 'Form submitted successfully!'
    return render_template('contact.html')

# @app.route("/liveresume.html")
# def liveresume():
#     return render_template("liveresume.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

