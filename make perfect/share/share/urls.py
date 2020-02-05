from django.urls import include, path
from django.contrib import admin

from account.views import sponsor, ideapeacher, account

urlpatterns = [

    path('', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', account.SignUpView.as_view(), name='signup'),
    path('accounts/signup/sponsor/', sponsor.SponsorSignUpView.as_view(), name='sponsor_signup'),
    path('accounts/signup/idepeacher/', ideapeacher.IdeapeacherSignUpView.as_view(), name='ideapeacher_signup'),


    path('admin/', admin.site.urls),
]
