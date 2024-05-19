from django.db import models


# carousel slider
class Carousel_slider(models.Model):
    header = models.CharField(max_length=150,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    sub_title = models.CharField(max_length=500,blank=True,null=True)
    read_more_button = models.CharField(max_length=200,blank=True,null=True)
    join_now_button = models.CharField(max_length=200,blank=True,null=True)
    background_image = models.ImageField(upload_to='carousel_slider')


# Expert Instructor show
class Expert_Instructor(models.Model):
    instructor_name = models.CharField(max_length=25)
    qualification = models.CharField(max_length=75)
    instructor_profile_picture = models.ImageField(upload_to='InstructorImage')
    fb_profile_link = models.CharField(max_length=200)
    linkedIn_profile_link = models.CharField(max_length=200,null=True,blank=True)
    twitter_profile_link = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.instructor_name
    
    
# Contact form
class Contact_forms(models.Model):
    name = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=100,null=True,blank=True)
    subjects = models.CharField(max_length=100,null=True,blank=True)
    messages = models.CharField(max_length=500)
    show_review_home = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
    
# Course Category and items  
COURSE_ITEM_CHOICES = (
    ('Academic','Academic'),
    ('Skill Development','Skill Development'),
    ('Others','Others'),
)
class Academy_course_Item(models.Model):
    course_item = models.CharField(choices=COURSE_ITEM_CHOICES, max_length=100, blank=True, null=True)
    course_name = models.CharField(max_length=100)
    course_instructor = models.CharField(max_length=50)
    duration_hour = models.CharField(max_length=50)
    duration_day = models.CharField(max_length=50,blank=True, null=True)
    total_student = models.CharField(max_length=50,blank=True, null=True)
    total_review_person = models.CharField(max_length=50, blank=True, null=True)
    course_price = models.CharField(max_length=50)
    discount_price = models.CharField(max_length=50)
    course_banner = models.ImageField(upload_to='CourseBannerImage')
    demo_class_link_YT = models.CharField(max_length=300)
    course_playlist_link = models.CharField(max_length=200)
    popular_or_not = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return str(self.id)
    
    
# # Course FAQ
# class FaQ_list_Item(models.Model):
#     course_item = models.ForeignKey(Academy_course_Item, on_delete=models.CASCADE)
#     question = models.CharField(max_length=255)
#     answer = models.TextField(1000)

#     def __str__(self):
#         return self.question
    
    # FaQ
class Faq_question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    course = models.ForeignKey(Academy_course_Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
