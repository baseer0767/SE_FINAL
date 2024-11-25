from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from course_instructor.models import Course, CourseContent

# def if_is_instructor(request):
#     return render(request, "if_is_instructor.html")

def main_page(request):
    # Fetch all courses
    courses = Course.objects.all()  # You can filter this as per your requirements
    return render(request, 'main_page.html', {'courses': courses})

# def course_detail(request, course_id):
#     # Get the course and its contents
#     course = get_object_or_404(Course, id=course_id)
#     course_contents = CourseContent.objects.filter(course=course)

#     context = {
#         'course': course,
#         'course_contents': course_contents,
#         'student_id': request.user.id,  # Pass user.id as student_id
#     }
#     return render(request, 'course_detail.html', context)

# def your_view(request):
#     student_id = request.user.id  # Assuming the logged-in user is the student
#     context = {'student_id': student_id}
#     return render(request, 'your_view.html', context)
