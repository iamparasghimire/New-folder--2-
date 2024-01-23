from django.shortcuts import render
from django.views.generic import TemplateView, FormView,ListView,DetailView
from django.contrib.auth.views import LogoutView,LoginView
from .forms import ContactForm , EnrollForm,LoginForm
from django.urls import reverse_lazy
from .models import Reading, Writing, Listening, Speaking,Enroll,Contact,About,Zoom,Stories,Blog

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    template_name = "Pte/index.html"
    success_url = reverse_lazy('index')
    model = Stories
    context_object_name = 'stories'  # Specify the context variable name for the queryset

    def get_queryset(self):
        return Stories.objects.all()  # Adjust the queryset according to your needs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        context['blogs'] = Blog.objects.all()

        return context
       
    

from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from .models import About


class LoginView(LoginView, ListView):
    template_name = "Pte/login.html"
    form_class = LoginForm
    model = Stories
    context_object_name = 'stories'
    reverse_lazy = 'index'

    def get_queryset(self):
        return Stories.objects.all()

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()  # Add this line to get data about the About model
        

        return context
    




class CustomLogoutView(LogoutView):
    pass
 


    

class EnrollView(ListView,FormView):
    template_name = "Pte/enroll.html"
    form_class = EnrollForm
    success_url = reverse_lazy('enroll')
    model = Stories
    context_object_name = 'stories' 

    def get_queryset(self):
        return Stories.objects.all()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()  # Add this line to get data about the About model

        return context
    
    
    



class IntroductionView(LoginRequiredMixin,ListView):
    template_name = "Pte/introduction.html"
    model = Zoom
    context_object_name = 'zooms' 

    def get_queryset(self):
        return Zoom.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        return context




class SpeakingView(ListView):
    template_name = "Pte/speaking.html"
    model = Speaking
    context_object_name = 'speakings'

    def get_queryset(self):
        return Speaking.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        return context
    



class WritingView(ListView):
    template_name = "Pte/writing.html"
    model = Writing
    context_object_name = 'writings'

    def get_queryset(self):
        return Writing.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        return context

class ReadingView(ListView):
    template_name = "Pte/reading.html"
    model = Reading
    context_object_name = 'readings'

    def get_queryset(self):
        return Reading.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        return context
    



class ListeningView(ListView):
    template_name = "Pte/listening.html"
    model = Listening
    context_object_name = 'listenings'

    def get_queryset(self):
        return Listening.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['stories'] = Stories.objects.all()
        return context
    
    

class EnquiryView(ListView,FormView):
    template_name = "Pte/contact.html"
    form_class  =  ContactForm
    success_url = reverse_lazy('enquiry')
    model = Stories
    context_object_name = 'stories' 

    def get_queryset(self):
        return Stories.objects.all()


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()  # Add this line to get data about the About model

        return context
    
class StoryView(ListView):
    template_name = "Pte/success.html"
    model = Stories
    context_object_name = 'stories'  

    def get_queryset(self):
        return Stories.objects.all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()  # Add this line to get data about the About model

        return context

    