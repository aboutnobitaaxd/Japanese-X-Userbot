@@ -0,0 +1,33 @@
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""Welcome To Japanese X Userbot String Generator By @Nobitaa_xd""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n {session} \n\n And Visit @teamishere For Any Help !"
   )

   print(
       "Thanks for Choosing Japanese Userbot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
   )
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +919876543210 ! Kindly Retry"
  )
  print("")
  continue
 break
