from django.urls import path
from . import views

urlpatterns =[
        path('teacher/', views.TeacherList.as_view()),

        path('student/', views.StudentList.as_view()),

        path('teacher/<int:pk>/',views.TeacherDetail.as_view()),
        
        path('teacher-login',views.teacher_login),

        path('teacher/change-password/<int:teacher_id>/',views.teacher_change_password),

        path('student/change-password/<int:student_id>/',views.student_change_password),

        path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),

        path('student/dashboard/<int:pk>/', views.StudentDashboard.as_view()),

        path('student-login',views.student_login),

        path('student/<int:pk>/',views.StudentDetail.as_view()),

        path('category/', views.CategoryList.as_view()),

        path('course/', views.CourseList.as_view()),

        path('search-courses/<str:searchstring>', views.CourseList.as_view()),

        path('course/<int:pk>/', views.CourseDetailView.as_view()),

        path('chapter/<int:pk>', views.ChapterDetailView.as_view()),

        path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),

        path('teacher-course/<int:teacher_id>', views.TeacherCourseList.as_view()),

        path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),

        path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),

        path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),

        path('fetch-enrolled-courses/<int:student_id>', views.EnrolledStuentList.as_view()),

        path('fetch-enrolled-students/<int:course_id>', views.EnrolledStuentList.as_view()),

        path('fetch-recomemded-coourses/<int:student_id>', views.EnrolledStuentList.as_view()),

        path('fetch-all-enrolled-students/<int:teacher_id>', views.EnrolledStuentList.as_view()),

        path('course-rating/', views.CourseRatingList.as_view()),

        path('popular-courses/', views.CourseRatingList.as_view()),

        path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),

        path('student-add-favorte-course/', views.StudentFavoriteCourseList.as_view()),

        path('student-remove-favorite-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),

        path('fetch-favorite-coourses/<int:student_id>', views.StudentFavoriteCourseList.as_view()),

        path('student-assignment/<int:teacher_id>/<int:student_id>',views.AssignmentList.as_view()),

        path('my-assignments/<int:student_id>',views.MyAssignmentList.as_view()),

        path('update-assignments/<int:pk>',views.UpdateAssignmentList.as_view()),

        path('quiz/',views.Quizlist.as_view()),

        path('teacher-quiz/<int:teacher_id>',views.TeacherQuizList.as_view()),

        path('teacher-quiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),

        path('quiz/<int:pk>', views.QuizDetailView.as_view()),

        path('quiz-questions/<int:quiz_id>', views.QuizQuestionList.as_view()),

        path('quiz-questions/<int:quiz_id>/<int:limit>', views.QuizQuestionList.as_view()),

        path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>', views.fetch_quiz_assign_status),

        path('quiz-assign-course/', views.CourseQuizList.as_view()),

        path('fetch-assigned-quiz/<int:course_id>', views.CourseQuizList.as_view()),

        path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>', views.fetch_quiz_assign_status),

        path('attempt-quiz/', views.AttempQuizList.as_view()),

        path('attempted-quiz/<int:quiz_id>', views.AttempQuizList.as_view()),

        path('quiz-questions/<int:quiz_id>/next-question/<int:question_id>', views.QuizQuestionList.as_view()),

        path('fetch-quiz-attempt-status/<int:quiz_id>/<int:student_id>', views.fetch_quiz_attempt_status),

        path('study-material/<int:course_id>', views.StudyMaterialList.as_view()),

        path('study-materials/<int:pk>', views.StudyMaterialView.as_view()),

        path('user/study-material/<int:course_id>', views.StudyMaterialList.as_view()),

        path('attempted-quiz/<int:quiz_id>', views.AttempQuizList.as_view()),

        path('fetch-quiz-result/<int:quiz_id>/<int:student_id>', views.fetch_quiz_result),

        path('update-view/<int:course_id>', views.update_view),

        path('student-test/', views.CourseRatingList.as_view()),

        path('popular-teachers/', views.TeacherList.as_view()),

        path('faq/', views.FaqList.as_view()),

        path('pages/', views.FlatPagesList.as_view()),

        path('pages/<int:pk>/<str:page_slug>', views.FlatPagesDetail.as_view()),

        path('send-message/<int:teacher_id>/<int:student_id>', views.ChatBot),

        path('get-message/<int:teacher_id>/<int:student_id>', views.MessageList.as_view()),

        path('send-group-message/<int:teacher_id>', views.GroupChatBot),

        path('fetch-my-teachers/<int:student_id>', views.MyTeacherList().as_view()),

]