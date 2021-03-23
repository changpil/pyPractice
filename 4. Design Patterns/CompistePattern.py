

class Manu:
    def __init__(self, s):
        self.manuitem = ManuItem(s)
        self.components = list()


class ManuItem():
    def __init__ (self, s):
        self.txt = s

def traverse(manu, indent):
    print(indent, manu.manuitem.txt)
    for decen in manu.components:
        traverse(decen, indent + "-")

mainManu = Manu("file")
mainManu.components.append(Manu("open"))
mainManu.components.append(Manu("save"))
mainManu.components.append(Manu("exit"))

mainManu.components[0].components.append(Manu("open local"))
mainManu.components[0].components.append(Manu("open box"))
mainManu.components[0].components.append(Manu("open istore"))

mainManu.components[1].components.append(Manu("save local"))
mainManu.components[1].components.append(Manu("save box"))
mainManu.components[1].components.append(Manu("save istore"))


traverse(mainManu, "")