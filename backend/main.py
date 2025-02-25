# st-1 install required libraries and import
from twilio.rest import Client
from datetime import datetime,timedelta
import time
import os

# st-2 twilio cred
account_sid=os.getenv("SID")
auth_token=os.getenv("TOKEN")


client = Client(account_sid, auth_token)

# st-3 designing send msg func
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
            
            
        )
        print(f'Message sent successfully! Message SID {message.sid}')
    except Exception as e:
        print('An error occured!')    
        
#st-4 user input

name = input('Enter the recipient name:')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g, +911233455123 ):')    
message_body = input (F'Enter the message you want to send to {name}:')

# st-5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM_DD):') #2025-02-25
time_str = input('Enter the time to send the message (HH:MM in 24hour format):') #18:30

# date time 
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The given time is already gone. Please enter a future time!")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    
    #wait until the schedule time
    time.sleep(delay_seconds) #1000sec
    
    #send the message
    send_whatsapp_message(recipient_number, message_body)
    
    
    
    




    
        


