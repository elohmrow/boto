import smtplib
import jira_creds
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
fromaddr = "bradley.andersen@magnolia-cms.com"
toaddr = "cs-support@magnolia-cms.com"

description = None

if (len(sys.argv) != 2):
    sys.exit(1)
else:
    description = sys.argv[1]

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "MUNIN WARNING"
 
body = description
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, jira_creds.login['password'])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
