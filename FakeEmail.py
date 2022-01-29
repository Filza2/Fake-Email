from requests import get;from time import sleep
def Banner():
    print("""
  ███████╗ █████╗ ██╗  ██╗███████╗  ███████╗███╗   ███╗ █████╗ ██╗██╗     
  ██╔════╝██╔══██╗██║ ██╔╝██╔════╝  ██╔════╝████╗ ████║██╔══██╗██║██║     
  █████╗  ███████║█████╔╝ █████╗    █████╗  ██╔████╔██║███████║██║██║     
  ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
  ██║     ██║  ██║██║  ██╗███████╗  ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    
                                                                                                             
                          By @TweakPY @vv1ck""")
def OneMessage():
    Try=0
    try:
        get_email=get(f"https://khafeer.ml/api/mail/fake-gmail.php?a=new").json();mail=get_email['mail'];print(f"Success, Your Mail Is : {mail}")
        if get_email['mail'] == "Too Many Requests":return OneMessage()
        while True:
            sleep(0.5)
            if get(f"https://khafeer.ml/api/mail/fake-gmail.php?a=list&mail={mail}").text=="":print(f"No Message Yet =>> [{Try}]");Try+=1
            else:
                Email_List=get(f'https://khafeer.ml/api/mail/fake-gmail.php?a=list&mail={mail}').json()
                sender=Email_List['result'][0]['sender']
                subject=Email_List['result'][0]['subject']
                send_time=Email_List['result'][0]['send_time']
                print(f"""----------------\nSender :{sender}\nSubject :{subject}\nSend Time :{send_time}\n----------------""")
                exit(2551)
    except:exit(507)
def OneANDSwitch():
    Try=0
    try:
        get_email=get(f"https://khafeer.ml/api/mail/fake-gmail.php?a=new").json();mail=get_email['mail'];print(f"Success, Your Mail Is : {mail}")
        if get_email['mail']=="Too Many Requests":return OneANDSwitch()
        while True:
            sleep(0.6)
            if get(f"https://khafeer.ml/api/mail/fake-gmail.php?a=list&mail={mail}").text=="":print(f"No Message Yet =>> [{Try}]");Try+=1
            else:
                Email_List=get(f'https://khafeer.ml/api/mail/fake-gmail.php?a=list&mail={mail}').json()
                sender=Email_List['result'][0]['sender']
                subject=Email_List['result'][0]['subject']
                send_time=Email_List['result'][0]['send_time']
                print(f"""----------------\nSender :{sender}\nSubject :{subject}\nSend Time :{send_time}\n----------------""")
                return OneANDSwitch()
    except:exit(507)
def Main_Start():
    Banner()
    Message_sys=int(input("""
1- Get One Message And close
2- Get One Message And switch Email
--{ """))
    if Message_sys==1:OneMessage()
    elif Message_sys==2:OneANDSwitch()
    else:Banner()
Main_Start()