#celcius hesaplama




while True:
    try:
        celcius=float(input("bir sayi degeri girin: "))
        fahrenheit=(celcius*1.8)+32
        print("Sicaklik Degeriniz: ",fahrenheit,"°F'tir")
        break
    except ValueError:
        print("lutfen sicaklik degerini giriniz")
    





