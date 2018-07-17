from flask import Flask, render_template
import ConfigParser
import sendgrid
import os
from sendgrid.helpers.mail import *

app = Flask(__name__)
Config = ConfigParser.ConfigParser()
Config.read("app.config.example")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/certificado", methods=("POST", ))
def submeteCertificado():
    return render_template("error.html")

def enviarEmail():
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(Config.get('SEND_GRID', 'ApiUser')))
    from_email = Email(Config.get('SEND_GRID', 'ApiUser'))
    to_email = Email("test@example.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

def anexarCertificado():
    """Build attachment mock."""
    attachment = Attachment()
    attachment.content = ("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNl"
                          "Y3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
    attachment.type = "application/pdf"
    attachment.filename = "balance_001.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "Balance Sheet"
    return attachment

if __name__ == '__main__':
    app.run()
