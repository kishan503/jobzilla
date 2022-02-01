from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
import math
from django.db.models import Max
# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    
    def __str__(self):
        return self.email
    
class Company(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_address = models.CharField(max_length=100)
    company_contact = models.CharField(max_length=20)
    company_city = models.CharField(max_length=30)
    company_type = models.CharField(max_length=30)
    company_established = models.CharField(max_length=100,default="")
    company_info = models.TextField(null=True,blank=True)
    company_emp = models.IntegerField(default=0)
    
    company_logo=models.FileField(upload_to='media/images/',default='media/default.jpg')
    company_cover=models.FileField(upload_to='media/images/',default='media/company-default-cover-pic.jpg')
    
    def __str__(self):
        return self.company_name
    
    def followingStatus(self,client_id):
        fall = CompanyFollower.objects.all()
        
        all_companies = []
        all_clients = [] 
        
        for i in fall:
            all_companies.append(i.company_id)
            all_clients.append(i.client_id)
        
        status = CompanyFollower.objects.get(company_id = self.id)
        
        print("-----> query set ",status)
        return status.following_status    
    

class Client(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    client_name = models.CharField(max_length=30)
    client_address = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=20)
    client_qualification = models.CharField(max_length=30)
    client_gender = models.CharField(max_length=30)
    client_skills = models.CharField(max_length=50)
    
    client_logo=models.FileField(upload_to='media/images/',default='media/userdefault.png')
    client_cover=models.FileField(upload_to='media/images/',default='media/company-default-cover-pic.jpg')
    
    def __str__(self):
        return self.client_name
    
class Company_Gallary(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    picture = models.FileField(upload_to='media/images/',blank=True,null=True)
    
    def __str__(self):
        return self.company_id.company_name
    
class Client_Gallary(models.Model):
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    picture = models.FileField(upload_to='media/images/',blank=True,null=True)
    
    def __str__(self):
        return self.client_id.client_name

class JobPost(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    job_salary =  models.ImageField()
    job_description = models.TextField()
    job_tags = models.CharField(max_length=100)
    emp_requirement = models.ImageField()
    
    status = models.CharField(max_length=20,default="open")
    created_at= models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    
    def __str__(self):
        return self.post_title+" post added by "+self.company_id.company_name
    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
            
    def mylikes(self):
        try:
            my_post_likes = PostLike.objects.filter(jobPost_id = self.id).order_by('-likes')
            # print("----> mypost like",my_post_likes[0].likes)
            # total_likes = my_post_likes.aggregate(Max('likes'))
            # print("-------------------> likes",total_likes)
            total_likes = my_post_likes[0].likes
            return total_likes
        except:
            return 0        
            
    def mytags(self):
        myall_tags = self.job_tags.split(",")
        
        print("---->>> myall_tags",myall_tags)
        return myall_tags
            
class PostLike(models.Model):
    jobPost_id = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client,models.CASCADE)
    likes = models.IntegerField(default=0)
    
    created_at= models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    
    def __str__(self):
        return self.jobPost_id.post_title +" liked by "+self.client_id.client_name
    
    
class CompanyFollower(models.Model):
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    following_status = models.CharField(max_length=20,default="pending")
    created_at= models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    
    def __str__(self):
        return self.client_id.client_name+" following "+self.company_id.company_name
        
    #  def followingStatus(self):
    #         data = CompanyFollower.objects.filter(client_id = self.client_id,company_id = self.company_id)
    #     print("------>data -----------------> ",data)
    #     return data.following_status 