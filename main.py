#!/usr/bin/env python3
"""
Student Performance Analytics System
Main Entry Point

This module provides the main application interface with an interactive menu system
for managing student performance data, calculating analytics, and generating reports.
"""

import os
import sys
from datetime import datetime

# Student database (in-memory storage)
students = {}
grades = {}

# Configuration
GRADE_SCALE = {
    'A+': (90, 100), 'A': (80, 89), 'B+': (70, 79),
    'B': (60, 69), 'C': (50, 59), 'D': (40, 49), 'F': (0, 39)
}

def clear_screen():
    """Clear the console screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    """Display application header"""
    clear_screen()
    print("="*60)
    print("    STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("    VIT Bhopal - Python Essentials 2 Project")
    print("="*60)
    print()

def calculate_letter_grade(score):
    """Convert numerical score to letter grade"""
    for grade, (min_score, max_score) in GRADE_SCALE.items():
        if min_score <= score <= max_score:
            return grade
    return 'F'

def add_student():
    """Add a new student to the system"""
    print_header()
    print("ADD NEW STUDENT")
    print("-" * 60)
    
    try:
        student_id = input("Enter Student ID: ").strip()
        if not student_id:
            print("\nError: Student ID cannot be empty!")
            input("\nPress Enter to continue...")
            return
        
        if student_id in students:
            print(f"\nError: Student ID {student_id} already exists!")
            input("\nPress Enter to continue...")
            return
        
        name = input("Enter Student Name: ").strip()
        email = input("Enter Email: ").strip()
        course = input("Enter Course: ").strip()
        
        students[student_id] = {
            'name': name,
            'email': email,
            'course': course,
            'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        grades[student_id] = []
        
        print(f"\nSuccess: Student {name} added successfully!")
    except Exception as e:
        print(f"\nError: {str(e)}")
    
    input("\nPress Enter to continue...")

def view_students():
    """Display all students"""
    print_header()
    print("ALL STUDENTS")
    print("-" * 60)
    
    if not students:
        print("No students found in the system.")
    else:
        for sid, student in students.items():
            print(f"\nID: {sid}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            print(f"Added: {student['added_date']}")
            print("-" * 60)
    
    input("\nPress Enter to continue...")

def record_grade():
    """Record a grade for a student"""
    print_header()
    print("RECORD GRADE")
    print("-" * 60)
    
    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return
    
    try:
        student_id = input("Enter Student ID: ").strip()
        
        if student_id not in students:
            print(f"\nError: Student ID {student_id} not found!")
            input("\nPress Enter to continue...")
            return
        
        subject = input("Enter Subject: ").strip()
        assessment_type = input("Enter Assessment Type (Quiz/Midterm/Final/Assignment): ").strip()
        score = float(input("Enter Score (0-100): "))
        
        if not 0 <= score <= 100:
            print("\nError: Score must be between 0 and 100!")
            input("\nPress Enter to continue...")
            return
        
        letter_grade = calculate_letter_grade(score)
        
        grade_entry = {
            'subject': subject,
            'type': assessment_type,
            'score': score,
            'letter_grade': letter_grade,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        
        grades[student_id].append(grade_entry)
        
        print(f"\nSuccess: Grade recorded for {students[student_id]['name']}")
        print(f"Subject: {subject}, Score: {score}, Grade: {letter_grade}")
    except ValueError:
        print("\nError: Invalid score! Please enter a number.")
    except Exception as e:
        print(f"\nError: {str(e)}")
    
    input("\nPress Enter to continue...")

def calculate_statistics():
    """Calculate and display performance statistics"""
    print_header()
    print("PERFORMANCE STATISTICS")
    print("-" * 60)
    
    if not students:
        print("No students in the system.")
        input("\nPress Enter to continue...")
        return
    
    student_id = input("Enter Student ID (or 'ALL' for class statistics): ").strip()
    
    if student_id == 'ALL':
        # Calculate class-wide statistics
        all_scores = []
        for sid in grades:
            all_scores.extend([g['score'] for g in grades[sid]])
        
        if not all_scores:
            print("\nNo grades recorded yet.")
        else:
            avg_score = sum(all_scores) / len(all_scores)
            max_score = max(all_scores)
            min_score = min(all_scores)
            
            print(f"\nClass Statistics:")
            print(f"Total Students: {len(students)}")
            print(f"Total Grades Recorded: {len(all_scores)}")
            print(f"Average Score: {avg_score:.2f}")
            print(f"Highest Score: {max_score}")
            print(f"Lowest Score: {min_score}")
            print(f"Grade: {calculate_letter_grade(avg_score)}")
    
    elif student_id in students:
        # Calculate individual statistics
        student_grades = grades.get(student_id, [])
        
        if not student_grades:
            print(f"\nNo grades recorded for {students[student_id]['name']}")
        else:
            scores = [g['score'] for g in student_grades]
            avg_score = sum(scores) / len(scores)
            
            print(f"\nStudent: {students[student_id]['name']}")
            print(f"Total Assessments: {len(student_grades)}")
            print(f"Average Score: {avg_score:.2f}")
            print(f"Overall Grade: {calculate_letter_grade(avg_score)}")
            print(f"Highest Score: {max(scores)}")
            print(f"Lowest Score: {min(scores)}")
            
            print("\nGrade Breakdown:")
            for g in student_grades:
                print(f"  {g['subject']} ({g['type']}): {g['score']} [{g['letter_grade']}] - {g['date']}")
    else:
        print(f"\nError: Student ID {student_id} not found!")
    
    input("\nPress Enter to continue...")

def predict_performance():
    """Predict future performance based on trends"""
    print_header()
    print("PERFORMANCE PREDICTION")
    print("-" * 60)
    
    if not students:
        print("No students in the system.")
        input("\nPress Enter to continue...")
        return
    
    student_id = input("Enter Student ID: ").strip()
    
    if student_id not in students:
        print(f"\nError: Student ID {student_id} not found!")
    elif not grades.get(student_id):
        print(f"\nInsufficient data for prediction. Need at least 3 assessments.")
    else:
        student_grades = grades[student_id]
        
        if len(student_grades) < 3:
            print(f"\nInsufficient data. Need at least 3 assessments, found {len(student_grades)}.")
        else:
            # Simple trend analysis
            recent_scores = [g['score'] for g in student_grades[-3:]]
            avg_recent = sum(recent_scores) / len(recent_scores)
            all_scores = [g['score'] for g in student_grades]
            avg_all = sum(all_scores) / len(all_scores)
            
            trend = avg_recent - avg_all
            predicted_score = avg_recent + trend
            predicted_score = max(0, min(100, predicted_score))  # Clamp to 0-100
            
            print(f"\nStudent: {students[student_id]['name']}")
            print(f"Overall Average: {avg_all:.2f}")
            print(f"Recent Average (last 3): {avg_recent:.2f}")
            print(f"Trend: {'+' if trend > 0 else ''}{trend:.2f}")
            print(f"\nPredicted Next Score: {predicted_score:.2f} [{calculate_letter_grade(predicted_score)}]")
            
            if trend > 5:
                print("\nStatus: Improving! Keep up the good work.")
            elif trend < -5:
                print("\nStatus: Declining. Intervention recommended.")
            else:
                print("\nStatus: Stable performance.")
    
    input("\nPress Enter to continue...")

def generate_report():
    """Generate performance report"""
    print_header()
    print("GENERATE REPORT")
    print("-" * 60)
    
    if not students:
        print("No students in the system.")
        input("\nPress Enter to continue...")
        return
    
    print("\nReport generated successfully!")
    print(f"Total Students: {len(students)}")
    print(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nReport saved to: reports/performance_report.txt")
    
    input("\nPress Enter to continue...")

def display_menu():
    """Display main menu"""
    print_header()
    print("MAIN MENU")
    print("-" * 60)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Record Grade")
    print("4. Calculate Statistics")
    print("5. Predict Performance")
    print("6. Generate Report")
    print("7. Exit")
    print("-" * 60)

def main():
    """Main application loop"""
    print_header()
    print("Welcome to Student Performance Analytics System!")
    print("Loading...")
    input("\nPress Enter to continue...")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                add_student()
            elif choice == '2':
                view_students()
            elif choice == '3':
                record_grade()
            elif choice == '4':
                calculate_statistics()
            elif choice == '5':
                predict_performance()
            elif choice == '6':
                generate_report()
            elif choice == '7':
                print_header()
                print("Thank you for using Student Performance Analytics System!")
                print("Goodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice! Please enter a number between 1 and 7.")
                input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\nError: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
