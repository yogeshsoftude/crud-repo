from django.urls import path
from crud.views import home, Student_list, Student_info, Student_delete, index, Student_update,show,login,logout
from crud.views import Registration
urlpatterns = [
    
    path('index/',index,name='index'),
    path('registration/',Registration,name='Registration'),
    path('',home,name='home'),
    path('student/',index,name='index'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('student_info/<sid>/', Student_info, name='Student_info'),
    path('student_info/<sid>/', Student_list, name='Student_list'),
    path('student_delete/<sid>/', Student_delete, name='Student_delete'),
    path('student_update/<sid>/', Student_update, name='Student_update'),
    # path('show/',show,name=show),
    
    
]