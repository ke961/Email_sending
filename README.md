# 📧 Python Automated Email Sender

## Project Overview

This project is a Python-based automated email sender developed using the **Yagmail** library and **Gmail SMTP**. It allows users to send both plain text and HTML-formatted emails. The project also includes support for scheduling emails to be sent automatically at a specified time.

---

## Features

- Send emails using Gmail SMTP
- HTML-formatted emails
- Professional email template
- Scheduled email sending
- Secure authentication using Gmail App Password
- Easy to customize

---

## Project Structure

```
Email/
│
├── automated_email.py      # Sends email immediately
├── schedule_email.py       # Sends email automatically at a scheduled time
├── email.html              # HTML email template
├── README.md
└── requirements.txt
```

---

## File Description

### 1. automated_email.py

This file sends an email immediately after execution.

Functions:
- Connects to Gmail SMTP
- Authenticates using Gmail App Password
- Sends HTML email
- Displays success or error messages

---

### 2. schedule_email.py

This file schedules emails to be sent automatically.

Functions:
- Uses the Schedule library
- Sends email at a specified time
- Runs continuously until stopped

Example:

```python
schedule.every().day.at("18:00").do(send_email)
```

---

### 3. email.html

This file contains the HTML template used as the email body.

Features:
- Colored header
- Styled text
- Clickable button
- Professional layout

---

## Requirements

Python 3.11+

Required Libraries

```
pip install yagmail
pip install schedule
pip install keyring
```

Or install everything using:

```
pip install -r requirements.txt
```

---

## Gmail Setup

1. Enable Google Two-Step Verification.
2. Create a Gmail App Password.
3. Replace the App Password in the Python code.
4. Do not use your Gmail login password.

---

## How to Run

### Send Email Immediately

```
python automated_email.py
```

### Send Scheduled Email

```
python schedule_email.py
```

---

## Technologies Used

- Python
- Yagmail
- SMTP
- HTML
- Schedule Library

---

## Future Improvements

- GUI using Tkinter or CustomTkinter
- Email attachments
- Multiple recipients
- Excel/CSV recipient list
- Email history
- Birthday reminder
- AI-generated email content

---

## Author

Keya 
