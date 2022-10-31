import math
print('THIS IS A SCIENTIFIC CALCULATOR FOR ADVANCED OPERATION')
function=input('''
   Enter a for basic operations
   Enter b for sin,cos,tan and log
   Enter c for square and squareroot
   Enter d for exponentiation:
 ''')
if function=='a':
    operation=input('Enter a for addition,s for subtraction, m for multiplication, d for division:')
    if operation=='a':
       a=int(input('Enter first number:'))
       b=int(input('Enter second number:'))
       c=print(a+b)
    elif operation=='s':
       a=int(input('Enter first number:'))
       b=int(input('Enter second number:'))
       c=print(a-b)
    elif operation=='m':
       a=int(input('Enter first number:'))
       b=int(input('Enter second number:'))
       c=print(a*b)
    elif operation=='d':
       a=int(input('Enter first number:'))
       b=int(input('Enter second number:'))
       c=print(a/b)
    else:
        print('WRONG INPUT')
elif function=='b':
    operation=input('Enter s for sin, c for cos, t for tan and l for log:')
    if operation=='s':
        a=int(input('Enter the number:'))
        Ans=print(math.sin(a))
    elif operation=='c':
        a=int(input('Enter the number:'))
        Ans=print(math.cos(a))
    elif operation=='t':
        a=int(input('Enter the number:'))
        Ans=print(math.tan(a))
    elif operation=='l':
        a=int(input('Enter the number:'))
        Ans=print(math.log(a))
    else:
        print('WRONG INPUT')
elif function=='c':
    operation=input('Enter s for square and sq for squareroot:')
    if operation=='s':
        a=int(input('Enter the number:'))
        Ans=print(a**2)
    elif operation=='sq':
        a=int(input('Enter the number:'))
        Ans=print(math.sqrt(a))
elif function=='d':
    a=int(input('Enter the base number:'))
    b=int(input('Enter the power:'))
    Ans=print(a**b)
else:
    print('WRONG INPUT')
print('THANKS FOR USING OUR APP')
   
    
        
    

       
    
    
 


    


