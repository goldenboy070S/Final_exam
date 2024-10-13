from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Day(models.Model):
    """Hafta kunlari"""
    week_day = models.CharField(max_length=15)

    def __str__(self):
        return self.week_day


class Course(models.Model):
    """kurslar"""
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

STATUS = [
    ('continue', 'Davom etmoqda'),
    ('stopped', 'Toxtatilgan'),
    ('not_started', 'Boshlanmagan'),
    ('finished', 'Yakunlangan'),
]


class CourseGroup(models.Model):
    """guruhlar"""
    number = models.CharField(max_length=5, help_text="Guruh raqami. M: FN21")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    time_lesson = models.TimeField()
    days = models.ManyToManyField(Day)
    status = models.CharField(max_length=16, choices=STATUS)

    def __str__(self):
        return self.number


class Teacher(models.Model):
    """ustozlar"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(CourseGroup)
    experience = models.IntegerField(default=1)
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Student(models.Model):
    """oquvchilar"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(CourseGroup)
    is_study = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name


class Lesson(models.Model):
    """dars"""
    course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255, help_text="dars mavzusi")

    def __str__(self) -> str:
        return self.theme


class LessonVideo(models.Model):
    """dars videosi"""
    name = models.CharField(max_length=155)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='lesson/videos/', validators=[FileExtensionValidator(['mp4', 'avi'])])

    def __str__(self) -> str:
        return self.name
    

class Attendance(models.Model):
    """Davomant"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student.user.first_name} - {self.lesson.theme}"


class Homework(models.Model):
    """uy vazifa qoshish"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    gived_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    file = models.FileField(upload_to='lesson/homework/', null=True, blank=True)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.lesson.theme
    

class StudentHomework(models.Model):
    """uy vazifa yuklash"""
    lesson_homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    file = models.FileField(upload_to='student/homework', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.student.user.first_name} - {self.lesson_homework.lesson.theme}"


class Comment(models.Model):
    """oquvchilarning izohlari"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.student.user.first_name} - {self.lesson.theme}"
    

class StudentReaction(models.Model):
    """oquvchilarning darsga bolgan reaksiyalari"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    liked_it = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.student.user.first_name} - {self.lesson.theme} - {self.liked_it}"