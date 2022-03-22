import pandas as pd
import datetime
import smtplib
import pywhatkit

GMAIL_ID = 'gmailid'
GMAIL_PASS = 'pass'

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg} ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASS)
    s.sendmail(GMAIL_ID, to ,f"Subject: {sub}\n\n{msg}")
    s.quit()

def sendwhatsappmessage():
    pywhatkit.sendwhatmsg("number", "message", {"time"})

def main_index():
    # sendEmail(GMAIL_ID, "subject","test message")
    df = pd.read_excel("Birthdaylist.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearnow = datetime.datetime.now().strftime("%y")
    # print(today)
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item["Birthday"])
        bday = item["Birthday"].strftime("%d-%m")
        # print(bday)
        if (today==bday) and yearnow not in str(item["Year"]):
            sendEmail(item["Email"],"Happy Birthday "+item["Name"], item["Dialogue"])
            # print("Yes")
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, "Year"]
        # print(yr)    
        df.loc[i, "Year"] = str(yr) + ', 20' + str(yearnow)
        # print(df.loc[i, "Year"])    
    # print(df)
    df.to_excel("Birthdaylist.xlsx", index=False)

main_index()    