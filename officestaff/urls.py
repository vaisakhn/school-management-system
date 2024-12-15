from django.urls import path,include
from officestaff import views

urlpatterns = [
    path('staff-login/',views.StaffLoginView.as_view(),name="staff-login"),
]
