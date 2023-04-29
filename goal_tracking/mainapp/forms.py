import requests
from django import forms

from .models import Goal, Category, User


class GoalForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "тема",
            'class': 'form-control'
        }
    ))

    description = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'описание',
            'class': 'form-control'
        }
    ))

    deadline = forms.DateField(widget=forms.SelectDateWidget(
        attrs={
            'placeholder': 'дедлайн',
            'class': 'special'
        }
    ))

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': "special"}
    ))

    class Meta:
        model = Goal
        # fields = '__all__'
        # fields = ('name', 'foods')
        exclude = ('is_active', 'started_at', 'lateness', 'user')

