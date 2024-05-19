from django.contrib import admin
from . models import (
    Carousel_slider,Expert_Instructor,Contact_forms,Academy_course_Item,Faq_question
    )


# Carousel slider
@admin.register(Carousel_slider)
class Carousel_slider_admin(admin.ModelAdmin):
    list_display = ['id','header','title','sub_title','read_more_button','join_now_button','background_image']
    
# ExpertInstructor
@admin.register(Expert_Instructor)
class Expert_Instructor_admin(admin.ModelAdmin):
    list_display = ['id','instructor_name','qualification','instructor_profile_picture','fb_profile_link','linkedIn_profile_link','twitter_profile_link']
    
# Contact Form
@admin.register(Contact_forms)
class Contact_forms_admin(admin.ModelAdmin):
    list_display = ['id','name','e_mail','subjects','messages','show_review_home']
    
# Course Category and items
@admin.register(Academy_course_Item)
class Academy_course_Item_admin(admin.ModelAdmin):
    list_display = ['id','course_item','course_name','course_instructor','duration_hour','duration_day','total_student','total_review_person','course_price','discount_price','course_banner','demo_class_link_YT','course_playlist_link','popular_or_not']
    
    
# Faq 
@admin.register(Faq_question)
class Faq_question_admin(admin.ModelAdmin):
    list_display = ['question','answer','course','created_at']