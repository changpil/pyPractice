### First Draft

# class Menu:
#     def __init__(self, s):
#         self.menuitem = MenuItem(s)
#         self.components = list()
# class MenuItem():
#     def __init__ (self, s):
#         self.txt = s
# def traverse(menu, indent):
#     print(indent, menu.menuitem.txt)
#     for decen in menu.components:
#         traverse(decen, indent + "-")

# mainManu = Menu("file")
# mainManu.components.append(Menu("open"))
# mainManu.components.append(Menu("save"))
# mainManu.components.append(Menu("exit"))
# mainManu.components[0].components.append(Menu("open local"))
# mainManu.components[0].components.append(Menu("open box"))
# mainManu.components[0].components.append(Menu("open istore"))
# mainManu.components[1].components.append(Menu("save local"))
# mainManu.components[1].components.append(Menu("save box"))
# mainManu.components[1].components.append(Menu("save istore"))
# traverse(mainManu, "")



### Second Draft
import abc
class IMenu(abc.ABC):
    def __init__(self, s):
        self.text = s
        self.components = list()

    @abc.abstractmethod
    def addMenu(self):
        pass

class Menu(IMenu):
    def addMenu(self, text):
        self.components.append(Menu(text))

    def traverse(self, prefix):
        self._traverse(self, prefix)

    def _traverse(self, ptr, prefix):
        print(f"{prefix} {ptr.text}")
        for menu in ptr.components:
            self._traverse(menu, prefix + prefix)
    def get(self, text):
        for menu in self.components:
            if menu.text == text:
                return menu


mainMenu = Menu("file")
mainMenu.addMenu("open")
mainMenu.addMenu("save")
mainMenu.addMenu("exit")

mainMenu.get("open").addMenu("open local")
mainMenu.get("open").addMenu("open box")
mainMenu.get("open").addMenu("open istore")

mainMenu.get("save").addMenu("save local")
mainMenu.get("save").addMenu("save box")
mainMenu.get("save").addMenu("save istore")

mainMenu.traverse(" - ")