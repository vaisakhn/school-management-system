from django.urls import path,include
from Admin import views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name='user-register'),
    path('admin-login/',views.AdminLoginView.as_view(),name="admin-loggin"),
    path('staff-login/',views.StaffLoginView.as_view(),name="staff-login"),
    path('librarian-login/',views.LibrarianLoginView.as_view(),name="librarian-login")
]
