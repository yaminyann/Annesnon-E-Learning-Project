from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . forms import Login
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.Home, name='home'),
    path('about/',TemplateView.as_view(template_name="Academy/About.html"), name='about'),
    path('contact/',views.Contact, name='contact'),
    path('courses/',TemplateView.as_view(template_name="Academy/Courses.html"), name='courses'),
    path('academic/',views.Academic_program, name='academic'),
    path('skills/',views.skills_development, name='skills'),
    path('details/<int:pk>/',views.CourseDetails.as_view(), name='details'),
    path('error404/',views.Error, name='error'),
    # SignUp and login
    path('signup/',views.Registration.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Academy/login.html', authentication_form=Login, ), name='login'),
    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)