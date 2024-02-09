import random
chat =  True
greetingIntent = ["hy","hello","hlo","hi there","hey"]
while chat:
    msg = input("Enter the message..")
    msg = msg.lower()
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg == "bye":
        print("bye user..")
        break
    else:
        print("I don't understand..")
