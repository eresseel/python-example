class Szemely:
    def hello(self):
        print("hello " + self.nev)

    def __init__(self, nev, db, vallas="hindu"):
        self.nev = nev
        self.db = db
        self.vallas = vallas
        self.hello()

class Alkalmazott(Szemely):
    tapasztal = 4
    megbizhatosag = 8
    vegzettseg = "Konyvelo"

alma = Alkalmazott("alma", 5)
print(alma.vegzettseg)