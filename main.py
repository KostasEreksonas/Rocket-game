import random


class Zigulys:
    def __init__(self,valstybinis):
        print("Sukurtas naujas zigulys")
        self.valstybinisNumeris=valstybinis
    def uzvesti(self):
        print("Zigulys "  +self.valstybinisNumeris+" uzvestas")


manopirmasisZigulys = Zigulys("BCM440")
manoantrasisZigulys = Zigulys("KJE320")
manopirmasisZigulys.uzvesti()
manoantrasisZigulys.uzvesti()
garazas = []
for i in range (0,20):
    numeris = random.randint(100,999)
    naujasAutomobilis = Zigulys("ABC"+ str(numeris))
    garazas.append(naujasAutomobilis)
    #print(naujasAutomobilis.valstybinisNumeris)

for automobilis in garazas:
    automobilis.uzvesti()