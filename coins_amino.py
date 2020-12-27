#!/usr/bin/python3
#script by kira_xc
#youtube : youtube.com/kiraxc
#insta : kira_xc
#github : kira-xc
from os import _exit
try:
    import amino
except:
    print("connect to network")
    _exit(1)
cpt=0
blog=input("your url blog : ")
infoo=amino.Client().get_from_code(blog)
blogId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]
print ("blogId = ",blogId)
print("comId = ",comId)
surr=False
while surr==False:
    password=input("your intial password :")
    ssssa=input("are you sure ? y/n :")
    if ssssa=="y":
        surr=True
client=amino.Client()
try:
    emails=open("email.txt")
except:
    print("\n\n\n\"email.txt\" not found\nplease create email lost in file email.txt ")
    _exit(1)
for line in emails:
    kk=False
    try:
      client.login(email=str(line).strip(),password=password)
    except:
      kk=True
      print(str(line).strip()+" cant login")
    try:
        subc=amino.SubClient(comId=comId,profile=client.profile)
    except:
        try:
            can=client.join_community(comId=comId)
        except:
            can=0
            print(str(line).strip()+" cant enter in community !!")
        if can ==200:
            subc=amino.SubClient(comId=comId,profile=client.profile)
        else:
            kk=True
    if kk==False:
        cpt=cpt+1
        print(str(cpt)+") this email : ",str(line).strip()," login ")
        try:
         subc.check_in()
        except:
          pass
        try:
         subc.lottery()
        except:
          print("cant lottery now")
        coins=int(client.get_wallet_info().totalCoins)
        print("my total coins : "+str(coins))
        while coins>500:
            subc.send_coins(coins=500,blogId=blogId)
            coins=coins-500
        if coins!=0:
            subc.send_coins(coins=coins,blogId=blogId)
    
_exit(1)
