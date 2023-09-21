
def display_Pattern(n):
    if n==0:
        return
    
    else:
        display_Pattern(n - 1)
        print(n,end=" ")

def main():
    n= int(input("Enter the number:"))

    display_Pattern(n)


if __name__ =="__main__":
    main()
