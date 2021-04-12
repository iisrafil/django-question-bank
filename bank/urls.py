from django.urls import path

from bank.views import home, course_details, all_courses, my_courses, question_list

urlpatterns = [
    path('', home, name='home'),
    path('all-course/', all_courses, name='all-courses'),
    path('my-course/', my_courses, name='my-courses'),
    path('details/<int:pk>/', course_details, name='detail'),
    path('question/<int:pk>/', question_list, name='question_list'),
]
