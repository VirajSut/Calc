def add(x,y):
    return x + y 

def subtract(x,y):
    return x-y

#multiply numbers 
def mult(x,y):
    return x*y

def divide(x,y):
    return x/y

print("what Operation")
print('add')
print('subtract')
print('multiply')
print('divide')

while True:
    choice= input('Enter choice(+,-,*,/)')

    if choice in ("+","-","*","/"):
            x=float(input(" First Num"))
            y=float(input(" Second Num"))

            if("+"):
                out: float=add(x,y)
                print(out)

                
            
            

