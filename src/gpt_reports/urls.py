from django.urls import path

from .api import views

urlpatterns = [
    path("report/", view=views.GPTReport.as_view()),
]
