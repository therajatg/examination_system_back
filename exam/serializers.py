from .models import Exam, Question
from rest_framework import serializers

class ExamSerializer(serializers.ModelSerializer):
	class Meta:
		model=Exam
		fields="__all__"


class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Question
		fields="__all__"