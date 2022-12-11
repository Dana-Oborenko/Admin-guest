class Rectangle:
    def __init__(self, g, s):
        self.garums = g
        self.saurums = s
        self.perimetrs = self.garums+self.saurums+self.garums+self.saurums
        self.laukums = self.garums*self.saurums

    def drukat_perimetru(self):
        print("Perimetrs: ", self.perimetrs)

rectangle1 = Rectangle(4, 3)
rectangle1.drukat_perimetru()