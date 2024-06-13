import requests

MAILGUN_API_ENDPOINT = "https://api.mailgun.net/v3/sandboxc390e2ff9185420f965d2ca1bb096766.mailgun.org/messages"
MAILGUN_API_KEY = ""


def send_simple_email(to, subject, body):
	

    # creating a dictionary of the email data
	data = {
		"from": "mailgun@mailgun@sandboxc390e2ff9185420f965d2ca1bb096766.mailgun.org",
        "to": to,
		"subject": subject,
		"text": body
    }

    # data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
	# 		"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
	# 		"subject": "Hello",
	# 		"text": "Testing some Mailgun awesomeness!"}


    # sending a post request to the mailgun api endpoint
	response = requests.post(
		MAILGUN_API_ENDPOINT,
		auth = ("api", MAILGUN_API_KEY),
		data = data
    )
	
    # checking if the request was successful
	if response.status_code == 200:
		print("Email sent successfully")
	else:
		print("An error occurred while sending the email")

# example
to = "wmittesh@gmail.com"
subject = "Test email"
body = "Hello, Mittesh. How are you doing?"
send_simple_email(to, subject, body)

