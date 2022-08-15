import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Your name"
email["to"] = "Recievers email address"
email["Subject"] = "This is a test email"


email.set_content(html.substitute({"TestPerson": Jesper}), "html")


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Your email address", "Your Password")
    smtp.send_message(email)
    print("All good, boss!")

