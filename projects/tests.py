# projects/tests.py
from django.test import TestCase
from .models import Project, Student  # Import your models
from django.urls import reverse

class ProjectTests(TestCase):

    def setUp(self):
        # Create some test data (projects and students)
        self.student1 = Student.objects.create(name="Alice", email="alice@example.com", department="CS", enrollment_number="1")
        self.student2 = Student.objects.create(name="Bob", email="bob@example.com", department="EE", enrollment_number="2")

        self.project1 = Project.objects.create(title="Project A", description="Description A", start_date="2024-01-01", end_date="2024-06-01")
        self.project1.students.add(self.student1)  # Add student to project

        self.project2 = Project.objects.create(title="Project B", description="Description B", start_date="2024-02-01", end_date="2024-07-01")
        self.project2.students.add(self.student1, self.student2)

    def test_project_list_view(self):
        # Test the project list view
        response = self.client.get(reverse('project_list'))  # Replace 'project_list' with your URL name
        self.assertEqual(response.status_code, 200)  # Check if the response is successful (200 OK)

        # Check if project titles are present in the response (adapt to your HTML)
        self.assertContains(response, "Project A")
        self.assertContains(response, "Project B")

        # Check if student names are present (adapt to your HTML)
        self.assertContains(response, "Alice")
        self.assertContains(response, "Bob")

        #Check table headers are present
        self.assertContains(response, "No.")
        self.assertContains(response, "Project Name")
        self.assertContains(response, "Students")


    def test_project_model_str(self):
        # Test the __str__ method of the Project model
        self.assertEqual(str(self.project1), "Project A")  # Should return the project title

    def test_no_projects_message(self):
        # Delete all projects to test the "no projects" message
        Project.objects.all().delete()
        response = self.client.get(reverse('project_list'))
        self.assertContains(response, "No projects yet.")  # Or whatever your message is