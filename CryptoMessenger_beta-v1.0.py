print ("")
import os
#os.system('color 0c ')
#os.system('mode con cols=76 lines=50')
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("                C R Y P T O   M E S S E N G E R    beta v-1.0                  ")
print ("")
print ("                         Developed by Khizar Khan                                            ")
print ("")
print ("")
print ("")
print ("")
print ("Welcome to Crypto Messenger. This program makes communication")
print ("more secure than ever.")
print ("")
print ("To start, press ENTER. To see instructions, type HELP.")
print ("To exit the program, type EXIT")
print ("")
iniresp = raw_input()       
if iniresp == "HELP":
    print ("")
    print ("")
    print ("After starting the program, you will be greeted with the welcome screen. Now you will have to sign into the account provided to you by Crypto Technician. After entering the credentials, you will be logged into the Crypto Server. Now you will be presented with 2 options,'Send Message' and 'Receive Message'. By selecting 'Send Message', you will have to enter the Crypto ID of the user you want to send the message to. Then you can type the rest of your message. If you want to receive a text from another Crypto user, select the 'Receive Message' option. After selecting it, you will see the latest message at the bottom of the screen. You will have to enter the numbers in the mail into another field, which will then decode the numbers, and show you the final message.")
    z = input("Press ENTER to start, or type EXIT to exit.")
    if z == "":
        print("")
        print("")
        print("")
        userid = raw_input("                      User ID:  ")
        print("")
        pswrd = raw_input("                      Password:  ")
        print("")
        print("")
        abc = 0
        while abc != 1:
            print("              Send Message          or          Receive Message     ")
            print("")
            startresp = raw_input()
            if startresp == "Send":
                import smtplib
                print ("")
                print ("")
                print ("")
                print ("")
                print ("")
                TO = raw_input("To: ")
                print ("")
                SUBJECT = raw_input("Subject: ")
                print ("")
                print ("")
                TEXT = raw_input("Type the text you want to send: ")

                gmail_sender = userid
                gmail_password = pswrd

                server = smtplib.SMTP('smtp.gmail.com' , 587)
                server.ehlo()
                server.starttls()
                server.ehlo
                server.login(gmail_sender , gmail_password)

                encryptionlist = []

                import random
                extractorfactor = random.randrange(13,79)
                for j in range(len(TEXT)):
                    encryptionlist.append(ord(TEXT[j])+extractorfactor)
                strlist = ""
                for i in range(len(encryptionlist)):
                    strlist = str(strlist)  + "," + str(encryptionlist[i])  
                finalmsg = (strlist , "Total neutrino's: " , len(encryptionlist) , "Extractor Factor: " , extractorfactor)
                #print (finalmsg , strlist)

                BODY = '\r\n'.join([
                             'To: %s' % gmail_sender ,
                             'Subject: %s' % SUBJECT ,
                             ' ' ,
                             strlist , 'Total Neutrinos: ' , str(len(encryptionlist)) , 'Extractor Factor: ' , str(extractorfactor)
                             ])

                try:
                    server.sendmail(gmail_sender , [TO] , BODY)
                    print ("Email sent successfully")
                    print ("")
                except:
                    print ("Error sending email")
                    print ("")

                #if (input("Press Enter to exit"))=="":
                 #   quit()
            elif startresp == "Receive":
                print("")
                print("")
                print("")
                import poplib
                mailServer = 'pop.gmail.com'
                #emailID = input(" User ID: ")
                #emailPass = input(" Password: ")

                
                myEmailConnection = poplib.POP3_SSL(mailServer)
                
                #print (myEmailConnection.getwelcome())
                
                myEmailConnection.user(userid)
                
                myEmailConnection.pass_(pswrd)
                
                EmailInformation = myEmailConnection.stat()
                 
                numberofmails = EmailInformation[0]
                print ("Number of mails: " , numberofmails)
                for i in range(numberofmails):
                    for email in myEmailConnection.retr(i+1)[1]:
                        print (email)
                decryptionlist=[]
                decryptedlist=[]
                decodestr=""
                print("")
                print("")
                print("")
                extractorID = int(raw_input("Extractor Factor ?: "))
                print("")
                print("")    
                for k in range(int(raw_input("Total neutrino's ?: "))):
                    decryptionlist.append(int(raw_input("Enter neutrino's one by one: ")))
                for i in range(len(decryptionlist)):
                    x=chr(decryptionlist[i]-int(extractorID))
                    decryptedlist.append(x)
                print("")
                print("")
                for b in range(len(decryptionlist)):
                    decodestr = str(decodestr) + str(decryptedlist[b])
                print("Message:  " , decodestr)
    elif z == "EXIT":
        quit()
