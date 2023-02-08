from palk import *

palgad=[1200,1200,395,395,1200]
inimesed=["Egor","Boris","Egor","Denis","Luka"]
while True:
    menu=""
    print()
    while menu.isdigit()==False:
        menu=input("\n 1-Vaata nimed ja palgad\n 2-Lisa andmed\n 3-Kustutage inimene ja tema palk\n 4-Leia kõrgeim palk ja kes seda saab\n")
    menu=int(menu)
    if menu==1:
        print(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=limed(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==3:
        inimesed,palgad=kip(inimesed,palgad) 
        print(inimesed,palgad)
    elif menu==4:
        print(maks(inimesed,palgad))
    elif menu==5:
        print(mini(inimesed,palgad))
    else:
        break
