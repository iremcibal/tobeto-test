#FOR 

#start => döngümüzün başlangıç değerini belirtir (0)
#stop => döngümüzün biteceği değeri belirtir
#step => artış miktarı (1)
# for i in range(10):
#     print(i)


""" biggestValue = 0
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı giriniz. " ))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiğiniz sayılar arasında en büyük olanı: {biggestValue}") """


""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))

for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i) """


""" sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz.")))

#defaultu küçükten büyüğe
sayilar.sort(reverse=True)
print(sayilar) """

ogrenciler = ["Güneş", "Recep", "Betül", "Yunus", "irem"]
#length
""" print(len(ogrenciler))

for i in range(len(ogrenciler)):
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

for ogrenci in ogrenciler:
    print(f"Öğrenci: {ogrenci}") """

#break : ilgili döngünün o anda kırılmasını sağlıyor
for i in range(len(ogrenciler)):
    if i>2:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#continue : iterasyondaki current değeri atla, bir sonraki değer ile devam et
for ogrenci in ogrenciler:
    if ogrenci == "Recep":
        continue
    print(f"Öğrenci: {ogrenci}")

#WHILE 
i = 0
while i < 10:
    print("Merhaba")
    i +=1