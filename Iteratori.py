'''
lista=["lol","sos",1]
for x in lista:
    print(x)
losto="banana"
lost=iter(losto)
next(lost)
print(next(lost))
print(iter(lost))
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter=iter(myclass)
#print(next(myiter))
class Serie:
    def __init__(self,low,high):
        self.low=low
        self.high=high
    def __iter__(self):
        return self
    def __next__(self):
        if (self.low>self.high):
            raise StopIteration
        else:
            self.low += 1
            return self.low-1

#ciao=Serie(int(input("Inizio\n")),int(input("Fine\n")))
#print(list(ciao))
'''
class Fib:
    def __init__(self,max):
        self.max=max
    
    def __iter__(self):
        self.n=0
        self.n0=0
        self.n1=1
        return self
    
    def __next__(self):
        if (self.n<=self.max):
            if (self.n == 0):
                result=self.n0
            if (self.n == 1):
                result=self.n1
            if (self.n > 1):
                result=self.n0+self.n1
                self.n0=self.n1
                self.n1=result
            self.n += 1
            return result
        else:
            raise StopIteration

fib=Fib(int(input("Quanti cicli di fibonacci vuoi fare?\n")))
print(list(fib))



            

        
