import abc
class Expression(abc.ABC):
    @abc.abstractmethod
    def evaluate(self):
        pass

class Number(Expression):
    def __init__(self, num):
        self.num = num
    def evaluate(self):
        return self.num

class Variable(Expression):
    def __init__(self, var, num):
        self.var = var
        self.num = num
    def evaluate(self):
        return self.num

class Operator(Expression):
    pass
class Addition(Operator):
    def __init__(self, right, left):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Multiplication(Operator):
    def __init__(self, right, left):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

#  a + b(2 + a) * 5
a = Variable("a", 13)
b = Variable("b", 14)
num2 = Number(2)
num5 = Number(5)
sub = Multiplication(b, Addition(num2,a))
main  = Addition(a, Multiplication(sub,num5))
print(main.evaluate())