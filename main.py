from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/works")
@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route("/work")
@app.route("/work.html")
def work():
    return render_template("work.html")

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template("about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

@app.route("/resume")
@app.route("/resume.html")
def resume():
    return render_template("resume.html")

def send_email(subject, email, message):
    msg = MIMEText(f"Subject: {subject}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = 'Incoming Porfolio Message!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        # Process form data (e.g., store in database, send email, etc.)
        send_email(subject, email, message)
        return render_template('emailsent.html')
    return render_template('contact.html')

# @app.route("/liveresume.html")
# def liveresume():
#     return render_template("liveresume.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

