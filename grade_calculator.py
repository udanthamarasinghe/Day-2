def main():
    while True:
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        if name.lower() == 'exit':
            break
        
        marks = []
        for i in range(1, 4):
            while True:
                try:
                    mark = float(input(f"Enter mark for subject {i}: "))
                    marks.append(mark)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        average = sum(marks) / len(marks)
        
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"
        
        print("-" * 30)
        print(f"Name    : {name}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
