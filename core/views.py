from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student, LibraryHistory, FeesHistory
from .forms import FeesHistoryForm, LibraryHistoryForm, StudentForm
from django.contrib.auth.views import LoginView, LogoutView

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        return Student.objects.all()

class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def test_func(self):
        # Only Admin and Staff can add students
        return self.request.user.role in ['admin', 'staff']

class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def test_func(self):
        # Only Admin and Staff can edit students
        return self.request.user.role in ['admin', 'staff']

class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def test_func(self):
        # Only Admin can delete students
        return self.request.user.role == 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Are you sure you want to delete this student?"
        return context

class LibraryHistoryListView(LoginRequiredMixin, ListView):
    model = LibraryHistory
    template_name = 'library_history_list.html'
    context_object_name = 'library_history'
    paginate_by = 10

    def get_queryset(self):
        return LibraryHistory.objects.all()

class LibraryHistoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = LibraryHistory
    form_class = LibraryHistoryForm
    template_name = 'library_history_form.html'
    success_url = reverse_lazy('library_history_list')

    def test_func(self):
        # Only Admin and Librarian can add library history
        return self.request.user.role in ['admin', 'librarian']

class LibraryHistoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LibraryHistory
    form_class = LibraryHistoryForm
    template_name = 'library_history_form.html'
    success_url = reverse_lazy('library_history_list')

    def test_func(self):
        # Only Admin and Librarian can edit library history
        return self.request.user.role in ['admin', 'librarian']

class LibraryHistoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LibraryHistory
    template_name = 'library_history_confirm_delete.html'
    success_url = reverse_lazy('library_history_list')

    def test_func(self):
        # Only Admin can delete library history
        return self.request.user.role == 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Are you sure you want to delete this library history?"
        return context

class FeesHistoryListView(LoginRequiredMixin, ListView):
    model = FeesHistory
    template_name = 'fees_history_list.html'
    context_object_name = 'fees_history'
    paginate_by = 10

    def get_queryset(self):
        return FeesHistory.objects.all()

class FeesHistoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = FeesHistory
    form_class = FeesHistoryForm
    template_name = 'fees_history_form.html'
    success_url = reverse_lazy('fees_history_list')

    def test_func(self):
        # Only Admin and Staff can add fees history
        return self.request.user.role in ['admin', 'staff']

class FeesHistoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FeesHistory
    form_class = FeesHistoryForm
    template_name = 'fees_history_form.html'
    success_url = reverse_lazy('fees_history_list')

    def test_func(self):
        # Only Admin and Staff can edit fees history
        return self.request.user.role in ['admin', 'staff']

class FeesHistoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FeesHistory
    template_name = 'fees_history_confirm_delete.html'
    success_url = reverse_lazy('fees_history_list')

    def test_func(self):
        # Only Admin can delete fees history
        return self.request.user.role == 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Are you sure you want to delete this fees history?"
        return context

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')  # After login, redirect to the dashboard

# Role-Based Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        user = request.user
        # Allow superusers to access the admin dashboard
        if user.is_superuser:
            return redirect('admin_dashboard')

        # Redirect based on the user's role
        if hasattr(user, 'role'): 
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'staff':
                return redirect('staff_dashboard')
            elif user.role == 'librarian':
                return redirect('library_dashboard')
        else:
            return redirect('login') 
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard.html'

class StaffDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'staff_dashboard.html'

class LibrarianDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'library_dashboard.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

