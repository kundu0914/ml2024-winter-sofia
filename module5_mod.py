from module5_oop import NumberProcessor

def main():
    n = int(input("Enter the number of elements (N): "))
    processor = NumberProcessor()

    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        processor.add_number(number)

    x = int(input("Enter the number to search for (X): "))
    index = processor.find_index(x)

    if index == -1:
        print(f"The number {x} was not found.")
    else:
        print(f"The number {x} was found at index {index}.")

if __name__ == "__main__":
    main()
