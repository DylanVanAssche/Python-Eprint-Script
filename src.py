import sys
import smtplib

import email
import email.mime.application

# Your email address
sender_address = 'email@emailserver.com'

# Printer email address
printer_address = 'yourPrinter@hpeprint.com'

instance = email.mime.Multipart.MIMEMultipart()
instance['Subject'] = 'Print Job'
instance['From'] = sender_address
instance['To'] = printer_address

if len(sys.argv) > 1:

    file = sys.argv[1]

    fp = open(file, 'rb')
    attachment = email.mime.application.MIMEApplication(fp.read(), _subtype="png")
    fp.close()
    attachment.add_header('Content-Disposition', 'attachment', filename=file)
    instance.attach(attachment)

    # Enter your mail server, defaults to Yahoo
    mail = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    mail.starttls()

    # Enter username and password here
    mail.login('yourEmailUsername', 'yourEmailPassword')
    mail.sendmail(sender_address, printer_address, instance.as_string())
    mail.quit()

    print('sent job %s to %s from %s' % (file, printer_address, sender_address))

else:

    print("Sending Failed, No Readable Document Provided")