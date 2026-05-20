from services.file_service import load_students


# =========================
# CALCULATE AVERAGE
# =========================

def calculate_average(student):

    subject1 = student.get(
        "subject1",
        0
    )

    subject2 = student.get(
        "subject2",
        0
    )

    subject3 = student.get(
        "subject3",
        0
    )

    total = (
        subject1 +
        subject2 +
        subject3
    )

    return round(total / 3, 2)


# =========================
# HIGHEST STUDENT
# =========================

def highest_student():

    students = load_students()

    if not students:
        return None

    return max(
        students,
        key=calculate_average
    )


# =========================
# LOWEST STUDENT
# =========================

def lowest_student():

    students = load_students()

    if not students:
        return None

    return min(
        students,
        key=calculate_average
    )


# =========================
# PASS FAIL REPORT
# =========================

def pass_fail_report():

    students = load_students()

    report = []

    for student in students:

        average = calculate_average(
            student
        )

        status = (
            "Pass"
            if average >= 40
            else "Fail"
        )

        report.append({

            "name": student["name"],

            "average": average,

            "status": status

        })

    return report


# =========================
# COURSE WISE AVERAGE
# =========================

def course_wise_average():

    students = load_students()

    course_data = {}

    for student in students:

        course = student["course"]

        average = calculate_average(
            student
        )

        if course not in course_data:

            course_data[course] = []

        course_data[course].append(
            average
        )

    final_result = {}

    for course, averages in course_data.items():

        final_result[course] = round(

            sum(averages) / len(averages),

            2
        )

    return final_result


# =========================
# STUDENT AVERAGES
# =========================

def student_average_report():

    students = load_students()

    report = []

    for student in students:

        report.append({

            "name": student["name"],

            "average": calculate_average(
                student
            )
        })

    return report