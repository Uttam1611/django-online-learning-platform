from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Quiz, Question, QuizSubmission
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('course_detail', course_id=course.id)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quizzes.all()
    return render(request, 'core/course_detail.html', {'course': course, 'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.POST.get(f'question_{q.id}')
            if answer == q.correct_answer:
                score += 1
        QuizSubmission.objects.create(student=request.user, quiz=quiz, score=score)
        return render(request, 'core/quiz_result.html', {'score': score, 'total': questions.count()})
    return render(request, 'core/take_quiz.html', {'quiz': quiz, 'questions': questions})
