import yagmail

html = """
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background-color:#f2f2f2;font-family:Arial,Helvetica,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" style="background:#f2f2f2;padding:30px 0;">
<tr>
<td align="center">

<table width="600" cellpadding="0" cellspacing="0"
style="background:#ffffff;border-radius:10px;border:1px solid #dddddd;">

<tr>
<td align="center" style="background:#6C63FF;padding:30px;border-radius:10px 10px 0 0;">
<h1 style="color:white;margin:0;">
Welcome to My Email
</h1>
</td>
</tr>

<tr>
<td style="padding:30px;">

<p style="font-size:18px;">
Hello <b>Keya</b>,
</p>

<p style="font-size:16px;color:#444444;line-height:1.6;">
This email was sent automatically using
<b>Python</b> and <b>Yagmail</b>.
</p>

<table cellpadding="0" cellspacing="0" border="0">
<tr>
<td bgcolor="#4CAF50" style="border-radius:6px;">
<a href="https://www.python.org"
style="
display:inline-block;
padding:14px 28px;
font-size:16px;
font-family:Arial;
color:#ffffff;
text-decoration:none;
font-weight:bold;">
Visit Python
</a>
</td>
</tr>
</table>

<br>

<p style="font-size:16px;color:#444444;">
Hope you are doing well.
</p>

<hr>

<p style="font-size:13px;color:gray;">
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