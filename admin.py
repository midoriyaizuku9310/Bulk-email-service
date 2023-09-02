
import pandas as pd
import smtplib as sm
import logging
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.message import EmailMessage 

logging.basicConfig(filename='logs_admin.txt',level=logging.DEBUG,
 format='%(asctime)s:%(message)s')

logging.basicConfig(filename='logs_customer.txt',level=logging.DEBUG,
 format='%(asctime)s:%(message)s')

sheet_id='1OzgLMJti-0lMN8nXKGwgxOcEW7dma_uH5-NffkQWX9I'

df =pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
email_col=df.get("Email")
print(email_col)
Order_details=df.get("Order Details")

 



user = "testtest6235@gmail.com"
password = "tykvbelgoxpjesew"

try:
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    from_= user
    to_=email_col

    messege=MIMEMultipart()
    messege['subject']="Here are your Order Details"
    messege["from"]="testtest6235@gmail.com"
    messege2=MIMEMultipart("your order details are saved")
    
    filename = "logs_admin.txt"
    attachment = open (r"C:\Users\danish\Documents\3-1\DT\code\logs_admin.txt","rb")
    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment; filename= %s" % filename)
    messege2.attach(p)

    

    server.sendmail(from_,to_,messege.as_string())
    print("sent successfully")
    print(Order_details)
    server.sendmail(from_,"md994955@gmail.com",messege2.as_string())
    
    logging.debug(email_col)
    logging.debug(Order_details)
    msg = MIMEMultipart
    filename = "logs_admin.txt"
    attachment = open(r"C:\Users\danish\Documents\3-1\DT\code\logs_admin.txt", "rb")
  


except Exception as e:
    
    print(e)


    