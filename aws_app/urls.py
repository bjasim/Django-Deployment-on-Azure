from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome_page, name="home"),
    # path('about/', AboutView.as_view(),name="about"),
    # path('create/', ProjectCreateView.as_view(),name="create"),
    # path('edit/<int:pk>', ProjectEditView.as_view(),name="edit"),
    # path('delete/<int:pk>', ProjectDeleteView.as_view(),name="delete"),
]