from django.shortcuts import render
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer


# def quiz_view(request):
#     active_quiz = Quiz.active_quiz_objects.get_active_quiz()
#     return render(request, 'main_app/index.html', {'quiz': active_quiz})



class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizActiveView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(status='active')

class QuizResultView(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(status='finished')
    serializer_class = QuizSerializer

class QuizAllView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


