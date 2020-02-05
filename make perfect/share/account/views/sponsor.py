from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView

from django.contrib.auth import login

from ..forms import SponsorSignUpForm
from django.http import HttpResponse
from django.db.models import Q

from ..models import User, Idea
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your views here.
class SponsorSignUpView(CreateView):
    model = User
    form_class = SponsorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Sponsor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ideapeacher:idealist')

def homepage(request):
    i = idea.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))
    return render(request,"main/home.html", context={"ideas":i})
    
    
    
    