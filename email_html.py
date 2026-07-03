import yagmail

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Python Email</title>
</head>

<body style="margin:0;padding:0;background-color:#f2f2f2;font-family:Arial,Helvetica,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f2f2f2">
<tr>
<td align="center">

<table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border:1px solid #dddddd;">

<tr>
<td align="center" bgcolor="#6C63FF" style="padding:30px;">
<h1 style="margin:0;color:#ffffff;font-size:32px;">
Welcome to My Email
</h1>
</td>
</tr>

<tr>
<td style="padding:35px;">

<p style="font-size:18px;color:#333333;margin-top:0;">
Hello <strong>Keya</strong>,
</p>

<p style="font-size:16px;color:#555555;line-height:26px;">
This email was sent automatically using
<strong>Python</strong> and
<strong>Yagmail</strong>.
</p>

<table cellpadding="0" cellspacing="0" border="0">
<tr>
<td bgcolor="#4CAF50">
<a href="https://www.python.org"
style="display:inline-block;padding:14px 28px;color:#ffffff;text-decoration:none;font-size:16px;font-weight:bold;font-family:Arial;">
Visit Python
</a>
</td>
</tr>
</table>

<p style="font-size:16px;color:#555555;line-height:26px;margin-top:30px;">
Hope you are doing well.
</p>

<hr style="border:none;border-top:1px solid #dddddd;">

<p style="font-size:13px;color:#999999;">
This is an automated email generated using Python.
</p>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

try:
    yag = yagmail.SMTP(
        user="khankeya961@gmail.com",
        password="dxni cmta jlig pvsn"
    )

    yag.send(
        to="abilakhankeya@gmail.com",
        subject="Hi Keya",
        contents=html
    )

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)