CheckEven = lambda No: No % 2 == 0
Increase= lambda No :No+2
Add= lambda A,B :A + B

#Task: Name of function 
#Element: list of data elements
def filterX(Task, Elements):
    Result =[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result
 
def mapX(Task, Elements):
    Result=[]
    for i in Elements:
        Ret= Task(i)
        Result.append(Ret)
    return Result

def reduceX(Task, Elements):
    Result=[]
    Sum=0
    for no in Elements:
        Sum =Task(Sum,no)
    return Sum
 
def main():
    Data= []
    print("Enter the number of elemets:")

    Size =int(input())

    print("Enter the number:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
      
    #Data= [5,4,9,8,13,17,12,18]
    print("Given numbers:",Data)

    output = list(filterX(CheckEven,Data))
    print("Output after filter:",output)

    moutput= list(mapX(Increase,output))

    print("Output After Map:",moutput)

    result =reduceX(Add,moutput)
    print("Output After Reduce:",result)
   
if __name__ == "__main__":
    main()