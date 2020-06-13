from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from main import models, forms
# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'

class Question(SingleObjectMixin, FormView):
    model = models.Question
    template_name = 'main/question.html'
    form_class = forms.AnswerForm

    def form_valid(self, form):
        return HttpResponseRedirect('/')

    
