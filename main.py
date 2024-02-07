from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'isuckmyowntoesforfun@gmail.com'
app.config['MAIL_PASSWORD'] = 'sfmq gfey ymmc wznu'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yes')
def yes():
  msg = Message('Subject: Valentine\'s Day Message',
  sender='isuckmyowntoesforfun@gmail.com',
  recipients=['ryan.rlyh@gmail.com'])
  msg.body = "Happy Valentine's Day, Ryan! You have received a Valentine's Day message."
  mail.send(msg)
  return render_template('yes.html')


app.run()
