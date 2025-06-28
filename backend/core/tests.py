from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Course, Enrollment, Quiz, Question, QuizSubmission

class CourseModelTest(TestCase):
    def test_create_course(self):
        user = User.objects.create_user(username='instructor', password='pass')
        course = Course.objects.create(title='Test Course', description='A test', instructor=user)
        self.assertEqual(course.title, 'Test Course')

class EnrollmentTest(TestCase):
    def test_enroll_student(self):
        instructor = User.objects.create_user(username='instructor', password='pass')
        student = User.objects.create_user(username='student', password='pass')
        course = Course.objects.create(title='Course', description='desc', instructor=instructor)
        enrollment = Enrollment.objects.create(student=student, course=course)
        self.assertEqual(enrollment.student.username, 'student')
        self.assertEqual(enrollment.course.title, 'Course')

class QuizTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username='instructor', password='pass')
        self.student = User.objects.create_user(username='student', password='pass')
        self.course = Course.objects.create(title='Course', description='desc', instructor=self.instructor)
        self.quiz = Quiz.objects.create(course=self.course, title='Quiz 1')
        self.q1 = Question.objects.create(quiz=self.quiz, text='2+2?', correct_answer='4')

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Quiz 1')
        self.assertEqual(self.quiz.questions.count(), 1)

    def test_take_quiz_and_score(self):
        self.client.login(username='student', password='pass')
        response = self.client.post(f'/quiz/{self.quiz.id}/take/', {
            f'question_{self.q1.id}': '4'
        })
        self.assertContains(response, 'Your score: 1 out of 1')
        self.assertTrue(QuizSubmission.objects.filter(student=self.student, quiz=self.quiz).exists())

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.instructor = User.objects.create_user(username='instructor', password='pass')
        self.student = User.objects.create_user(username='student', password='pass')
        self.course = Course.objects.create(title='Course', description='desc', instructor=self.instructor)
        self.quiz = Quiz.objects.create(course=self.course, title='Quiz 1')
        self.q1 = Question.objects.create(quiz=self.quiz, text='2+2?', correct_answer='4')

    def test_course_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.title)

    def test_course_detail_view(self):
        response = self.client.get(f'/course/{self.course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.title)
        self.assertContains(response, self.quiz.title)

    def test_enroll_view_requires_login(self):
        response = self.client.post(f'/course/{self.course.id}/enroll/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_enroll_view(self):
        self.client.login(username='student', password='pass')
        response = self.client.post(f'/course/{self.course.id}/enroll/')
        self.assertEqual(response.status_code, 302)  # Redirect after enroll
        self.assertTrue(Enrollment.objects.filter(student=self.student, course=self.course).exists())

    def test_take_quiz_view_requires_login(self):
        response = self.client.get(f'/quiz/{self.quiz.id}/take/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_take_quiz_view(self):
        self.client.login(username='student', password='pass')
        response = self.client.get(f'/quiz/{self.quiz.id}/take/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.quiz.title)
        self.assertContains(response, self.q1.text)
