class Szemely:
    neve = ''
    kor = None
    neme = ''

    def setKor(self, kor):
        self.kor = kor


sz1 = Szemely()
sz1.setKor(21)
print(sz1.kor)