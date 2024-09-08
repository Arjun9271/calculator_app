from calcns import do_addition,do_subtraction

def main():
    print("welcome to the calculator App")
    print("""\nselect the functions 
          1.Add
          2.sub""")
    user_input = input("select the function:")
    
    a = int(input("enter the value of the A:"))
    b = int(input("enter the value of the B:"))
    
    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_subtraction(a,b)
        
    print(f'result = {result}')
        
if __name__ == "__main__":
    main()