# 🎓 Student Analytics Dashboard (Flask)

A modern Student Management and Analytics Dashboard built using Flask.

This application helps manage student records efficiently while providing insightful analytics and exportable reports through a clean and responsive web interface.

---

# 🚀 Features

## 📚 Student Management
- Add new student records
- Update existing student details
- Delete student records
- Search students instantly

## 📊 Analytics Dashboard
- Highest scoring student
- Lowest scoring student
- Course-wise average marks
- Pass/Fail analysis
- Student average calculations

## 📁 Export Reports
- Export student data as CSV
- Export analytics report as TXT

## 🎨 Frontend Features
- Responsive user interface
- Dynamic student cards
- Search functionality
- Form validation
- Clean dashboard design

---

# 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Jinja2
- JSON

---

# 📂 Project Structure

```bash
project/
│
├── app.py
│
├── data/
│   └── students.json
│
├── exports/
│   ├── students_report.csv
│   └── analytics_report.txt
│
├── preview/
│   ├── Preview_dashboard.png
│   └── preview_analytics_dashboard.png
│
├── routes/
│   └── student_routes.py
│
├── services/
│   ├── file_service.py
│   ├── student_service.py
│   └── analytics_service.py
│
├── static/
│   ├── style.css
│   └── app.js
│
├── templates/
│   ├── students.html
│   ├── analytics.html
│   └── update_student.html
│
├── requirements.txt
│
└── README.md
```

---

# 🖥️ Dashboard Preview

## Student Dashboard

![Dashboard](preview/Preview_dashboard.png)

---

## Analytics Dashboard

![Analytics Dashboard](preview/preview_analytics_dashboard.png)

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
```

## 2️⃣ Navigate to Project Folder

```bash
cd student-analytics-dashboard-flask
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Flask Application

```bash
python app.py
```

---

# 🌐 Access the Application

Open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

# 📈 Future Improvements

- Database integration (MySQL/PostgreSQL)
- Authentication system
- Charts and visual analytics
- REST API support
- Docker deployment

---

# 👨‍💻 Author

Developed as a Flask + Data Analytics practice project to strengthen backend development and analytics skills.
