class Klass:

    def skriv_ut_min_klass(self):
        print(Klass.__name__)

    def detta_är_en_metod(self):
        print('Detta är en metod!')

k = Klass()

def skriv_klass_1(klass:Klass):
    klass.skriv_ut_min_klass()
    klass.detta_är_en_metod()

def skriv_klass_2():
    k.skriv_ut_min_klass()
    k.detta_är_en_metod()


skriv_klass_1(k)
skriv_klass_2()