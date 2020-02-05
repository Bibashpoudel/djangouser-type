from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

from ..forms import IdeapeacherSignUpForm

from ..models import User, Idea

from django.views.generic import CreateView, ListView
from  ..decorator import ideapeacher_required

class IdeapeacherSignUpView(CreateView):
    model = User
    form_class = IdeapeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Idea Peacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ideapeacher:ideapost')

@method_decorator([login_required, ideapeacher_required], name='dispatch')
class IdeaListView(ListView):
    model = Idea
    ordering = ('title', )
    context_object_name = 'ideas'
    template_name = 'account/ideapeacher/ideapost.html'

    def get_queryset(self):
        queryset = self.request.user.ideas.all()
            
        return queryset