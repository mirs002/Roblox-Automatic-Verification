import imaplib
import email
import threading
import time
import json
import os


from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pystyle import Write, Colors, Colorate

# Clear cmd so it doesn't look crowded
os.system('cls' if os.name == 'nt' else 'clear')

# Assign cryptography key
key = 'Jq00OK3wOGIgSD1CslnZ6DAR6B20ZaMfBM7ACylBYOk='
# You can create a new one using generateKey.py
# You will have to re-enter the email and password when you switch to a different cryptography key
fernet = Fernet(key)


# Ask if the user wants to use last gmail account or a new gmail account
oldnewChoice = Write.Input("Would you like to use saved credentials or use a new one? (old/new)-> ", Colors.white, interval=0.0025)
if oldnewChoice == 'old':
    pass
elif oldnewChoice == 'new':
    # Encrypt the credentials
    inpGmail = Write.Input("Input the gmail: ", Colors.white, interval=0.0025)
    newGmail = fernet.encrypt(inpGmail.encode()).decode()
    inpPassword = Write.Input("Input the password: ", Colors.white, interval=0.0025)
    newPassword = fernet.encrypt(inpPassword.encode()).decode()
    credentials = {'email':newGmail,
                   'password':newPassword}
    # Save the credentials in a json file
    with open("credentials.json", "w") as json_file:
        json.dump(credentials, json_file)


# Connect to the imap server
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Decrypt the credentials
try:
    with open("credentials.json", "r") as json_file:
        jsonData = json.loads(json_file.read())
        encGmail = jsonData['email']
        encPassword = jsonData['password']
        gmail = fernet.decrypt(encGmail.encode()).decode()
        password = fernet.decrypt(encPassword.encode()).decode()
except FileNotFoundError as i:
    Write.Print("\nCan not find credentials.json, you should choose (new) if you want to create one", Colors.red, interval=0.0025)
    input("")
    exit()
except json.decoder.JSONDecodeError:
    Write.Print("\ncredentials.json is either empty or missing information, you should choose (new) if you want to reassign credentials", Colors.red, interval=0.0025)
    input("")
    exit()




# Login to your account
try:
 mail.login(gmail, password)
except:
    Write.Print("\nInvalid credentials.", Colors.red, interval=0.0025)
    input("")
    exit()



def main():
    # Start a selenium webdriver
    opt = Options()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument('--disable-notifications')
    opt.add_argument("--headless")  # You can remove this line if you want to see the chrome instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)



    while True:
        Write.Print("\nStarted listening for emails.\n", Colors.yellow, interval=0.0025)
        # Check for emails from "Roblox" with the word "Verification" in the subject
        while True:
            try:
                mail.select("inbox")
            except:
                Write.Print("\nLost connection to imap.gmail.com", Colors.red, interval=0.0025)
                input("")
                exit()
            status, msgnums = mail.search(None, '(FROM "Roblox")', '(SUBJECT "Verification")', '(UNSEEN)')

            if msgnums == [b'']:
                pass
            else:
                global username
                for msgnum in msgnums[0].split():
                    # Getch the email message by ID
                    status, data = mail.fetch(msgnum, '(RFC822)')

                    # Get the subject from the email
                    subject = (data[0][1].decode()).split('Subject: ')[1].split('\r\n')[0]
                    username = subject.partition(": ")[2]
                    Write.Print(f"Received Email for: {username}.\n", Colors.blue, interval=0.0025)
                    break
                break


        # Get the emails from the imap server
        for msgnum in msgnums[0].split():

            status, data = mail.fetch(msgnum, "(RFC822)")
            message = email.message_from_bytes(data[0][1])
            # Mark email as seen
            mail.store(msgnum, '+FLAGS', '(SEEN)')


            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    rawText = part.as_string()

                    # Seperate the link from the raw email contents
                    link2 = rawText[rawText.find("( ")+1:rawText.find(" )")]

                    # Remove spaces and newline operators from the link
                    link2 = link2.replace('\n', '')
                    link2 = link2.replace(' ','')

                    # Seperate the link into 2 parts (Because we have to remove some unwanted characters from the link, otherwise it does not work)
                    link2 = link2.replace('https://www.roblox.com/account/settings/verify-email?ticket=', '')
                    link2 = link2.replace('=3D', '')
                    link2 = link2.replace('=', '')

                    # Connect the 2 parts back together
                    link1 = 'https://www.roblox.com/account/settings/verify-email?ticket='
                    link1 += link2
                    link = link1


                    # Open the link on selenium chrome instance
                    driver.get(link)
                    Write.Print(f'Verified: {username}\n', Colors.green, interval=0.0025)


            break


if __name__ == '__main__':
    main()
