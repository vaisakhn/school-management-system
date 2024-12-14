from django.urls import path
from officestaff import views

urlpatterns = [
    path('staff-login/',views.StaffLoginView.as_view(),name="staff-login"),
]
