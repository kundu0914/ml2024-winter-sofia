def main():
    # Step 1: Ask the user for input N
    N = int(input("Enter a positive integer N: "))

    # Step 2: Ask the user to provide N numbers
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Step 3: Ask the user for input X
    X = int(input("Enter an integer X: "))

    # Step 4: Output the result
    if X in numbers:
        index = numbers.index(X) + 1
        print(f"The index of {X} is: {index}")
    else:
        print("-1")

if __name__ == "__main__":
    main()
