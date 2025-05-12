# email_sender.py
# This file shows how a Python script might send tickets to vendors via email.
# SMTP setup and sending logic is commented out for learning and safe reference only.

# import smtplib
# from email.message import EmailMessage

# def send_email_ticket(config, ticket):
#     # Setup the email message
#     # msg = EmailMessage()
#     # msg['Subject'] = f"[{ticket['severity']}] {ticket['issue']}"
#     # msg['From'] = config['from']
#     # msg['To'] = config['to']

#     # msg.set_content(f\"\"\"
#     # Issue: {ticket['issue']}
#     # Severity: {ticket['severity']}
#     # Contact: {ticket['contact']}
#     # \"\"\")

#     # Connect to SMTP server and send
#     # with smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port']) as smtp:
#     #     smtp.login(config['username'], config['password'])
#     #     smtp.send_message(msg)

#     # For demo purposes only
#     # print("Email ticket sent (simulated).")

