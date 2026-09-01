from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='department')
router.register('teachers', TeacherViewSet, basename='teacher')
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls
