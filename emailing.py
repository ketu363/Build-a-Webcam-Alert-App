# this library use to send the mail
import smtplib

# this give the meta-data about the images
import imghdr


# This image class create image object instance
from email.message import EmailMessage

# Email sender and pass
SENDER = "Nishantketu363@gmail.com"
PASSWORD = "terhdngjfvloabfo"

# Receiver email address
RECEIVER = "Nishantketu363@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey! we just saw a new customer")

    # adding the image to the email
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    # sending out the email and port for gmail is 587
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    # start the gmail server
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")

