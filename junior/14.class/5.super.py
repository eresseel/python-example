class Szemely:
    def hello(self):
        print("hello " + self.nev)

    def __init__(self, nev, db, vallas="hindu"):
        self.nev = nev
        self.db = db
        self.vallas = vallas
        self.hello()

class Alkalmazott(Szemely):
    def __init__(self, nev, db, vallas, tapasztalat, megbizhatosag, vegzettseg):
        super().__init__(nev, db, vallas)
        self.tapasztalat = tapasztalat
        self.megbizhatosag =  megbizhatosag
        self.vegzettseg = vegzettseg

alma = Alkalmazott("alma", 5, "pogany", 8, 8, "korte")
print(alma.vegzettseg)