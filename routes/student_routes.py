from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    send_file
)

import csv

from services.student_service import (
    add_student,
    get_all_students,
    delete_student,
    search_students,
    update_student
)

from services.analytics_service import (
    highest_student,
    lowest_student,
    pass_fail_report,
    course_wise_average,
    student_average_report
)

student_bp = Blueprint(
    "student_bp",
    __name__
)


# HOME PAGE

@student_bp.route("/")
def home():

    students = get_all_students()

    return render_template(
        "students.html",
        students=students
    )


# ADD STUDENT

@student_bp.route(
    "/add",
    methods=["POST"]
)
def add():

    student = {

        "id": request.form["id"],

        "name": request.form["name"],

        "age": int(
            request.form["age"]
        ),

        "course": request.form["course"],

        "email": request.form["email"],

        "subject1": int(
            request.form["subject1"]
        ),

        "subject2": int(
            request.form["subject2"]
        ),

        "subject3": int(
            request.form["subject3"]
        )
    }

    add_student(student)

    return redirect("/")


# DELETE STUDENT

@student_bp.route("/delete/<student_id>")
def delete(student_id):

    delete_student(student_id)

    return redirect("/")


# SEARCH STUDENT

@student_bp.route("/search")
def search():

    keyword = request.args.get(
        "keyword",
        ""
    ).strip()

    if keyword == "":

        students = get_all_students()

    else:

        students = search_students(keyword)

    return render_template(
        "students.html",
        students=students
    )


# ANALYTICS

@student_bp.route("/analytics")
def analytics():

    highest = highest_student()

    lowest = lowest_student()

    report = pass_fail_report()

    course_average = course_wise_average()

    student_average = student_average_report()  

    if highest is None or lowest is None:

        return render_template(

            "analytics.html",

            highest={"name": "No Data"},

            lowest={"name": "No Data"},

            report=[]
        )

    return render_template(

        "analytics.html",

        highest=highest,

        lowest=lowest,
        
        report=report,

        course_average=course_average,

        student_average=student_average
    )


# UPDATE STUDENT

@student_bp.route(
    "/update/<student_id>",
    methods=["GET", "POST"]
)
def update(student_id):

    students = get_all_students()

    student_data = None

    for student in students:

        if str(student["id"]) == str(student_id):

            student_data = student

            break

    if request.method == "POST":

        updated_student = {

            "name": request.form["name"],

            "age": int(
                request.form["age"]
            ),

            "course": request.form["course"],

            "email": request.form["email"],

            "subject1": int(
                request.form["subject1"]
            ),

            "subject2": int(
                request.form["subject2"]
            ),

            "subject3": int(
                request.form["subject3"]
            )
        }

        update_student(
            student_id,
            updated_student
        )

        return redirect("/")

    return render_template(
        "update_student.html",
        student=student_data
    )
    
    
@student_bp.route("/export/csv")
def export_csv():

    students = get_all_students()

    with open(
        "exports/students_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "ID",
            "Name",
            "Age",
            "Course",
            "Email",
            "Subject1",
            "Subject2",
            "Subject3"

        ])

        for student in students:

            writer.writerow([

                student["id"],
                student["name"],
                student["age"],
                student["course"],
                student["email"],
                student["subject1"],
                student["subject2"],
                student["subject3"]

            ])

    return send_file(
        "exports/students_report.csv",
        as_attachment=True
    )
    
@student_bp.route("/export/analytics")
def export_analytics():

    highest = highest_student()

    lowest = lowest_student()

    report = pass_fail_report()

    with open(
        "exports/analytics_report.txt",
        "w"
    ) as file:

        file.write(
            "STUDENT ANALYTICS REPORT\n\n"
        )

        file.write(
            f"Highest Student: "
            f"{highest['name']}\n"
        )

        file.write(
            f"Lowest Student: "
            f"{lowest['name']}\n\n"
        )

        file.write(
            "PASS FAIL REPORT\n"
        )

        for item in report:

            file.write(
                f"{item}\n"
            )

    return send_file(
        "exports/analytics_report.txt",
        as_attachment=True
    )