elif iniresp == "EXIT":
    quit()
elif iniresp == "":
    print("")
    print("")
    print("")
    userid = raw_input("                     User ID:  ")
    print("")
    pswrd = raw_input("                     Password:  ")
    print("")
    print("")
    xyz = 1
    while xyz != 0:     
        print("              Send Message          or          Receive Message     ")
        print("")
        startresp = raw_input()
        if startresp == "Send":
            import smtplib
            print ("")
            print ("")
            print ("")
            print ("")
            print ("")
            TO = raw_input("To: ")
            print ("")
            SUBJECT = raw_input("Subject: ")
            print ("")
            print ("")
            TEXT = raw_input("Type the text you want to send: ")

            gmail_sender = userid
            gmail_password = pswrd

            server = smtplib.SMTP('smtp.gmail.com' , 587)
            server.ehlo()
            server.starttls()
            server.ehlo
            server.login(gmail_sender , gmail_password)

            encryptionlist = []

            import random
            extractorfactor = random.randrange(13,79)
            for j in range(len(TEXT)):
                encryptionlist.append(ord(TEXT[j])+extractorfactor)
            strlist = ""
            for i in range(len(encryptionlist)):
                strlist = str(strlist)  + "," + str(encryptionlist[i])  
            finalmsg = (strlist , "Total neutrino's: " , len(encryptionlist) , "Extractor Factor: " , extractorfactor)
            #print (finalmsg , strlist)

            BODY = '\r\n'.join([
                         'To: %s' % gmail_sender ,
                         'Subject: %s' % SUBJECT ,
                         ' ' ,
                         strlist , 'Total Neutrinos: ' , str(len(encryptionlist)) , 'Extractor Factor: ' , str(extractorfactor)
                         ])

            try:
                server.sendmail(gmail_sender , [TO] , BODY)
                print ("Email sent successfully")
                print ("")
            except:
                print ("Error sending email")
                print ("")

            #if (input("Press Enter to exit"))=="":
             #   quit()
        elif startresp == "Receive":
            print("")
            print("")
            print("")
            import poplib
            mailServer = 'pop.gmail.com'
            #emailID = input(" User ID: ")
            #emailPass = input(" Password: ")

            
            myEmailConnection = poplib.POP3_SSL(mailServer)
            
            #print (myEmailConnection.getwelcome())
            
            myEmailConnection.user(userid)
            
            myEmailConnection.pass_(pswrd)
            
            EmailInformation = myEmailConnection.stat()
             
            numberofmails = EmailInformation[0]
            print ("Number of mails: " , numberofmails)
            for i in range(numberofmails):
                for email in myEmailConnection.retr(i+1)[1]:
                    print (email)
            decryptionlist=[]
            decryptedlist=[]
            decodestr=""
            print("")
            print("")
            print("")
            extractorID = int(raw_input("Extractor Factor ?: "))
            print("")
            print("")    
            for k in range(int(raw_input("Total neutrino's ?: "))):
                decryptionlist.append(int(raw_input("Enter neutrino's one by one: ")))
            for i in range(len(decryptionlist)):
                x=chr(decryptionlist[i]-int(extractorID))
                decryptedlist.append(x)
            print("")
            print("")
            for b in range(len(decryptionlist)):
                decodestr = str(decodestr) + str(decryptedlist[b])
            print("Message:  " , decodestr)
       # if (input("Press ENTER to exit"))=="":
        #    quit()
        #else:
         #   print("Pagal samjha hoa hai kya")
            
