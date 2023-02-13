from palk import *

palgad=[1200,1200,395,395,200,700]
inimesed=["Egor","Boris","Egor","Denis","Luka","Andrei"]
while True:
    menu=""
    print()
    while menu.isdigit()==False:
        menu=input("""
 0-Stop programm\n 1-Vaata nimed ja palgad\n 2-Lisa andmed\n 3-Kustutage inimene ja tema palk\n 4-Leia kõrgeim palk ja kes seda saab
 5-Leia väiksem palk ja kes seda saab\n 6-Leia kes on saama palk\n 7-Leia palk nimi abiga\n 8-Leia kes saab palk suurem, väiksem või täpselt kui palk
 9-Leia top 3 inimesed kes saab väike palk ja suur palk\n 10-Otsi keskmine palk ja kes on saada suurem\n 11-Otsi maksuvaba palk
 12-Sorteerimine\n 13-Otsige üles, kes teenivad alla keskmise palga, ja eemaldage nad\n 14-Tee ilus nimekiri
 15-Uuri välja inimeste palk N aasta pärast\n 16-Nimetage ümber iga 3 inimese järel \n
""")
    menu=int(menu)
    if menu==0:
        break
    elif menu==1:
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
    elif menu==6:
        saapa(inimesed,palgad)
    elif menu==7:
        lepani(inimesed,palgad)
    elif menu==8:
        suva(inimesed,palgad)
    elif menu==9:
        tomami(inimesed,palgad)
    elif menu==10:
        keskmine(inimesed,palgad)
    elif menu==11:
        tulumaks(inimesed,palgad)
    elif menu==12:
        inimesed,palgad=sorteerimine(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=keskpop(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==14:
        inimesed,palgad=tint(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==15:
        pogod(inimesed,palgad)
    elif menu==16:
        inimesed=petew(inimesed)
        print(inimesed,palgad)
    else:
        print("Kirjuta õige arv")
