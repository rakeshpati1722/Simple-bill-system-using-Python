def idli():
    idli=50+2.0
    print("Your bill is :",idli)

def vada():
    vada=30+2.0
    print("Your bill is :", vada)

def dosa():
    vada=40+2.0
    print("Your bill is :", dosa)

def puri():
    vada=20+2.0
    print("Your bill is :", puri)
# north indian recipe
def rice():
    r=50+2.0
    print("Your bill is :",r)

def roti():
    r1=30+2.0
    print("Your bill is :", r1)

def paratha():
    p=40+2.0
    print("Your bill is :", p)

def chole():
    c=20+2.0
    print("Your bill is :", c)
# north indian ends


while True:
    print("1.South indian")
    print("2.North indian")
    choice=int(input("Enter your menu choice:"))
    if choice == 1:
        print("1.Idli")
        print("2.vada")
        print("3.dosa")
        print("4.puri")
        choice2=int(input("Enter south indian choice:"))
        if choice2 == 1:
            idli()
        elif choice2 == 2:
            vada()
        elif choice2 == 3:
            dosa()
        elif choice2 == 4:
            puri()
        # extra = str(input("Extra items ?:Y/N"))
        # if extra == 'Y':
        #     continue;
        # else:
        #     break
        continue
    elif choice == 2:
        print("1.Rice")
        print("2.Roti")
        print("3.Paratha")
        print("4.Chole")
        choice3 = int(input("Enter north indian choice:"))
        if choice3 == 1:
            rice()
        elif choice3 == 2:
            roti()
        elif choice3 == 3:
            paratha()
        elif choice3 == 4:
            chole()
        continue
    else:
        print("enter valid choice")
        continue;