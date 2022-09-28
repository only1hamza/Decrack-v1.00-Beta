from bs4 import BeautifulSoup
import requests


def Click():
    r2=requests.get(entsrv.get())
    soup = BeautifulSoup(r2.text, 'html.parser')
    b = soup.find('p').get_text()
    s = list(b.split("\n"))
    f = entlog.get() in s
    print(f)
    if f == True :
        i = s.index(entlog.get())
        id_login = s[i-1]
        user_login = s[i]
        key_login = s[i+1]
        date_login = s[i+2]
        activation_login = s[i+3]
        print(s)
        log1 = entlog.get()
        key1 = entkey.get()
        
        r1=requests.get('https://www.calendardate.com/todays.html')
        soup = BeautifulSoup(r1.text, 'html.parser')
        a = soup.find_all(id='tprg')[6].get_text()
        a = a.replace('-','')
        
        a = a.replace(' ','')
        if log1 == user_login and key1 == key_login :
            if date_login >= a :
                lblinf["text"]="Connection Succesfuly .. Please Wait"
                if activation_login == "YES":
                    lblinf["text"]="Your User is Activated .. Please Wait"
                    #time.sleep(2)
                    lblinf["text"]=f"Your ID {id_login} is working till {date_login[0:4]}-{date_login[4:6]}-{date_login[6:8]}"
                else: 
                    lblinf["text"]="Your User is Disactivated"
            else :
                lblinf["text"]="Your User is Expered"
        else :
            lblinf["text"]="Login is Faild, Try Again"
    else :
        lblinf["text"]="Login is Faild, Try Again"
    print(log1, key1)
    