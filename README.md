## Student_project_tracker
Title: Student Project Tracking Application

In many educational institutions, managing and tracking student projects can become cumbersome, especially when projects are group-based. Faculty members need a system to store student details, project details, and monitor the progress of each project.

The Student Project Tracking Application will allow administrators and faculty to:

✅ Add student details (name, email, department, etc.)✅ Create and manage project details (title, description, start and end dates, status)✅ Assign multiple students to a project (many-to-many relationship)✅ Track the project progress with status updates

🏗️ Installation and Setup

1️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

2️⃣ Install Dependencies

pip install django

3️⃣ Check Django Version

django-admin --version

🚀 Project Setup

✅ Create a new Django project and app

django-admin startproject student_project_tracker
cd student_project_tracker
python manage.py startapp projects

✅ Register the app in settings.py

📦 Database Models

✅ Define models in projects/models.py

✅ Apply Migrations

python manage.py makemigrations
python manage.py migrate

🛠️ Admin Registration

✅ Register models in projects/admin.py

✅ Run the server and access the admin panel:

python manage.py createsuperuser
python manage.py runserver

Visit: http://127.0.0.1:8000/admin/ to manage students and projects.

🚀 Running the Application

1️⃣ Run migrations:

python manage.py makemigrations
python manage.py migrate

2️⃣ Start the server:

python manage.py runserver

3️⃣ Open http://127.0.0.1:8000/ in your browser.

🏁 Conclusion

This Django-based Student Project Tracking Application helps institutions efficiently manage student projects, allowing faculty to track progress in real time.
