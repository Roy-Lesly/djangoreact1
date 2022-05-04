from django.urls import path
from .views import RadiDeptList, RadiDeptDetail     # radi_dept_list, radi_dept_detail

app_name = 'api'

urlpatterns = [
    #path('deptList/', radi_dept_list),
    #path('deptDetail/<int:pk>', radi_dept_detail) # detail, update, delete
    path('deptList/', RadiDeptList.as_view()),
    path('deptDetail/<int:id>', RadiDeptDetail.as_view()) # detail, update, delete
]