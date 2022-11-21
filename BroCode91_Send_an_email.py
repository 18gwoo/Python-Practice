#NOTE THIS DOES NOT WORK ANYMORE DUE TO A GOOGLE UPDATE
import smtplib #Simple mail proticol transfer library

sender = "garrettwoogs@gmail.com"
receiver = "garrettwoogs@yahoo.com"
password = "Teemo@123" #password to email account
subject = "Python email test"
body = "I wrote an email! :D"

# header: Triple quote string can span multiple lines of text
message = f"""From: Snoop Dogg{sender} 
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587) #creates a server object ("smtp.gmail.com", port number(587 is default))
server.starttls() #Tranport laired security

try:
    server.login(sender,password) #Logins to email
    print("Logged in...")
    server.sendmail(sender, receiver, message) #Sends the mail
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError: #Error for gmail if password is incorrect or if gmail security is up
    print("unable to sign in")