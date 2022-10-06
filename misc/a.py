

class A(object):
    def __init__(self,value):
        self.value = value

    def __add__(self, obj):
        return self.value + obj.value

    def __mul__(self, obj):
        return self.value * obj.value
    
    def __len__(self):
        return 100


    


if __name__ == "__main__":
    a = A(2)
    b = A(3)
    print(len(a), len(b))
    print(a*b)