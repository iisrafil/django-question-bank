from django.db import models

from users.models import Profile


class Category(models.Model):
    course_code = models.CharField(max_length=30)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_code


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='questions')


class MyCourses(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    my_course = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.user.username} {self.my_course.course_name} '
