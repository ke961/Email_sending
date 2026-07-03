import yagmail


yag = yagmail.SMTP(
    user="khankeya961@gmail.com",
    password="hesh ynjh ysrp teck")

yag.send(
    to =  "abilakhankeya@gmail.com",
    subject = "hi keya",
    contents= "Hello keya, its a just a test message from python. Hope you are doing well." \
    "Break the ice and have a great future ahead."\
    "From your future self , keya."


)

print("Email sent successfully!")

