import smtplib

def send_emails(emails, schedule, forecast):
	# Connect to the smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')

	# Start TLS encryption
	server.starttls()

	# Login
	password = input('What is your password?')
	from_email = 'shivam19j@gmail.com'
	server.login(from_email, password)

	# Send to entire email list
	for to_email, name in emails.items():
		message = 'Subject: App Testing\n'
		message += 'Hi' + name + ':\n\n'
		message += forecast + '\n\n'
		message += schedule + '\n\n'
		message += 'Hope to see you!'
		server.sendmail(from_email, to_email, message)
	server.quit()