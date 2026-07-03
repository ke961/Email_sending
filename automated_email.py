import yagmail


yag = yagmail.SMTP(
    user="khankeya961@gmail.com",
    password="hesh ynjh ysrp teck")

yag.send(
    to =  "abilakhan961@gmail.com",
    subject = "hi keya",
    contents= "Hello keya, its a just a test message from python"


)

print("Email sent successfully!")

