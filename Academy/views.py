from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from . models import Carousel_slider,Contact_forms,Academy_course_Item,Faq_question
from . forms import Contact_form,SignUp
from django.db.models import Q
from django.core.paginator import Paginator


# HomePage
def Home(request):
    slider = Carousel_slider.objects.all()
    context = {
        'slider':slider,
    }
    return render(request,'Academy/home.html',context)
    
    
# Contact page
def Contact(request):
    form = Contact_form
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            name_data = form.cleaned_data['name']
            name_email = form.cleaned_data['email']
            name_subjects = form.cleaned_data['subjects']
            name_messages = form.cleaned_data['textbox']
            Contact_forms(
                name=name_data,
                e_mail=name_email,
                subjects=name_subjects,
                messages=name_messages
            ).save()
            context = {
                'form_submitted':True,
                'form':form
            }
            return render(request,'Academy/home.html',context)
    else:
        form = Contact_form()
        return render(request,'Academy/Contact.html',{'form':form})
    

# Registration page
class Registration(View):
    def get(self,request):
        form = SignUp()
        return render(request, 'Academy/signup.html', {'form':form})
    def post(self,request):
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Academy/signup.html', {'form':form,'signup_done':True})
        else:
            return render(request, 'Academy/signup.html', {'form':form})
    
    
    
# academic program page
def Academic_program(request):
    academic = Academy_course_Item.objects.filter(course_item='Academic')
    # pagination
    paginator = Paginator(academic,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_total = page_obj.paginator.num_pages
    return render(request, 'Academy/academic.html',{'academic':page_obj,'page_total':[n+1 for n in range(page_total)]})


# skills development program page
def skills_development(request):
    skill_dev = Academy_course_Item.objects.filter(course_item='Skill Development')
    # pagination
    paginator = Paginator(skill_dev,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_total = page_obj.paginator.num_pages
    context = {
        'skill_dev':page_obj,
        'page_total':[n+1 for n in range(page_total)]
    }
    return render(request, 'Academy/skills.html',context)


# course details page
class CourseDetails(View):
    def get(self,request,pk):
        course = Academy_course_Item.objects.get(pk=pk)
        accordion  = Faq_question.objects.filter(Q(course=course))
        return render(request, 'Academy/course_details.html',{'course':course,'accordion':accordion})


# Error 404 page
def Error(request):
    return render(request, 'Academy/error404.html')