from django.shortcuts import render
from django.urls import reverse_lazy

##class based basic gritty way
##
from django.views.generic import (View, TemplateView,ListView, 
                                  DetailView, CreateView, 
                                  UpdateView, DeleteView)
from . import models

#from django.http import HttpResponse


# Create your views here.


class SchoolListView(ListView):
    
    ##changes from school_list to what you want
    ##
    context_object_name = 'schools'
    
    ##school_list
    ##
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'



class IndexView(TemplateView):
    template_name = 'index.html'
    
    ##required syntax
    ##**key word arguements
    ##
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    
    ##once you delete go back to list of schools
    ##
    success_url = reverse_lazy("basic_app:list")


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

