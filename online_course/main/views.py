from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.core.mail import send_mail
from online_course.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
# Create your views here.


class DaysViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaysSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class CourseGroupViewSet(ModelViewSet):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['theme']


class LessonVideoViewSet(ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
  

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class HomeworkViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class StudentHomeworkViewSet(ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class StudentReactionViewset(ModelViewSet):
    queryset = StudentReaction.objects.all()
    serializer_class = StudentReationSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]


class MessageView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_mail(
            subject=serializer.validated_data.get('title'),
            message=serializer.validated_data.get('message'),
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email for user in User.objects.all() if user.email],
            fail_silently=False,
        )
        return Response('Message sent successfully')
    



