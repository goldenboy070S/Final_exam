from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('courses', CoursesViewSet)
router.register('days', DaysViewSet)
router.register('courseGroups', CourseGroupViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('lessons', LessonViewSet)
router.register('lessonVideos', LessonVideoViewSet)
router.register('homeworks', HomeworkViewSet)
router.register('studentHomeworks', StudentHomeworkViewSet)
router.register('comments', CommentViewSet)
router.register('reactions', StudentReactionViewset)

urlpatterns = router.urls