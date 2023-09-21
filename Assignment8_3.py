
def display_Pattern(n):
    if n==0:
        return
    
    else:
        print(n,end=" ")
        display_Pattern(n - 1)
        

def main():
    n= int(input("Enter the number:"))

    display_Pattern(n)


if __name__ =="__main__":
    main()
