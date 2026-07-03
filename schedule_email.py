import schedule
import time
import yagmail

def send_email():
    yag = yagmail.SMTP(
      user="khankeya961@gmail.com",
      password="hesh ynjh ysrp teck")

    yag.send(
      to =  "abilakhankeya@gmail.com",
      subject = "hi keya",
      contents= "Hello keya, its a just a test message from python. Hope you are doing well." \
      "Break the ice and have a great future ahead."\
     "From your future self , keya.")




print("Email sent successfully!")



schedule.every().day.at("05:00").do(send_email)

print("Scheduled message has been sent successfully!")



while True:
    schedule.run_pending()
    time.sleep(1)