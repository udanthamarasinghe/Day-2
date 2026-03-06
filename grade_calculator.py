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
        
        print(f"\nStudent Name: {name}")
        print(f"Average Mark: {average:.2f}")
        
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"
        
        if grade == "Fail":
            print(f"Result: {grade}")
        else:
            print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
