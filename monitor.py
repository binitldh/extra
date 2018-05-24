import subprocess
import os
import sys
import time
import datetime
import logging
import platform
from subprocess import Popen, PIPE
import smtplib

machine= platform.node()

def run_command(cmd):
    process = Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout, stderr

cmd1 = "ps aux | awk '{sum+=$3} END {print sum}'"
cmd2 = "ps aux | awk '{sum+=$4} END {print sum}'"
cmd3 = "df -h | awk '{print $5}'"


cpu, err = run_command(cmd1)


if err:
    print "ERROR: "+err
cpu_use = cpu.splitlines()[0]                         

print "CPU usage perventage is: " cpu_use               ### CPU usage
#print type(cpu_use)

memory, err = run_command(cmd2)
memory_use = memory.splitlines()[0]
print "Memory usage percentage is: " memory_use        ### Memory usage



def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except Exception as e:
        print ("failed to send mail: ", e)



#send_email('binitpm@gmail.com', 'binit000', 'binitbsn@gmail.com', 'system health check', 'system consuming high memory' )

if float(cpu_use) >= 90:
    print 'sending email...'
    #send_email('binitpm@gmail.com', 'binit000', 'binitbsn@gmail.com', 'subject', 'body' )


space, err = run_command(cmd3)

print "Free space is: " , space

if err:
    print "ERROR-" , err
var = space.splitlines()

print var

buff = []
for item in var:
    try:
        buff.append(int(item.strip('%')))
    except Exception as error:
        pass

print buff

if max(buff) > 3:
    print("%s: sending email" %datetime.datetime.now())
    send_email('binitpm@gmail.com', 'binit000', 'binitbsn@gmail.com', machine+' : system health check', 'high disk usage: %s percent' % max(buff))





# x = subprocess.check_output(["uptime"])

# print x

# y = subprocess.check_output(["ps aux | awk '{for(i=1;i<=NF;i++)$i=(a[i]+=$i)}END{print}'"])

# z = os.system("ps aux | awk '{for(i=1;i<=NF;i++)$i=(a[i]+=$i)}END{print}'")

# w = os.system("ps aux | awk '{sum+=$4} END {print sum}'")



