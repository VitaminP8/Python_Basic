from django.shortcuts import render
from .models import User, Category, Goal
from datetime import timedelta
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import GoalForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test


def index_view(request):
    # animals = Animal.objects.all().select_related('category')
    # animals = Animal.objects.all().prefetch_related('category__foods')
    users = User.objects.all()
    # goals = Goal.objects.all().selected_related('user').perfetch_realted('categories')
    return render(request, 'mainapp/index.html', {'users': users})


class CategoryListView(UserPassesTestMixin, ListView):
    model = Category
    template_name = "category_list"
    context_object_name = "categories"

    def test_func(self):
        return self.request.user.is_authenticated


class GoalListView(UserPassesTestMixin, ListView):
    model = Goal
    template_name = "goal_list"
    context_object_name = "goals"

    def test_func(self):
        return self.request.user.is_authenticated

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    # template_name = "goal_form"
    form_class = GoalForm
    success_url = '/goal-list/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print("****")
        print(self.request.user.username)
        print("****")
        return super().form_valid(form)


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    # template_name = "goal_delete"
    context_object_name = "goal"
    success_url = '/goal-list/'

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    # template_name = "goal_form"
    success_url = '/goal-list/'


class GoalDetailView(LoginRequiredMixin, DetailView):
    model = Goal
    # template_name = "goal_detail"
    context_object_name = "goal"