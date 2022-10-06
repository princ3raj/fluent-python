
class Number:
    def __init__(self, num) -> None:
        self.num = num
    
    def __add__(self, obj):
        return self.num + obj.num

    @property
    def value(self):
        return self.num

n1  = Number(2)
n2 =  Number(3)

print(n1.value, n2.value)
print(n1.value + n2.value)