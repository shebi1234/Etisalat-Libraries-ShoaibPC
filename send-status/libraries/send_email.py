import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import pandas as pd


class send_email(object):
    mail_body = ""

    # def agentname(self):
    #     df = pd.read_excel('E:/BIMA-Parallel/agents.xlsx')
    #     return df['Name'].to_string()
    # def rowscount(self):
    #     df = pd.read_excel('E:/BIMA-Parallel/agents.xlsx', error_bad_lines=False)
    #     try:
    #         return int(df.shape[0])
    #     except Exception as e:
    #         raise e

    def send_email_file(self, count):
        # names = send_email()
        # NAMES = names.agentname()

        # PIDs = send_email()
        # pid = PIDs.rowscount()

        mail_body = """<!DOCTYPE html> <html lang="en"> <head> <link href="Tests/style.css" rel="stylesheet"> </head> 
				<body> <h2>This is the email from Mercurail Minds</h2> <p>Below is the table including MSISDN numbers of the 
				memebers against their MO and pids</p> <table style = "border: 1px solid black; border-collapse:collapse; 
				width:60%; height:20%;"> <thead> <tr> <th style = "border: 1px solid Black; border-collapse:collapse; 
				background-color: Green; color: White; width:80px; text-align: left;"> Accounts </th> <th style = "border: 
				1px solid Black; border-collapse:collapse; background-color: Green; color: White; width: 40px; text-align: 
				left;""> Count </th> </tr> <td style = "border: 1px solid black; border-collapse:collapse; color: Black;">In 
				Progress</td> <td style = "border: 1px solid black; border-collapse:collapse; color: Black; 
				text-align:right;">{}</td> </thead> </table> </body> </html>""".format(count)
        try:
            # The mail addresses and password
            sender_address = 'rpamercurialminds@gmail.com'
            sender_pass = 'Heytherealeesho123'
            receiver_address = 'rpamercurialminds@gmail.com'
            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Output XML File.'
            # The body for the mail
            message.attach(MIMEText(mail_body, 'html'))
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(sender_address, sender_pass)  # login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        except Exception as e:
            raise e

# email_send = send_email()
# email_send.send_email_file()

# 'hi {0}'.format(self.rowscount())

# def send_email_file(self):
#     mail_body = 'hi {0} The total number of ids are {1}'.format(self.mail_message(), format(self.rowscount()))
