from django.db import models
from django.core import serializers

class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True,null=True)
    qualification=models.CharField(max_length=500)
    mobile_no=models.CharField(max_length=20)
    profile_img=models.ImageField(upload_to='teacher_profile_imgs/',null=True)
    skills=models.CharField(max_length=20,null=True)

    face_url=models.URLField(null=True)
    insta_url=models.URLField(null=True)
    twit_url=models.URLField(null=True)
    web_url=models.URLField(null=True)
    you_url=models.URLField(null=True)

    class Meta:
        verbose_name_plural="1. Teacher"

    def skill_list(self):
        skill_list=self.skills.split(',')
        return skill_list

    def total_teacher_course(self):
        total_course=Course.objects.filter(teacher=self).count()
        return total_course

    def total_teacher_chapters(self):
        total_chapters=Chapter.objects.filter(course__teacher=self).count()
        return total_chapters

    def total_teacher_students(self):
        total_students=StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_students 

class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    class Meta:
        verbose_name_plural="2. Course Categories"

    def total_courses(self):
        return Course.objects.filter(category=self).count()

    def __str__(self) :
        return self.title

class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE, related_name='category_courses')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='teacher_courses')
    title=models.CharField(max_length=150)
    description=models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/',null=True)
    techs=models.TextField(null=True)
    course_views=models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural="3. Courses"

    def related_videos(self):
        related_videos=Course.objects.filter(techs__icontains=self.techs).exclude(id=self.id)
        return serializers.serialize('json',related_videos)

    def teach_list(self):
        teach_list=self.techs.split(',')
        return teach_list

    def total_enrolled_students(self):
        total_enrolled_students=StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_students

    def course_rating(self):
        course_rating=CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']
    
    def __str__(self) :
        return self.title

class Chapter(models.Model):
    course=models.ForeignKey(Course,null=True,on_delete=models.CASCADE,related_name='course_chapters')
    title=models.CharField(max_length=150,null=True)
    description=models.TextField()
    video=models.FileField(upload_to='chapter_videos/',null=True)
    remarks=models.TextField(null=True)

    class Meta:
        verbose_name_plural="4. Chapters"


class Student(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=500)
    interseted_categories=models.TextField()
    profile_img=models.ImageField(upload_to='student_profile_imgs/',null=True)

    def __str__(self) :
        return self.fullname

    def enrolled_courses(self):
        enrolled_courses=StudentCourseEnrollment.objects.filter(student=self).count()
        return enrolled_courses

    def favorite_courses(self):
        favorite_courses=StudentFavoriteCourse.objects.filter(student=self).count()
        return favorite_courses

    def complete_assignments(self):
        complete_assignments=StudentAssignment.objects.filter(student=self,student_status=True).count()
        return complete_assignments

    def pending_assignments(self):
        pending_assignments=StudentAssignment.objects.filter(student=self,student_status=False).count()
        return pending_assignments

    class Meta:
        verbose_name_plural="5. Students"

class StudentCourseEnrollment(models.Model):
    course=models.ForeignKey(Course,null=True,on_delete=models.CASCADE,related_name='enrolled_courses')
    student=models.ForeignKey(Student,null=True,on_delete=models.CASCADE,related_name='enrolled_student')
    enrolled_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="6. Enrolled Courses"

    def __str__(self) :
        return f"{self.course}-{self.student}"

class CourseRating(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    rating=models.PositiveBigIntegerField(default=0)
    reviews=models.TextField(null=True)
    review_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="7. Course Ratings"

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"

class StudentFavoriteCourse(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    class Meta:
         verbose_name_plural="8. Student Favorite Course"

class StudentAssignment(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=150)
    detail=models.TextField(null=True)    
    student_status=models.BooleanField(default=False,null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="9. STudent Assignment"

    def __str__(self):
        return f"{self.title}" 
        
class Quiz(models.Model):   
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    class Meta:
         verbose_name_plural="11. Quizs"

class QuizQuestions(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    questions=models.CharField(max_length=200)
    ans1=models.CharField(max_length=200)
    ans2=models.CharField(max_length=200)
    ans3=models.CharField(max_length=200)
    ans4=models.CharField(max_length=200)
    right_ans=models.CharField(max_length=200)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="12. Quiz Question&answer "

class CourseQuiz(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="13. Course Quiz "

class AttemptQuiz(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,null=True)
    right_ans=models.CharField(max_length=200,null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="14. Attempted Questions "

class StudyMaterial(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    upload=models.FileField(upload_to='study_materials/',null=True)
    remarks=models.TextField(null=True)

    class Meta:
         verbose_name_plural="15. Course Materials"

class Faq(models.Model):
    question=models.CharField(max_length=300)
    answer=models.TextField()

    class Meta:
         verbose_name_plural="16. FAQ "

class TeacherStudentChat(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    msg_to=models.TextField()
    msg_from=models.CharField(max_length=100)
    msg_time=models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural="17. ChatBot "