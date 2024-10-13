from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class CourseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGroup
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1
    

class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class StudentReationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReaction
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1
    

class MessageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=155)
    message = serializers.CharField()