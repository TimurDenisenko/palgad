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
        nimi=input("Mis nimi on uue inimene? ").title()
        while nimi.isdigit() or len(nimi)<2:
            nimi=input("Kirjuta õige nimi ").title()

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
    nimi=input("Kirjuta nimi mis tahad kustuda ").title()
    while nimi.isdigit() or len(nimi)<2 or nimi not in x:
        nimi=input("Kirjuta õige nimi! ").title()
    n=x.count(nimi)
    if n!=0:
        print("Siin on mõned inimesed sama nimega")
        valik=input("Kas sa tahad kustuda mõned inimesed? (jah või ei) ").lower()
        while valik not in ["jah","ei"]:
            valik=input("Kirjuta ainult jah või ei ").lower() 
        if valik=="jah":
            j=input("Kui palju inimesed sama nimega sa tahad kustuda? ")
            while j.isdigit()==False or int(j)>=n+1 or int(j)==1:
                j=input("Kirjuta õige arv! ")
            j=int(j)
            for _ in range(j):
                valik=input(f"Siin on {n} nimed, mis nimed sa tahad kustuda? ")
                while valik.isdigit()==False or int(valik)>=n+1:
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
            tegevus=input(f"Siin on {n} nimed, mis nimi sa tahad kustuda? ")
            while tegevus.isdigit()==False or int(tegevus)>=n+1:
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
    if n>1:
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
            kopia.insert(ind,0)
            ind=kopia.index(min(kopia))
        vas=(f"ja nad saavad {min(y)}")
    else:
        vas=(f"Saab minimaalne palka {x[ind]} ja ta saab {y[ind]}")
    return vas