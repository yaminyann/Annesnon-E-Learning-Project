from . models import Expert_Instructor
from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import Academy_course_Item,Faq_question,Contact_forms
from django.core.paginator import Paginator



def ExpertInstructor_details(request):
    instructor_details = Expert_Instructor.objects.all()
    reviews = Contact_forms.objects.filter(show_review_home=True)
    return {'instructor':instructor_details,'reviews':reviews}


def popular_course(request):
    popular_course = Academy_course_Item.objects.filter(popular_or_not=True)
    # pagination
    paginator = Paginator(popular_course,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_total = page_obj.paginator.num_pages
    return {'popular_course':page_obj,'page_total':[n+1 for n in range(page_total)]}


def CountCourse(request):
    academic = len(Academy_course_Item.objects.filter(course_item='Academic'))
    skill = len(Academy_course_Item.objects.filter(course_item='Skill Development'))
    others = len(Academy_course_Item.objects.filter(course_item='Others'))
    context = {
        'academic':academic,
        'skill':skill,
        'others':others,
    }
    return context
