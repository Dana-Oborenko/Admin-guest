class Cilveks:
    def __init__(self, v, u, a, s, sl, ak):
        self.vards = v
        self.uzvards = u
        self.augums = a
        self.svars = s
        self.slimibas = sl
        self.acu_krasa = ak

    def drukat(self):
        print("Cilvēka vards: ", self.vards)
        print("Cilvēka uzvards: ", self.uzvards)
        print("Cilvēka augums: ", self.augums)
        print("Cilvēka svars: ", self.svars)
        print("Cilvēka slimibas: ", self.slimibas)
        print("Cilvēka acu krasa: ", self.acu_krasa)
       
    def parbaudit_analizes(self):
        print(self.vards, "labā stāvoklī")
        print(self.vards + " labā stāvoklī")
        print("{} labā stāvoklī".format(self.vards))

cilveks1 = Cilveks("Māris", "Ozols", "172", "50", "nav", "zaļa")
# cilveks1.drukat()
# cilveks1.parbaudit_analizes()

vards = input("Lūdzu, ievadiet savu vārdu: ")
uzvards = input("Lūdzu, ievadiet savu uzvardu: ")
augums = input("Lūdzu, ievadiet savu augumu: ")
svars = input("Lūdzu, ievadiet savu svaru: ")
slimibas = input("Lūdzu, ievadiet savas slimības: ")
acu_krasa = input("Lūdzu, ievadiet savu acu krāsu: ")

cilveks2 = Cilveks(vards, uzvards, augums, svars, slimibas, acu_krasa)
# cilveks2.drukat()
# cilveks2.parbaudit_analizes()

cilveks3 = Cilveks("Lauris", "Kalniņš", "189", "75", "alerģija", "zīlas")
cilveks4 = Cilveks("Marta", "Cīrule", "159", "46", "nav", "brūnas")

cilveki = [cilveks1, cilveks2, cilveks3, cilveks4]
for i in cilveki:
    i.drukat()
    print()
