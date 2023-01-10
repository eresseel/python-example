class Szemely:
    def hello(self):
        print("hello " + self.nev)

    def __init__(self, nev, db, vallas="hindu"):
        self.nev = nev
        self.db = db
        self.vallas = vallas
        self.hello()

alma = Szemely("alma", 5)
print(alma.nev)
print(alma.db)
print(alma.vallas)