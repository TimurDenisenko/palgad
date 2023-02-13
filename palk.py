def limed(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:list,list
    """
    n=input("Kui palju inimesed sa tahad lisa? ")
    while n.isdigit()==False:
        n=input("Kirjuta õige arv! ")
    for i in range(int(n)):
        nimi=input("Mis nimi on uue inimene? ")
        while nimi.isdigit() or len(nimi)<2:
            nimi=input("Kirjuta õige nimi ")

        palk=input("Kui palju teda maksab? ")
        while palk.replace(".","",1).isdigit()==False or palk==0:
            palk=input("Kirjuta õige palk! ")
        if palk.isdigit():
            palk=int(palk)
        else:
            palk=float(palk)

        x.append(nimi)
        y.append(palk)
    return x,y 

def kip(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:list,list
    """
    kopia=x.copy()
    print(x,y)
    nimi=input("Kirjuta nimi mis tahad kustuda ")
    while nimi.isdigit() or len(nimi)<2 or nimi not in x:
        nimi=input("Kirjuta õige nimi! ")
    j=x.count(nimi)
    if j!=1:
        print("Siin on mõned inimesed sama nimega")
        valik=input("Kas sa tahad kustuda mõned inimesed? (jah või ei) ").lower()
        while valik not in ["jah","ei"]:
            valik=input("Kirjuta ainult jah või ei ").lower() 
        if valik=="jah":
            j=input("Kui palju inimesed sama nimega sa tahad kustuda? ")
            while j.isdigit()==False or int(j)>=int(j)+1 or int(j)==1:
                j=input("Kirjuta õige arv! ")
            j=int(j)
            for _ in range(j):
                valik=input(f"Siin on {j} nimed, mis nimed sa tahad kustuda? ")
                while valik.isdigit()==False or int(valik)>=j+1:
                    valik=input("Kirjuta õige arv! ")
                    kopia=x.copy()
                for i in range(int(valik)):
                    if i!=(int(valik)-1):
                        k=kopia.index(nimi)
                        kopia.pop(k)
                        kopia.insert(k,"")
                    else:
                        ind=kopia.index(nimi)
                        x.pop(ind)
                        x.insert(ind,"")
                        y.pop(ind)
                        y.insert(ind,"")
            j=0
            o=x.count("")
            for e in range(o):
                x.remove("")
                y.remove("")
        else:
            tegevus=input(f"Siin on {j} nimed, mis nimi sa tahad kustuda? ")
            while tegevus.isdigit()==False or int(tegevus)>=j+1:
                tegevus=input("Kirjuta õige arv! ") 
            for _ in range(int(tegevus)-1):
                k=kopia.index(nimi)
                kopia.pop(k)
                kopia.insert(k,"")
            j=1
    for i in range(j):
        ind=kopia.index(nimi)
        x.pop(ind)
        y.pop(ind)
    return x,y

def maks(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    im=[] 
    pm=[]
    ind=y.index(max(y))
    n=y.count(y[ind])
    if n!=1:
        print("Siin on mõned inimesed kes saab maksimaalne palk")
        kopia=y.copy()
        print("Saavad saama palk: ", end="")
        for i in range(n):
            print(f"{x[ind]}, ", end="") 
            kopia.pop(ind) 
            kopia.insert(ind,0)
            ind=kopia.index(max(kopia))
        vas=(f"ja nad saavad {max(y)}")
    else:
        vas=(f"Saab kõrgeimat palka {x[ind]} ja ta saab {y[ind]}")
    return vas

def mini(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    im=[] 
    pm=[]
    ind=y.index(min(y))
    n=y.count(y[ind])
    if n>1:
        print("Siin on mõned inimesed kes saab minimaalne palk")
        kopia=y.copy()
        print("Saavad saama palk: ", end="")
        for i in range(n):
            print(f"{x[ind]}, ", end="") 
            kopia.pop(ind) 
            kopia.insert(ind,(min(y)+1))
            ind=kopia.index(min(kopia))
        vas=(f"ja nad saavad {min(y)}")
    else:
        vas=(f"Saab minimaalne palka {x[ind]} ja ta saab {y[ind]}")
    return vas

def saapa(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    a=0
    for u in range(len(y)):
        for i in range(u+1,len(y)):
            if y[u]==y[i]:
                ind=y.index(y[i])
                print(f"{x[u]} ja {x[i]} saavad saama palk, see on {y[u]} euro.")
                z=1
    if z==0:
        print(f"Sul ei ole inimesed kes saavad saama palk.")

def lepani(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    """
    nimi=input("Kelle palk tahad leia? ")
    while nimi not in x:
        nimi=input("Palun kirjuta õige nimi ")
    n=x.count(nimi)
    if n!=1:
        print(f"Siin on mõned inimesed kes nimi on {nimi}") 
        kopia=x.copy()
        for i in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{i+1} {nimi} saab {y[ind]}")
    else:
        ind=x.index(nimi)
        print(f"{nimi} saab {y[ind]}")

def suva(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    palk=input("Kirjuta igasugune palk ")
    while palk.replace(".","",1).isdigit()==False: 
        palk=input("Kirjuta õige palk ")
    palk=float(palk)
    for i in range(len(x)):
        if y[i]>palk: 
            print(f"{x[i]} saab suurem kui {palk}, ta saab {y[i]}")
        elif y[i]<palk: 
            print(f"{x[i]} saab väiksem kui {palk}, ta saab {y[i]}")
        else:
            print(f"{x[i]} saab täpselt {palk}")

def tomami(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    """
    kopia=y.copy()
    for i in range(3):
        ind=kopia.index(min(kopia))
        print(f"{i+1} inimene - {x[ind]} saab väikse palk: {y[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(y)+1)
    kopia=y.copy()
    for i in range(3):
        ind=kopia.index(max(kopia))
        print(f"{i+1} inimene - {x[ind]} saab suur palk: {y[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(y)+1)

def keskmine(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    """
    kesk=sum(y)/len(y)
    print(f"Keskmine palk on {kesk}")
    for i in range(len(x)):
        if y[i]>kesk:
            print(f"{x[i]} saab suurem kui keskmine palk, ta saab {y[i]}")
        elif y[i]==kesk:
            print(f"{x[i]} saab täpselt keskmine palk")

def tulumaks(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    """
    for i in range(0,len(y)):
        if y[i]<500:
            palk=y[i]
        elif 500>=y[i]<=1200:
            palk=(y[i]-500)-(y[i]-500)*0.2
        elif 1200>y[i]>=2099:
            palk=(500-(5/9)*(y[i]-1200))-(500-(5/9)*(y[i]-1200))*0.2
        else:
            palk=y[i]*0.2
        print(f"{x[i]} on maksuvaba palk {palk}")

def sorteerimine(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    vali=input("Sorteeri nime (1) või palga järgi (2) ")
    while vali not in ["1","2"]:
        vali=input("Kirjuta ainult 1 või 2 ")
    if vali=="1":
        vali_2=input("A–Z või Z–A ").upper()
        while vali_2 not in ["A-Z","Z-A"]:
            vali_2=input("A–Z või Z–A ").upper()
        for p in range(0,len(x)):
            for o in range(0,len(x)):
                if x[p]==x[o] and p!=o:
                    for u in range(0,len(x)):
                        x[o]+=f"_{u+1}"
                        break
        kopia=x.copy()
        x.sort()
        y1=[]
        for i in range(0,len(x)):
            ind=kopia.index(x[i])
            y1.insert(i,y[ind])
        y=y1
        if vali_2=="Z-A":
            x.reverse()
            y.reverse()
    else:
        for p in range(0,len(x)):
            for o in range(0,len(x)):
                if y[p]<y[o]:
                    abi=y[p]
                    y[p]=y[o]
                    y[o]=abi
                    abi=x[p]
                    x[p]=x[o]
                    x[o]=abi
        vali_2=input("Kasvav või kahanev järjekord ").title()
        while vali_2 not in ["Kasvav","Kahanev"]:
            vali_2=input("Kasvav või kahanev! ").title()
        if vali_2=="Kahanev":
            x.reverse()
            y.reverse()
    return x,y 

def keskpop(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    x1=[] 
    y1=[]
    kesk=sum(y)/len(y)
    print(f"Keskmine palk on {kesk}")
    for i in range(0,len(x)):
        if y[i]>kesk:
            y1.append(y[i])
            x1.append(x[i])
    x=x1 
    y=y1
    return x,y

def tint(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    for i in range(0,len(x)):
        x[i]=x[i].title()
        y[i]=round(y[i],1) 
        y[i]=int(y[i])
    return x,y

def pogod(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    vali=input("Kas soovite teada 1 inimese (1), mitme inimese (2) või kõigi (3) palka? ")
    while vali not in ["1","2","3"]:
        vali=input("Kirjtua ainult 1, 2 või 3 ")
    if vali in ["3","1"]:
        aasta=input("Mitme aasta pärast soovite palka teada? ")
        while aasta.isdigit()==False or aasta=="0":
            aasta=input("Kirjtua õige arv ")
    if vali=="3":
        for o in range(0,len(x)):
            newy=y[o]
            for i in range(0,int(aasta)):
                newy+=newy*0.05
            print(f"{x[o]} palk {aasta} aasta pärast on {round(newy,2)} eurot")
    elif vali=="1":
        nimi=input("Keda soovite muudatustest teada? ")
        while nimi not in x:
            nimi=input("Kirjuta õige nimi ")
        ind=x.index(nimi)
        newy=y[ind]
        for i in range(0,int(aasta)):
            newy+=newy*0.05
        print(f"{nimi} palk {aasta} aasta pärast on {round(newy,2)} eurot")
    else:
        arv=input("Mitut inimest me testime? ")
        while arv.isdigit()==False or int(arv)==0 or int(arv)>len(x):
            arv=input("Kirjuta õige arv ")
        for i in range(0,int(arv)): 
            nimi=input(f"Keda sa tahad kontrollida {i+1}? ")
            while nimi not in x:
                nimi=input("Kirjuta õige nimi ")
            aasta=input("Mitme aasta pärast soovite palka teada? ")
            while aasta.isdigit()==False or aasta=="0":
                aasta=input("Kirjtua õige arv ")
            ind=x.index(nimi)
            newy=y[ind]
            for i in range(0,int(aasta)):
                newy+=newy*0.05
            print(f"{nimi} palk {aasta} aasta pärast on {round(newy,2)} eurot")

def petew(x:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :rtype: list
    """
    for i in range(0,len(x),3):
        neni=input("Kirjuta uus nimi ")
        while neni.isdigit() or len(neni)<1:
            neni=input("Kirjuta õige nimi ")
        x.pop(i)
        x.insert(i,neni)
    return x
