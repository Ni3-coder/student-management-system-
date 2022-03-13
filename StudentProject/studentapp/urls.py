from django.urls import path
from studentapp import views

urlpatterns = [
    path('',views.home),
    path('createaccount/',views.create_account),
    path('addstudent/',views.addstudent),
    path('list/',views.list),
    path("details/<int:id>/",views.details),
    path('update/<int:id>/',views.update_student),
    path('addschool/',views.add_school),
    path('delete/<int:id>/',views.delete)

]
