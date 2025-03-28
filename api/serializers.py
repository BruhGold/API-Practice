from rest_framework import serializers
from .models import Choice, Question

class MyChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class MyQuestionSerializer(serializers.ModelSerializer):
    choice_set = MyChoiceSerializer(many=True, required=False)
    pub_date = serializers.DateTimeField(required=False)
    
    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date", "choice_set"]