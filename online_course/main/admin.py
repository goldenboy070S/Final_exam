from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('week_day',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CourseGroup)
class CourseGroupAdmin(admin.ModelAdmin):
    list_display = ('number', 'course', 'status')
    list_filter = ('course', 'teacher')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_working', 'experience')
    list_filter = ('courses', 'experience')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_study')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('theme', 'start', 'course_group')


@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_file', 'lesson')
    list_filter = ('lesson',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'created_at') 


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson','file', 'gived_time')
    

@admin.register(StudentHomework)
class StudentHomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson_homework', 'file', 'student', 'upload_time')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'created_at')


@admin.register(StudentReaction)
class StudentReactionAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'liked_it', 'created_at', 'updated_at')