class Human:
    #property,attribute => nitelik,özellik
    # name= "irem"
    # age=25

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalıştı")

    #method,davranışlar
    def talk(self,message):
        print(message)

    def walk(self):
        print(f"{self.name} is Walking")

#instance üretmek => örnek ürettiğimi belirtiyorum
human1 = Human("Şeyma", 25)
# human1.name = "şeyma"
# human1.age = 24
human1.talk("Merhaba")
human1.walk()
