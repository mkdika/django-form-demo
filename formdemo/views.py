from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from .models import Author
from .forms import AuthorForm

# Create your views here.
def authors(request):
  
  author = Author()
  author_list =  Author.objects.all()
  form = AuthorForm(initial=model_to_dict(author))

  response_dict = {
    'list':author_list,
    'form':form,
  }
    
  return render(request, 'formdemo/author.html', response_dict)