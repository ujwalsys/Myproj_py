import json

# Step 1: Initialize an empty dictionary for students and their attendance
attendance = {}

# Load attendance from file if it exists
def load_attendance():
    try:
        with open('attendance.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save attendance to a file
def save_attendance():
    with open('attendance.json', 'w') as file:
        json.dump(attendance, file)
    print("Attendance saved successfully!")

# Step 2: Function to add a student
def add_student(name, enrollment):
    if enrollment not in attendance:
        attendance[enrollment] = {'name': name, 'status': 'Absent'}
        print(f"Student {name} with enrollment {enrollment} added.")
    else:
        print(f"Student with enrollment {enrollment} is already in the list.")

# Function to mark attendance
def mark_attendance(enrollment):
    if enrollment in attendance:
        attendance[enrollment]['status'] = 'Present'
        print(f"Attendance marked for {attendance[enrollment]['name']}.")
    else:
        print(f"Student with enrollment {enrollment} is not in the list. Please add the student first.")

# Step 3: Function to display attendance
def display_attendance():
    print("Attendance List:")
    for enrollment in sorted(attendance.keys(), key=lambda x: attendance[x]['name']):
        student = attendance[enrollment]
        print(f"{student['name']} (Enrollment: {enrollment}): {student['status']}")

# Main code to demonstrate the functionality
if __name__ == "__main__":
    attendance = load_attendance()
    
    while True:
        print("\n1. Add Student\n2. Mark Attendance\n3. Display Attendance\n4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_name = input("Enter student name: ")
            enrollment_number = input("Enter enrollment number: ")
            add_student(student_name, enrollment_number)
        elif choice == '2':
            enrollment_number = input("Enter enrollment number to mark attendance: ")
            mark_attendance(enrollment_number)
        elif choice == '3':
            display_attendance()
        elif choice == '4':
            save_attendance()
            break
        else:
            print("Invalid choice. Please try again.")
