from django.urls import path
from librarian import views

urlpatterns = [
    path('librarian-login/',views.LibrarianLoginView.as_view(),name="librarian-login")
]
