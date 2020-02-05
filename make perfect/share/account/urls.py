from django.urls import path, include
from .import views
from django.conf.urls import url





from django.conf.urls.static import static
from django.conf import settings

from account.views import account, ideapeacher, sponsor 











urlpatterns = [

    path('', account.home, name='home'),

    path('sponsor/', include(([
        path('', sponsor.homepage, name='idealist')

    ], account), namespace='sponsor')),


    path('ideapeacher/', include(([
        path('', ideapeacher.IdeaListView.as_view(), name='ideapost')

    ], account), namespace='ideapeacher')),
    
] 


