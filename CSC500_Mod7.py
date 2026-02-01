# Course ictionaries
course_room = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

course_instructor = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

course_time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def get_course_number():
    """
    Get valid course number.
    """
    valid_courses = course_room.keys()

    while True:
        course_number = input("Enter a course number: ").strip().upper()
        if course_number in valid_courses:
            return course_number

        print("Invalid course number. Please try again.\n")


def display_course_info(course_number):
    """
    Display the room number, instructor, and meeting time
    for course.
    """
    print("\nCourse Information")
    print("-" * 20)
    print(f"Course Number: {course_number}")
    print(f"Room Number  : {course_room[course_number]}")
    print(f"Instructor   : {course_instructor[course_number]}")
    print(f"Meeting Time : {course_time[course_number]}\n")


def main():
    course_number = get_course_number()
    display_course_info(course_number)


if __name__ == "__main__":
    main()
