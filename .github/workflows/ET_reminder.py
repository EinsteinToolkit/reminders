'''
Reminder users of ucoming ET call
'''
import os, sys

# Import smtplib for the actual sending function
import smtplib

DST_WARNING=""
os.environ["TZ"] = 'America/Chicago'
CHICAGO_TIME = os.popen("date -d '9:00am tomorrow' +%s").read().strip()
os.environ["TZ"] = 'Europe/Berlin'
BERLIN_TIME = os.popen(f"date -d @{CHICAGO_TIME} +'%H:%M'").read().strip()
del os.environ["TZ"]

if BERLIN_TIME != "16:00":
  DST_WARNING="""
** DAYLIGHT SAVING TIME WARNING **
Please note that the US / EU has already / not yet transitioned to /
from daylight saving time. The phone call will be at $BERLIN_TIME Central EU
time.
""""

mesg = f"""
Subject: Einstein Toolkit Meeting Reminder

Hello,

Please consider joining the weekly Einstein Toolkit phone call at
9:00 am US central time on Thursdays. For details on how to connect
and what agenda items are to be discussed, use the link below.
{DST_WARNING}
https://docs.einsteintoolkit.org/et-docs/Main_Page#Weekly_Users_Call
--The Maintainers
""" 
sender = "reminders@einsteintoolkit.org"
receiver = "user@einsteintoolkit.org"

# Send the message via our own SMTP server.
s = smtplib.SMTP('mail.einsteintoolkit.org')
s.sendmail(sender, receiver, mesg)
s.quit()
