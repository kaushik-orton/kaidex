from urllib.request import urlopen
import json
import time
import telegram_send

url="https://api.info.kaidex.io/api/tokens"
d={}

#ncnbskjmnxjks

while True:
 
 #telegram_send.send(messages=['1'])
 a=json.load(urlopen(url))
 b=a['data']
 c={}
 

#get only pairs and prices in c
 for x in b.keys():
    if x =='0xAF984E23EAA3E7967F3C5E007fbe397D8566D23d':
        
        sy=b[x]['symbol']
        pr=float(b[x]['price'])
        
        c[sy]=pr
    if x!='0xAF984E23EAA3E7967F3C5E007fbe397D8566D23d' and x!='0x92364Ec610eFa050D296f1EEB131f2139FB8810e':
     b[x].pop('name')
     b[x].pop('price')
     sym=b[x]['symbol']
     price=float(b[x]["price_KAI"])
     c[sym]=price
 
#set old with present array values during start
 
 if len(d.keys())==0:
     
     d=c
      #finding per change
      #for each token 
 
 for x in c:
         #check token present price qual to past price,if not
         
         if c[x]!=d[x]:
             diff=c[x]-d[x]
             per=diff*100/d[x]
             #print(per)
             if diff>0 and per>3:
                 telegram_send.send(messages=['{} up {}% in 2 mins\ncmp = {}$'.format(x,round(per,2),round(c[x],4)) if x=='WKAI' else '{} up {}%\ncmp = {} KAI'.format(x,round(per,2),round(c[x],4))
        
                 ])
                 
             elif diff<0 and per<(-3):
                 telegram_send.send(messages=['''{} down {}% in 2 mins\ncmp = {} KAI
                 
                 '''.format(x,round(per,2),round(c[x],4))])


         else:
             #telegram_send.send(messages=['no change'])
             pass
             
 d=c
 
 time.sleep(120)
 
