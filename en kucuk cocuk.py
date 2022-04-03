def cocuk_yas(x):
    x=int(input("1yas giriniz: "))
    print(x)

def cocuk_yas1(y):
    y=int(input("2.yas giriniz: "))
    print(y)


def cocuk_yas2(z):
    z=int(input("3.yas giriniz: "))
    print(z)


yas=[16,18,23]

b=[]
if yas[0]==cocuk_yas:
    b.append(cocuk_yas)
    print("adem yas: ",cocuk_yas)
    
elif yas[1]==cocuk_yas1:
    b.append(cocuk_yas1)
    print("ayse yas: ",cocuk_yas1)
    
elif yas[2]==cocuk_yas2:
    b.append(cocuk_yas2)
    print("ali yas: ",cocuk_yas2)





