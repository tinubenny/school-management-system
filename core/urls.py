from django.urls import path
from .views import (StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
                    LibraryHistoryListView, LibraryHistoryCreateView, LibraryHistoryUpdateView, LibraryHistoryDeleteView,
                    FeesHistoryListView, FeesHistoryCreateView, FeesHistoryUpdateView, FeesHistoryDeleteView, 
                    CustomLoginView, CustomLogoutView,  DashboardView, AdminDashboardView, StaffDashboardView, LibrarianDashboardView)

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreateView.as_view(), name='add_student'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='edit_student'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),

    path('library-history/', LibraryHistoryListView.as_view(), name='library_history_list'),
    path('library-history/add/', LibraryHistoryCreateView.as_view(), name='library_history_add'),
    path('library-history/<int:pk>/edit/', LibraryHistoryUpdateView.as_view(), name='edit_library_history'),
    path('library-history/<int:pk>/delete/', LibraryHistoryDeleteView.as_view(), name='delete_library_history'),

    path('fees-history/', FeesHistoryListView.as_view(), name='fees_history_list'),
    path('fees-history/add/', FeesHistoryCreateView.as_view(), name='add_fees_history'),
    path('fees-history/<int:pk>/edit/', FeesHistoryUpdateView.as_view(), name='edit_fees_history'),
    path('fees-history/<int:pk>/delete/', FeesHistoryDeleteView.as_view(), name='delete_fees_history'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

     path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Role-based dashboards
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/staff/', StaffDashboardView.as_view(), name='staff_dashboard'),
    path('dashboard/librarian/', LibrarianDashboardView.as_view(), name='library_dashboard'),
]
