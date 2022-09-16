try:import secrets,re;from colorama import Fore;from requests import get;from time import sleep
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()

class Fake_Email:
    def __init__(self):pass
    def Receive_email(self,s):
        vv1ck='JQ';count=0
        print('--------------------------------------------------------------------------------')
        while vv1ck=='JQ':
            sleep(5)
            try:
                rq2=get(f'https://10minutemail.net/address.api.php?sessionid={s}')
                msg=str(rq2.json()['mail_list'][0]['subject'])
                if msg.find('Hi, Welcome to 10 Minute Mail')>=0:
                    print(rq2.text)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] No Message Yet >> {count}');count+=1
                elif '"from"' in rq2.text:
                    Time=re.findall('"datetime2":"(.*?),',rq2.text)[0]
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] From : ',rq2.json()['mail_list'][0]['from'])
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Date : ',rq2.json()['mail_list'][0]['datetime'])
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Message : ',msg)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] This Message From : "{Time}')
                    print('--------------------------------------------------------------------------------')
                else:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Email Expired ..');exit()
                    #print('Note : Prees Enter to Get New Email')
                    #input(' ')
                    #rq_more=get('https://10minutemail.net/more.html',headers={'Host': '10minutemail.net','Cookie': f'PHPSESSID={s}; lang=en','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://10minutemail.net/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers'})
                    #if  'Your e-mail address will expire in' in rq_more.text:Fake_Email.Receive_email(s)
            except Exception as i:print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error ...');exit()
    def crate_Email(slef):
        sleep(1);s=secrets.token_hex(8)*2
        try:
            rq=get('https://10minutemail.net/new.html',headers={'Host': '10minutemail.net','Cookie': f'PHPSESSID={s}; lang=en','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://10minutemail.net/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers'})
            em0=re.findall('<div id="d_clip_button"><button id="copy-button" data-clipboard-text="(.*?)" class="button button-3d button-primary button-rounded button-height-auto"><i id="copy-icon" class="fa fa-copy fa-fw fa-lg m-r-8"></i>Copy to clipboard</button></div>',rq.text)[0]
            rq2=get(f'https://10minutemail.net/address.api.php?sessionid={s}')
            em=str(rq2.json()['mail_get_mail'])
        except:print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTRED_EX}You got Ban wait 10 minute ..');sleep(15);Fake_Email().crate_Email()
        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Email : ',em)
        Fake_Email().Receive_email(s)
print("""
  ███████╗ █████╗ ██╗  ██╗███████╗  ███████╗███╗   ███╗ █████╗ ██╗██╗     
  ██╔════╝██╔══██╗██║ ██╔╝██╔════╝  ██╔════╝████╗ ████║██╔══██╗██║██║     
  █████╗  ███████║█████╔╝ █████╗    █████╗  ██╔████╔██║███████║██║██║     
  ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
  ██║     ██║  ██║██║  ██╗███████╗  ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    
                                                                                                             
                          By @TweakPY - @vv1ck""")

Fake_Email().crate_Email()
