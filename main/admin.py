from django.contrib import admin
from . import models

admin.site.register(models.Teacher)

admin.site.register(models.CourseCategory)

admin.site.register(models.Course)

admin.site.register(models.Chapter)

admin.site.register(models.Student)

admin.site.register(models.StudentCourseEnrollment)

admin.site.register(models.CourseRating)

admin.site.register(models.StudentFavoriteCourse)

admin.site.register(models.StudentAssignment)

admin.site.register(models.Quiz)

admin.site.register(models.CourseQuiz)

admin.site.register(models.QuizQuestions)

admin.site.register(models.AttemptQuiz)

admin.site.register(models.StudyMaterial)

admin.site.register(models.Faq)

admin.site.register(models.TeacherStudentChat)