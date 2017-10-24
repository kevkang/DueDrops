from flask import render_template
from flask_mail import Message
from duedrops import app, mail


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')

@app.route('/halloo')
def send_mail():
	app.logger.warning('sample message')
	msg = Message("halloo",
				  sender="noreply@duedrop.link")
	msg.add_recipient("9544595718@vtext.com")
	msg.body = "testing"
	msg.html = "<b>testing</b>"
	mail.send(msg)
	return render_template('index.html')
