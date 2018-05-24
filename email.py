import smtplib
#import email.utils
from email.mime.text import MIMEText
import UTILS
from UTILS import *

me = 'binitpm@gmail.com'

recipients = [ 'binitbsn@gmail.com', 'binitpm@gmail.com']
subject = 'testing Status Report_1'


def setupLogger():
	log = logging.getLogger('')
	log.setLevel(logging.DEBUG)
	format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	ch = logging.StreamHandler(sys.stdout)
	ch.setFormatter(format)
	log.addHandler(ch)
	fh = handlers.RotatingFileHandler(LOGFILE, maxBytes=(10000*5), backupCount=7)
	fh.setFormatter(format)
	log.addHandler(fh)


# def send_mail(buff):
# 	try:

# 		msg=MIMEMultipart('alternative')
# 		msg['Subject'] = subject
# 		msg['From'] = me
# 		msg['To'] = ", ".join(recipients)
# 		part = MIMEText(buff,'html')
# 		msg.attach(part)
# 		s = smtplib.SMTP('10.150.100.141')
# 		s.UseDefaultCredentials = False;
# 		s.sendmail(me, recipients, msg.as_string())
# 		print "sending email......"
# 		s.sendmail(me, recipients,)
# 		s.quit()
# 	except Exception as error:
# 		print error


def send_mail(buff):
	
	msg=MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = ", ".join(recipients)
	part = MIMEText(buff,'html')
	msg.attach(part)
	s = smtplib.SMTP('10.150.100.141')
	s.UseDefaultCredentials = False;
	s.sendmail(me, recipients, msg.as_string())
	print "sending email......"
	s.sendmail(me, recipients,)
	s.quit()
	print error










send_mail(recipients)