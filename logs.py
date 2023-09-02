
import pandas as pd
import smtplib as sm
import logging



logging.basicConfig(filename='logs_customer.txt',level=logging.DEBUG,
 format='%(asctime)s:%(message)s')

sheet_id='1OzgLMJti-0lMN8nXKGwgxOcEW7dma_uH5-NffkQWX9I'

df =pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
email_col=df.get("Email")
print(email_col)
Order_details=df.get("Order Details")

 

try:

    logging.debug(Order_details)

    filename = "logs_customer.txt"
    attachment = open(r"C:\Users\danish\Documents\3-1\DT\code\logs_customer.txt", "rb")
  


except Exception as e:
    
    print(e)


    