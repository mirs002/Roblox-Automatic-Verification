
# Roblox Automatic Verification
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/567688006341885953/1054375086750191626/WindowsTerminal_lOtkHWM8ft.gif" />
</p>

Automatically verifies upon receiving verification email. Used to verify multiple accounts at once automatically.

This was tested in Windows but should work with other operating systems.

## Installation Guide (Windows)

1. Install [Python 3.X](https://www.python.org/downloads/) & [Google Chrome](https://www.google.com/chrome/)
2. Open command prompt in the downloaded directory ``cd C:\location\to\file``
3. Install the requirements.txt file by using ```pip -r requirements.txt```
4. Head over to [Gmail Preparation Guide](https://github.com/mirs002/Roblox-Automatic-Verification#gmail-preparation-guide) to Continue with the Guide.
## Gmail Preparation Guide

This is a mandatory requirement in-order to ensure that the program can access your gmail and it's contents.

1. Head over to [Gmail](https://mail.google.com) and then Click See All Settings
![Click the Gear Icon then See All Settings](https://cdn.discordapp.com/attachments/567688006341885953/1054017230255431781/firefox_byX6VXcR6A.png)
2. Click Forwarding and POP/IMAP and enable IMAP then click save changes.
![Forwarding and POP/IMAP](https://cdn.discordapp.com/attachments/567688006341885953/1054017631201525915/firefox_Iuxz0AfqE3.png)
3. For this step you will need to have **2 Step Authentication turned ON**.
then [Go to Manage Your Google Account](https://myaccount.google.com/)

4. Click [Security](https://myaccount.google.com/security) then Scroll Down to "Signing in to Google" and Click App passwords.
![Signing in to Google](https://cdn.discordapp.com/attachments/567688006341885953/1054026989847183431/firefox_rWeyzGOpRC.png)
5. Generate Your password
![Generate Password](https://cdn.discordapp.com/attachments/567688006341885953/1054028635176189972/firefox_jzWTkYTUW9.png)
### Back to Program
6. Copy the Password and Keep it **SAFE** This is needed for signing in to your gmail account via the python program.
7. Head Over to your directory and run ``py main.py`` with your Program
8. Type ``new`` and Input your **gmail address** and **app specific password**
9. The Program should be running as intended if all of the above steps are correct.

**That's all!**

## Additional Steps
1. You can create your own encryption key using ``generateKey.py`` and assign it in ``main.py`` line 13
(I am aware this is not the most secure way to store credentials, but i tried to make it as simple as possible.)


## To-Do Features
- [x]  Add the ability to add your own key for encryption
- [x]  Improved Output and Stylization
- [x]  Sped up the Process of Verification (Details about it in Release Log)
- [ ]  Add Multi-Threaded Support
- [ ]  Implement a GUI


