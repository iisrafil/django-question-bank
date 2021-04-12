from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from bank.models import Category, SubCategory, Question


def home(request):
    courses = Category.objects.all()[:15]

    context = {
        'courses': courses,
    }
    return render(request, 'bank/home.html', context)


def all_courses(request):
    courses = Category.objects.all()
    paginator = Paginator(courses, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'All Courses',
        'courses': page_obj,
    }
    return render(request, 'bank/courses.html', context)


def my_courses(request):
    courses = request.user.profile.mycourses_set.all()

    context = {
        'title': 'My Courses',
        'courses': courses,
    }
    return render(request, 'bank/my_courses.html', context)


def course_details(request, pk):
    course = get_object_or_404(Category, pk=pk)

    SubCatagorys = SubCategory.objects.filter(category=course)

    context = {
        'course': course,
        'SubCatagorys': SubCatagorys,
    }
    return render(request, 'bank/details.html', context)


def question_list(request, pk):
    SubCatagory = get_object_or_404(SubCategory, pk=pk)
    questions = Question.objects.filter(category=SubCatagory)

    context = {
        'course': SubCatagory.category,
        'SubCatagory': SubCatagory,
        'questions': questions,
    }
    return render(request, 'bank/question_view.html', context)

