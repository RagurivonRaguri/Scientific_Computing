def structures():
    my_input = int(input("Enter a number: ")) 
    
    if my_input % 2 == 0:
        print(f"{my_input} is even.")
    else:
        print(f"{my_input} is odd.")

    even_numbers = [i for i in range(1, my_input + 1) if i % 2 == 0] #list comprehension
    odd_numbers = [i for i in range(1, my_input + 1) if i % 2 != 0]

    print(f"Even numbers from 1 to {my_input}: {even_numbers}")
    print(f"Odd numbers from 1 to {my_input}: {odd_numbers}")

    num = 10
    print("Countdown from 10 to 1:")
    while num >= 1:
        print(num, end=" ") 
        num -= 1
    print()  

structures()
