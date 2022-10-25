from django.urls import path
from .import views

urlpatterns = [
    path("",views.Employee_Form,name='employee_insert'),
    path('<int:id>/', views.Employee_Form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.Employee_Delete,name='employee_delete'),
    path("list/",views.Employee_List,name="Employee_List"),
]