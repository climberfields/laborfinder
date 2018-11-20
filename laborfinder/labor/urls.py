from django.urls import path
from . views import Contractor, Contractor_detail

urlpatterns = [
    path('', Contractors.as_view()),
    path('<int:pk>/', Contractor_detail.as_view())
]