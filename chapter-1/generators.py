

# def fun(genexp):
#     for value in genexp:
#         print(value,end=" ")


class Customer:

    def firstName(self, firstname):
        self.firstname = firstname
        return self
    
    def lastName(self, lastname):
        self.lastname = lastname
        return self
    
    def _print(self):
        print(f"HI {self.firstname} {self.lastname}")




if __name__ == "__main__":
#     symbols = "abcdesfjkxw"
#     fun(ord(symbol) for symbol in symbols)
    Customer().firstName("Prince").lastName("Raj")._print()
    ...


 