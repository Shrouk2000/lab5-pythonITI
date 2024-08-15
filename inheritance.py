class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):  
        print("the aniamal eating...")  
class cat(animal):    
    def meow(self):
        return "Meow!"
    def eat(self):
        print("the cat eat food")

x=cat("cat")
x.eat()
print(x) #the cat eat food