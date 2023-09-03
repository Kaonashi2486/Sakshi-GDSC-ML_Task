
# number1=("input the furst number")
# number2=("input the second number")

op=input("enter what type of calculation is to be performed")
exp=input("enter the expression")
def compute(op,exp):  
    if op=="+":
        numbers=exp.split('+')
        sum=0
        for i in range(len(numbers)):
            sum+=float(numbers[i])
        return sum
    elif op=="-":
        numbers=exp.split('-')
        for i in range(len(numbers)):
            sum-=float(numbers[i])
        return sum 
    elif op=="*":
        sum=1
        numbers=exp.split('*')
        for i in range(len(numbers)):
            sum*=float(numbers[i])
        return sum 
    elif op=="/":
        numbers=exp.split('/')
        sum=float(numbers[0])
        i=1
        while i<len(numbers):
            sum/=float(numbers[i])
            i+=1
        return sum 
# i=compute(number1,number2,op)
# prfloat(i)
sum=compute(op,exp)
print(sum)