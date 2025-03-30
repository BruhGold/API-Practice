import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MyChoiceSerializer, MyQuestionSerializer
from rest_framework.permissions import DjangoObjectPermissions, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import CanEditQuestion


from .models import Choice, Question

class choice_list(APIView):
    def get(self, request):
        choices = Choice.objects.all()
        serializer = MyChoiceSerializer(choices, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass

class questions_list(APIView):
    queryset = Question.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [DjangoObjectPermissions()]

    def get(self, request):
        questions = Question.objects.all()
        serializer = MyQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data["pub_date"] = datetime.datetime.now()

        serializer = MyQuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class question_detail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, CanEditQuestion]

    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = MyQuestionSerializer(question)
        return Response(serializer.data)
    
    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)

        self.check_object_permissions(request, question)
        
        serializer = MyQuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)