class Base1:
    def __init__(self):
        print("Base1")

class Base1_mid1(Base1):
    pass

class Base1_mid2(Base1):
    def __init__(self):
        super().__init__()
        print("Base1_mid2")

class Base2(Base1_mid1, Base1_mid2):
    pass

b1 =Base1_mid1()
b1 =Base1_mid2()

