# my first programme
school_name = "lztv"
school_name_2 = "R88vsk"
x = 5
y = x ** 2
# operand1 operator operand2

z1 = x / 2
z2 = x // 2
z3 = x % 2



print(x, y)
print(z1, z2, z3)

print(school_name, school_name_2)

from datetime import date
datums = date(2022,11,19)
print(datums)
print('no mūsu ēras sākuma pagājušas', datums.toordinal(), 'dienas')
print('Pēc 800000 dieām būs', datums.fromordinal(800000))

class Koks:
    def __init__(self, kt, kv):
        self.koka_tips = kt
        self.koka_lapu_veids = kv
    def drukat(self):
        print("Koka tips: ", self.koka_tips)
        print("Koka veids: ", self.koka_lapu_veids)
    def augt(self):
        print("Koks aug!")
    def sanemt_razu(self, kg):
        print(kg)        

koks1 = Koks ("liepa", "lapu koks")
koks1.drukat()
koks1.augt()
koks1.sanemt_razu(3)

#koks2 = Koks ("egle", "skuju koks")
koks2.drukat()
koks2.augt()
koks2.sanemt_razu(2)
