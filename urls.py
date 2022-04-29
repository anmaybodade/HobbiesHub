from django.contrib import admin
from django.urls import path
#for load views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('Login/',views.Login),
    path('Blog/',views.Blog),
   
    path('Register/',views.Register),
    path('AdminHome/',views.AdminHome),
    path('AddCourse/',views.AddCourse),
    path('CourseList1/',views.CourseList1),
    path('AddBatch/',views.AddBatch),
    path('NewBatchList/',views.NewBatchList),
    path('Logout/',views.Logout),
    path('StudentHome/',views.StudentHome),
    path('CourseList2/',views.CourseList2),
    path('NewBatchList2/',views.NewBatchList2),
    path('Admission/',views.Admission),
    path('BatchBooking/',views.BatchBooking),
    path('SearchProfile/',views.SearchProfile),
    path('UpdateProfile/',views.UpdateProfile),
    path('Contact/',views.Contact),
    path('Dance/',views.Dance),
    


]
