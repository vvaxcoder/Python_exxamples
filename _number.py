class Number:
    def __init__(self, val) -> None:
        self.val = val
    
    def __iadd__(self, other):
        self.val += other
        return self

x = Number(6)
x += 1
x += 1
print(x.val)
