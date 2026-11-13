# ex number 1
bill_total = int(input("Enter the total bill amount: "))
amount_people = int(input("Enter the number of people: "))
total_with_tip = bill_total * 1.15
individual_share = total_with_tip / amount_people
print(f"Total bill with tip: ${total_with_tip:.2f}")
print(f"Each person should pay: ${individual_share:.2f}")
# ex number 2
print("\n---Welcome to the cinema---")
age = int(input("Enter your age: "))
ticket=input("do you have a ticket? (yes/no): ")

if age < 16:
    print("You are not allowed to watch the movie.")
elif age >=16 and ticket == "yes":
    print("You are allowed to watch the movie.")
elif age >18 and age <60:
    print("you have discount of 20% for popcorn ")
else:
    print("go buy a ticket first.")

# ex number 3
print("\n---Welcome to the game guess number---")
while True:
    secret_number = 7
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Wrong guess. Try again.") 

# ex number 4
print("\n ---Welcome to the multiplication calculator---")
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

#ex number 5
print("\n---Welcome to the results of a control work---")
results = [("Ali", 5), ("Elbek", 3), ("Vaxob", 4), ("Sobir", 2),
        ("Azim", 5), ("Sitora", 4), ("Farzona", 2), ("Djovanna", 5)]

total_score = 0
excellent_students = []
retake_count = 0
grades = set()
grade_counts = {}

for name, score in results:
    total_score += score
    grades.add(score)
    if score == 5:
        excellent_students.append(name)
    if score == 2:
        retake_count += 1
    grade_counts[score] = grade_counts.get(score, 0) + 1

average_score = total_score / len(results)
print(f"Average score: {average_score}")
print(f"Students with grade 5: {excellent_students}")
print(f"Students needing retake: {retake_count}")
print(f"Different grades: {grades}")
print(f"Count of each grade: {grade_counts}")

# part 2 ex number 1
print("\n---Welcome to the journal of students---")
journal = {
    "Ali": [5, 4, 5],
    "Muxriddin": [3, 4],
    "Timur": [2, 3, 3],
}

menu = """
1. Add a student
2. Remove a student
3. Show all students
4. put a grade for a student
5. Show average grade for a student
6.the student with the highest average grade
7. list if students that fall below a certain grade
8. Exit
""" 
while True:
    print(menu)
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        name = input("Enter the student's name: ")
        grades = list(map(int, input("Enter the student's grades separated by spaces: ").split()))
        journal[name] = grades
        print(f"Student {name} added with grades {grades}.")
    elif choice == "2":
        name = input("Enter the student's name to remove: ")
        if name in journal:
            del journal[name]
            print(f"Student {name} removed.")
        else:
            print(f"Student {name} not found.")
    elif choice == "3":
        for name, grades in journal.items():
            print(f"{name}: {grades}")
    elif choice == "4":
        name = input("Enter the student's name to add a grade: ")
        if name in journal:
            grade = int(input("Enter the grade to add: "))
            journal[name].append(grade)
            print(f"Grade {grade} added for student {name}.")
        else:
            print(f"Student {name} not found.")
    elif choice == "5":
        name = input("Enter the student's name to show average grade: ")
        if name in journal:
            average_grade = sum(journal[name]) / len(journal[name])
            print(f"Average grade for {name}: {average_grade:.2f}")
        else:
            print(f"Student {name} not found.")
    elif choice == "6":
        highest_avg_student = max(journal.items(), key=lambda x: sum(x[1]) / len(x[1]))
        highest_avg_grade = sum(highest_avg_student[1]) / len(highest_avg_student[1])
        print(f"Student with the highest average grade: {highest_avg_student[0]} with an average of {highest_avg_grade:.2f}")
    elif choice == "7":
        threshold = int(input("Enter the grade threshold: "))
        students_below_threshold = [name for name, grades in journal.items() if any(grade < threshold for grade in grades)]
        print(f"Students with grades below {threshold}: {students_below_threshold}")
    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")