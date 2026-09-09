from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_college_help():
    return """
College Support Services:
1. Academic Regulations
2. Examination Information
3. Attendance Rules
4. Syllabus Information
5. Department Notices
6. Academic Calendar
7. Student FAQs
"""

def get_emergency_message():
    return """
For urgent college-related issues, students should contact their department office or college administration.
"""
