import string
import random
import smtplib
import sys
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#normie = "mail"
randomAdress =  string.lowercase + string.digits + "@gmail.com"
subject = string.lowercase + string.digits
def clear():
	os.system("cls")

def banner():
	sys.stdout.write('''
               .........               
            ###((/////((###            
         ###//*,.......,**/###         
      .#(//.................,/(##      
     ##/*,,,,,,,,,,,,,,,,,,,,,*//#     
    #//*,,,,,,,,,,,,,,,,,,,,,,,**/#    
    #/***,,,***************,,****/#    
  (#/*(@/,,.,&@*********@@,..,/@@*/##  
  (#/*(@#//*/#%@*******@%%/**/#@@*/##  
  (#**(@&&&&&&&&@%****@&&&&&&&&@@**##  
  (#/*(@&%%%%%%&@%****@&%%%%%%&@@*/##  
    (***&%%####%@#****@%####%%&***(    
     ((****@@@@*********@@@@#****(     
      .(***********************((      
         ((*,,,&&&&&&&&&,,,*/(         
           (***,%%%%%%%,***(*          
               ((/*,**((               
                 ,(((#        
 ___  _  _            ___        __               __ __       _  _ 
| . || |<_> ___ ._ _ / __> ___  /. |  _ _ _ ._ _ |  \  \ ___ <_>| |
|   || || |/ ._>| ' |\__ \| . \/_  .|| | | || ' ||     |<_> || || |
|_|_||_||_|\___.|_|_|<___/|  _/  |_| |__/_/ |_|_||_|_|_|<___||_||_|
by: Max_Cano              |_|    
-------------------------------------------------------------------
                                
''')


def setUp():
	global mailAdress
	global password
	global number
	global filToSend
	global attach
	global target
	global body
	target = raw_input("Enter target : ")
	mailAdress = raw_input("Enter you email : ")
	password = raw_input("Enter your password : ")
	number = raw_input("Number of emails to spam : ")
	print '\n'
	print '[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
	print '\n   Target: ' + target
	print '[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
	print '\n   Email: ' + mailAdress
	print '   Password: ' + password 
	print '\n[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
	print '\n'
	ask = raw_input("The info abobe is correct? [y/n]: ")
	if ask == 'y':
		pass
	else:
		setUp()
	filToSend = raw_input("Name of the file with extention : ")
	attach = raw_input("File location : ")
	body = raw_input("Messege to send : ")

def mailGmail():
	try:
		msg = MIMEMultipart() 
		msg['From'] = ''.join(random.sample(randomAdress, 8))
		msg['To'] = target
		msg['Subject'] = ''.join(random.sample(subject, 10))

		msg.attach(MIMEText(body, 'plain'))

		filename = filToSend
		attachment = open(attach, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(mailAdress, password)
		text = msg.as_string()
		server.sendmail(randomAdress, target, text)
		server.quit()
	except:
		print "\n Error: Mail not send it!"

def mailHotmail():
	try:
		msg = MIMEMultipart() 
		msg['From'] = ''.join(random.sample(randomAdress, 8))
		msg['To'] = target
		msg['Subject'] = ''.join(random.sample(subject, 10))

		msg.attach(MIMEText(body, 'plain'))

		filename = filToSend
		attachment = open(attach, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

		server = smtplib.SMTP('smtp.live.com', 465)
		server.starttls()
		server.login(mailAdress, password)
		text = msg.as_string()
		server.sendmail(randomAdress, target, text)
		server.quit()
	except:
		print "\n Error: Mail not send it!"
		
def mailYahoo():
	try:
		msg = MIMEMultipart() 
		msg['From'] = ''.join(random.sample(randomAdress, 8))
		msg['To'] = target
		msg['Subject'] = ''.join(random.sample(subject, 10))

		msg.attach(MIMEText(body, 'plain'))

		filename = filToSend
		attachment = open(attach, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

		server = smtplib.SMTP('smtp.yahoo.com', 465)
		server.starttls()
		server.login(mailAdress, password)
		text = msg.as_string()
		server.sendmail(randomAdress, target, text)
		server.quit()
	except:
		print "\n Error: Mail not send it!"
def mailOutlook():
	try:
		msg = MIMEMultipart() 
		msg['From'] = ''.join(random.sample(randomAdress, 8))
		msg['To'] = target
		msg['Subject'] = ''.join(random.sample(subject, 10))

		msg.attach(MIMEText(body, 'plain'))

		filename = filToSend
		attachment = open(attach, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

		server = smtplib.SMTP('smtp.live.com', 587)
		server.starttls()
		server.login(mailAdress, password)
		text = msg.as_string()
		server.sendmail(randomAdress, target, text)
		server.quit()
	except:
		print "\n Error: Mail not send it!"

def choice():
	print 'Gmail [1]'
	print 'Hotmail [2]'
	print 'Yahoo [3]'
	print 'Outlook [4]'
	ask = raw_input("Whitch domain is your mail?")
	if ask == 1:
		print "\n Please wait, this will take a wile..."
		for i in range (int(number)):
			mailGmail()
	elif ask == 2:
		print "\n Please wait, this will take a wile..."
		for i in range (int(number)):
			mailHotmail()
	elif ask == 3:
		print "\n Please wait, this will take a wile..."
		for i in range (int(number)):
			mailYahoo()
	
	elif ask == 4:
		print "\n Please wait, this will take a wile..."
		for i in range (int(number)):
			mailOutlook()
	

def main():
	banner()
	setUp()
	choice()
	sendMails()
	print "\n Process finished!"

clear()
main()

#El que no culeo burra no tubo infancia
