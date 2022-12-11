class Cilveks:
    def __init__(self, v, u, l, vec):
        self.vards = v
        self.uzvards = u
        self.loma = l
        self.vecums = vec

    def drukat_cilveku(self):
        return self.vards + ", " + self.uzvards + ", " + self.loma + ", " + self.vecums

admins = []
viesi = []

with open("admin.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().split(", ")
        print(line)
        admins.append(Cilveks(line[0], line[1], line[2], line[3]))

with open("viesis.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().split(", ")
        print(line)
        viesi.append(Cilveks(line[0], line[1], line[2], line[3]))
    
cilveki = admins + viesi

with open("kopejais.txt", "w") as f:
    for cilveks in cilveki:
        f.write(cilveks.drukat_cilveku())
        f.write("\n")

from collections import Counter
from operator import countOf
from statistics import mean

admins = [43, 33, 35]
age_avg = mean(admins)
visjaunakais = min(admins)
visvecakais = max(admins)

print("Vidējais administratoru vecums:\n")
print(age_avg)
print("Visjaunākais administrators:\n")
print(visjaunakais)
print("Visvēcakais administrators:\n")
print(visvecakais)

count=0
f=open('kopejais.txt','r')
admins=f.readlines()
for line in admins:
    if "administrators" in line:
        count=count+1
print("Administratoru skaits:\n")
print(count)
f.close()

count=0
f=open('kopejais.txt','r')
viesi=f.readlines()
for line in viesi:
    if "viesis" in line:
        count=count+1
print("Viesu skaits:\n")
print(count)
f.close()
