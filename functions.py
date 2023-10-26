#definition 

def ortalamaHesapla():
    final= 69
    vize= 87
    ortalama = (vize* 0.4) + (final* 0.6)
    print(ortalama)

def ortalamaHesaplaVeDöndür():
    final= 69
    vize= 87
    ortalama = (vize* 0.4) + (final* 0.6)
    return ortalama

ortalamaHesapla()
print(ortalamaHesaplaVeDöndür())

def ortalamaHesapla(vize:float,final:float) -> float:
    return (vize* 0.4) + (final * 0.6)

print(ortalamaHesapla(50,78))

vize = int(input("vize notunuzu giriniz: "))
final = int(input("final notunuzu giriniz: "))

def ortalamaHesaplaVeYazdır(vize=vize,final=final):
    return (vize* 0.4) + (final * 0.6)

print(ortalamaHesaplaVeYazdır())