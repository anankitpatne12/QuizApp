from django.urls import path
from main_app.views import QuizCreateView, QuizActiveView, QuizResultView, QuizAllView

app_name = 'main_app'

urlpatterns = [
    path('quizzes/', QuizCreateView.as_view(), name='quizzes_create'),  # create quiz
    path('quizzes/active/<int:pk>/', QuizActiveView.as_view(), name='quizzes_active'),  # get active quiz
    path('quizzes/<int:pk>/result/', QuizResultView.as_view(), name='quizzes_result'),  # get quiz result
    path('quizzes/all/', QuizAllView.as_view(), name='quizzes_all'),   # get all quizzes
    # path('quiz/', quiz_view, name='quiz'),
]
