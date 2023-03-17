from rest_framework import serializers
from . import models
from django.contrib.flatpages.models import FlatPage


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id','full_name','email','password','qualification','mobile_no','skills','profile_img','teacher_courses','skill_list','total_teacher_course','face_url','insta_url','twit_url','web_url','you_url']
    def __init__(self, *args, **kwargs):
            super(TeacherSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory
        fields=['id','title','description','total_courses']
    def __init__(self, *args, **kwargs):
            super(CategorySerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Course
        fields=['id','category','teacher','title','description','featured_img','techs','course_chapters','related_videos','teach_list','total_enrolled_students','course_rating']
    def __init__(self, *args, **kwargs):
            super(CourseSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class ChapterSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.Chapter
            fields=['id','course','title','description','video','remarks']
        def __init__(self, *args, **kwargs):
            super(ChapterSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=['id','fullname','email','password','username','interseted_categories','profile_img']
    def __init__(self, *args, **kwargs):
            super(StudentSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class StudentCourseEnrollSerializer(serializers.ModelSerializer):        
        class Meta:
            model=models.StudentCourseEnrollment
            fields='__all__'
        def __init__(self, *args, **kwargs):
            super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2
            

class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.StudentFavoriteCourse
            fields=['id','course','student','status']
        def __init__(self, *args, **kwargs):
            super(StudentFavoriteCourseSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class CourseRatingSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.CourseRating
            fields=['id','course','student','rating','reviews','review_time']
        def __init__(self, *args, **kwargs):
            super(CourseRatingSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_course','total_teacher_chapters','total_teacher_students']

class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentAssignment
        fields=['id','teacher','student','title','detail','student_status','add_time']
    def __init__(self, *args, **kwargs):
            super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=['enrolled_courses','favorite_courses','complete_assignments','pending_assignments']
        def __init__(self, *args, **kwargs):
            super(StudentDashboardSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Quiz
        fields=['id','teacher','title','detail','assign_status','add_time']
        def __init__(self, *args, **kwargs):
            super(QuizSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.QuizQuestions
        fields=['id','quiz','questions','ans1','ans2','ans3','ans4','right_ans']
        def __init__(self, *args, **kwargs):
            super(QuestionSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseQuiz
        fields=['id','teacher','course','quiz','add_time']
    def __init__(self, *args, **kwargs):
        super(CourseQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class AttempQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AttemptQuiz
        fields=['id','student','quiz','question','right_ans','add_time']
    def __init__(self, *args, **kwargs):
        super(AttempQuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class StudyMaterialSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.StudyMaterial
            fields=['id','course','title','description','upload','remarks']

        def __init__(self, *args, **kwargs):
            super(StudyMaterialSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 2

class FaqSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.Faq
            fields=['question','answer']

class FlatPageSerializer(serializers.ModelSerializer):
    class Meta :
        model=FlatPage
        fields=['id','title','content','url']

class TeacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta :
        model=models.TeacherStudentChat
        fields=['id','teacher','student','msg_from','msg_to','msg_time']
        def __init__(self, *args, **kwargs):
            super(TeacherStudentChatSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
                print('Method is POST')
                self.Meta.depth = 0
                print(self.Meta.depth)
            else:
                print(f"Method is - {request.method}")
                self.Meta.depth = 3

        def to_representation(self,instance):
            representation=super(TeacherStudentChatSerializer, self).to_representation(instance)
            representation['msg_time']=instance.msg_time.strftime("%Y-%m-%d %H:%M")
            return representation