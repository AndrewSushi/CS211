def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def floordiv(a, b):
    return a // b

operands = {"+":add,"-":sub,"*":mul,"/":floordiv}

class ASTNode():
    def __init__(self):
        raise NotImplementedError("Not yet implemented")
    
    def eval(self):
        raise NotImplementedError("Not yet implemented")

    def __str__(self):
        raise NotImplementedError("Not yet implemented")

class BinOp(ASTNode):
    def __init__(self, symbol: str, left: ASTNode, right: ASTNode):
        self.symbol = symbol
        self.left = left
        self.right = right
    def eval(self) -> int:
        return operands[self.symbol](self.left.eval(), self.right.eval())

    def __str__(self) -> str:
        return f"<{self.symbol},{self.left},{self.right}>"

class Num(ASTNode):
    def __init__(self, val: int):
        self.val = val

    def eval(self) -> int:
        return self.val

    def __str__(self) -> str:
        return f"{self.val}"

def main():
    bin1 = BinOp("+", Num(3), Num(4))
    bin2 = BinOp("+", Num(1), Num(2))
    tree = BinOp("-", bin1, bin2)
    print(tree)
    print(tree.eval())

main()



    # def eval(self) -> int:
    #     # if self.symbol == "+":
    #     #     return self.left.eval() + self.right.eval()
    #     # elif self.symbol == "-":
    #     #     return self.left.eval() - self.right.eval()
    #     # elif self.symbol == "*":
    #     #     return self.left.eval() * self.right.eval()
    #     # else:
    #     #     return self.left.eval() // self.right.eval()

    #     return operands[self.symbol](self.left.eval(), self.right.eval())