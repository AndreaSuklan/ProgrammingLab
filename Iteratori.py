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
'''
class Data:
    def __init__(self,g,m,a):
        self.g=g
        self.m=m
        self.a=a
        self.mesibrutti=[11,4,6,9]

    def __str__(self):
        return "Il giorno successivo sarà il {}/{}/{}\n".format(self.g,self.m,self.a)

    def __iter__(self):
        return self

    def __next__(self):
        origine = [self.g,self.m,self.a]
        if (self.a%400 == 0 or (self.a%4 == 0 and self.a%100 != 0)):
            bisestile = True
        else:
            bisestile = False
        if (self.g == 28 and not bisestile and self.m == 2):
            self.g = 1
            self.m = 3
        elif (self.g == 29 and bisestile and self.m == 2):
            self.g = 1
            self.m = 3
        elif (self.g == 31 and self.m not in self.mesibrutti):
            if (self.m==12):
                self.g = 1
                self.m = 1
                self.a += 1
            else:
                self.g = 1
                self.m += 1
        elif (self.g == 30 and self.m in self.mesibrutti):
            self.g = 1
            self.m += 1
        else:
            self.g += 1

        return Data(self.g,self.m,self.a)

data=Data(int(input("Inserire il giorno il mese e l'anno\n")),int(input()),int(input()))
viaggio_data=iter(data)
n=int(input("Di quanti giorni vuoi andare avanti?\n"))
for i in range(n-1):
    print(next(viaggio_data))
print(next(viaggio_data))

            

        
