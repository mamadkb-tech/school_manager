from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="list"),
    path("new/", views.student_create, name="create"),
    path("<int:id>/", views.student_detail, name="detail"),
    path("<int:id>/edit/", views.student_update, name="update"),
    path("<int:id>/delete/", views.student_delete, name="delete"),
    path("classe/<str:classe>/", views.students_by_class, name="by_class"),
]
