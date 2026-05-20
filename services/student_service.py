from services.file_service import (
    load_students,
    save_students
)


def get_all_students():

    return load_students()


def add_student(student):

    students = load_students()

    students.append(student)

    save_students(students)


def delete_student(student_id):

    students = load_students()

    updated_students = [

        student for student in students
        if student["id"] != student_id
    ]

    save_students(updated_students)


def search_students(keyword):

    students = load_students()

    keyword = str(keyword).lower()

    results = []

    for student in students:

        student_id = str(
            student["id"]
        ).lower()

        student_name = str(
            student["name"]
        ).lower()

        student_course = str(
            student["course"]
        ).lower()

        if (

            keyword in student_id

            or keyword in student_name

            or keyword in student_course

        ):

            results.append(student)

    return results

def update_student(student_id, updated_student):

    students = load_students()

    for student in students:

        if str(student["id"]) == str(student_id):

            student["name"] = updated_student["name"]

            student["age"] = updated_student["age"]

            student["course"] = updated_student["course"]

            student["email"] = updated_student["email"]

            student["subject1"] = updated_student["subject1"]

            student["subject2"] = updated_student["subject2"]

            student["subject3"] = updated_student["subject3"]

            break

    save_students(students)

def update_student(student_id, updated_student):

    students = load_students()

    for student in students:

        if str(student["id"]) == str(student_id):

            student["name"] = updated_student["name"]

            student["age"] = updated_student["age"]

            student["course"] = updated_student["course"]

            student["email"] = updated_student["email"]

            student["subject1"] = updated_student["subject1"]

            student["subject2"] = updated_student["subject2"]

            student["subject3"] = updated_student["subject3"]

            break

    save_students(students)