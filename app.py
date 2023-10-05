import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['SECRET_KEY'] = 'kjhdigfjegfuw'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SLS'] = False
app.config['MAIL_USERNAME'] = 'ajay20003kumar@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'ajay20003kumar@gmail.com'

mail = Mail(app)

@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(subject="New Message",body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}",

                      recipients=["ajay20003kumar@gmail.com"])
        mail.send(msg)
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
