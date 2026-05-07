class Avtomobil:
    def __init__(self, rang, model):
        self.rang = rang
        self.model = model

    def harakatlanish(self):
        print(f"{self.model} {self.rang} avtomobil harakatlanmoqda.")

class AvtomobilTuri(Avtomobil):
    def __init__(self, rang, model, yonilgi_turi):
        super().__init__(rang, model)
        self.yonilgi_turi = yonilgi_turi

    def harakatlanish(self):
        print(f"{self.model} {self.rang} avtomobil {self.yonilgi_turi} yonilg'ida harakatlanmoqda.")

class AvtomobilTuri2(AvtomobilTuri):
    def __init__(self, rang, model, yonilgi_turi, korobka):
        super().__init__(rang, model, yonilgi_turi)
        self.korobka = korobka

    def harakatlanish(self):
        print(f"{self.model} {self.rang} avtomobil {self.yonilgi_turi} yonilg'ida {self.korobka} korobkali harakatlanmoqda.")

avtomobil = Avtomobil("qora", "Toyota")
avtomobil.harakatlanish()

avtomobil_turi = AvtomobilTuri("qora", "Toyota", "benzin")
avtomobil_turi.harakatlanish()

avtomobil_turi2 = AvtomobilTuri2("qora", "Toyota", "benzin", "avtomat")
avtomobil_turi2.harakatlanish()
```

Open/Closed Principle: "Klasslar ochiq bo'lishi kerak, yangi xususiyatlarni qo'shish uchun yangi klasslar yaratish uchun yopiq bo'lishi kerak."
