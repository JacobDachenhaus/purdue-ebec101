"""
Author: Jacob Dachenhaus, jdachenh@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/22/2021

Description:
    Program that takes a course number and looks up its course
    info, including the room, instructor, and time.

Contributors:
    None

My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

def get_course_data():
    # Hard coded dictionary values
    return {
        'CS101': { 'room': '3004', 'instructor': 'Django', 'time': '9:00 a.m.' },
        'CS102': { 'room': '4501', 'instructor': 'Idle', 'time': '10:00 a.m.'},
        'CS103': { 'room': '6755', 'instructor': 'Rich', 'time': '11:00 a.m.' },
        'NT110': { 'room': '1244', 'instructor': 'Marshal', 'time': '12:00 p.m.' },
        'CM241': { 'room': '1411', 'instructor': 'Pickle', 'time': '2:00 p.m.'}
    }
    #END get_course_data def

def main():
    course_data = get_course_data()
    cn = input('Enter a course number: ')
    course = course_data.get(cn) # Fetch the course from course_data

    # Check for invalid course
    if course == None:
        print(f'  {cn} is an invalid course number.')
        return

    # Get course info
    instructor = course.get('instructor')
    room = course.get('room')
    time = course.get('time')

    # Format and output
    print(f'  The details for course {cn} are:')
    print(f'    Instructor: {instructor}')
    print(f'          Room: {room}')
    print(f'          Time: {time}')
    #END main def

if __name__ == '__main__':
    main()
