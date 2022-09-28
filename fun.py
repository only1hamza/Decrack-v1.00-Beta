import requests

def string_to_crc(Sinta):
    #Convert String to ASCII
    m = str(Sinta)
    values1 = []
    for character in m:
        values1.append(ord(character))

   #Convert ASCII to Polynomial
    n = len(values1)
    r = 0
    multi = 0
    ans = 0
    for i in range(0,n):
        num = values1[i]
        multi = multi+1
        sum = num * multi
        if multi == 5 :
            multi = 0
        r = r + sum    
        ans = r
    return ans
    
def Writer(v1,v2,v3,v4,v5,v6,v7,v8,v9,s1,s2,s3,s4,s5,s6,s7,s8,s9,Path):
    f= open(f"{Path}\{v1}.S","w")
    f.write(f"[MESURES]\n200={v1}\n320={v2}\n410={v3}\n411={v4}\n412={v5}\n413={v6}\n414={v7}\n415={v8}\n416={v9}\n[CRC]\n200={s1}\n320={s2}\n410={s3}\n411={s4}\n412={s5}\n413={s6}\n414={s7}\n415={s8}\n416={s9}\n")
    f.close()
    

def checkInternetConnection(a):
        try:
            requests.get('https://www.google.com/')
            a["text"]="YES"
            a["foreground"]="green"
        except:
            a["text"]="Bad"
            a["foreground"]="red"
            print('[!] No internet connection...Please connect to the Internet')
        else:
            print('[+] Checking Internet connection...')
            print('[+] Connection Successful <3 <3 <3') 
            a["text"]="YES"
            a["foreground"]="green"




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    