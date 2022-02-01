from django.shortcuts import render
from company.models import * 
from django.shortcuts import redirect
from django.core.mail import send_mail
from random import * 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

"""
insert data into table : 

        model.objects.create() 

retrive data from table condition wise (singular data): 

        model.objects.get(fieldname = value)   
        
        note : it return single object but if it does not match it will thrown an exception 
        
retrive data from table condition wise (multiple data) :

    
        model.objects.filter(fieldname = value)

        note : it return queryset if it does not match any criteria it does not return any exception or error 
      
      
retrive all data from model : 

        model.objects.all()
        
"""

def home(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        # call_latest_job = JobPost.objects.filter(company_id = cid).order_by('-created_at')[0]
        # print("---> call latest job",call_latest_job)
        
        # if call_latest_job:   
        #     jobs_category = call_latest_job.post_title 
        #     print("----> jobs_category",jobs_category)
        #     suggesstion = Client.objects.filter(client_skills__icontains = jobs_category)
        #     print("suggesstion==?",suggesstion)
            
        
        context = {
                        'uid':uid,
                        'cid':cid,
                        'call':call,
                        'calljob':calljob,
                    
        }
        return render(request,"company/company-profile.html",context)   
    
    elif "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        clall = Client_Gallary.objects.filter(client_id = clid)
        calljob = JobPost.objects.all().order_by('-created_at')            
                
        context = {
                        'uid':uid,
                        'clid':clid,
                        'clall':clall,
                        'calljob':calljob,
        }
        return render(request,"company/user-profile.html",context)
    
    else:
        return redirect('company-signin')

def index(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        context = {
                        'uid':uid,
                        'cid':cid,
                        'call':call,
                        'calljob':calljob,
        }
        return render(request,"company/index.html",context)  
    
def company_signup(request):
    if "companyemail" in request.session:
        return redirect('home')
    else:
        try:
            if request.POST:
                if request.POST['role'] == "company":
                    print("-----> submit button called")
                    company_name = request.POST['companyname']
                    company_email = request.POST['companyemail']
                    company_contact = request.POST['companycontact']
                    company_city = request.POST['companycity']
                    company_address = request.POST['companyaddress']
                    company_category = request.POST['companycategory']
                    
                    data = ['asd234','78httt','888hTT','909ssd','7843nc']
                    
                    password = choice(data)+company_contact[-3:]+company_email[:3]
                    
                    # terms = request.POST['terms']
                    # print("---> terms = ",terms)
                    if "checked" in request.POST['terms']:
                        uid = User.objects.create(email = company_email,
                                                password = password,
                                                role = request.POST['role'])
                        
                        
                        cid = Company.objects.create(user_id = uid,
                                                    company_name= company_name,
                                                    company_address = company_address,
                                                    company_contact = company_contact,
                                                    company_city = company_city,
                                                    company_type = company_category
                                                    )
                        
                        if cid:    
                            print("-----------------> successfully registered")
                            send_mail("Confirmation Mail","Welcome to jobZilla Portal - please check your password : "+password,"anjali.20.learn@gmail.com",[company_email])
                            s_msg = "Successfully register - please check your email inbox for autogenerated password "
                            return render(request,"company/sign-in.html",{'s_msg':s_msg})
                        else:
                            e_msg = "something went wrong"
                            return render(request,"company/sign-in.html",{'e_msg':e_msg})
                    else:
                        e_msg = "terms and condition must be agree "
                        return render(request,"company/sign-in.html",{'e_msg':e_msg})
                else:
                    pass
            else:
                print("----> only refresh without submit button")
                return render(request,"company/sign-in.html")
        except Exception as e:
            print("---> exception : ",e)
            e_msg = "Email already exist"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})

def client_signup(request):
    if "clientemail" in request.session:
        return redirect('home')
    else:
        try:
            if request.POST:
                if request.POST['role'] == "client":
                    client_name = request.POST['clientname']
                    client_email = request.POST['clientemail']
                    client_contact = request.POST['clientcontact']
                    client_gender = request.POST['clientgender']
                    client_address = request.POST['clientaddress']
                    client_qualification = request.POST['clientqualification']
                        
                    data = ['ab123','cd456','ef789','gh100','ij012']
                        
                    password = choice(data)+client_contact[-3:]+client_email[:3]
                        
                    if "checked" in request.POST['terms']:
                        uid = User.objects.create(email = client_email,
                                                password = password,
                                                role = request.POST['role'])
                            
                            
                        clid = Client.objects.create(user_id = uid,
                                                    client_name= client_name,
                                                    client_address = client_address,
                                                    client_contact = client_contact,
                                                    client_gender = client_gender,
                                                    client_qualification = client_qualification
                                                    )
                        if clid:    
                                print("-----------------> successfully registered")
                                send_mail("Confirmation Mail","Welcome to jobZilla Portal - please check your password : "+password,"anjali.20.learn@gmail.com",[client_email])
                                s_msg = "Successfully register - please check your email inbox for autogenerated password "
                                return render(request,"company/sign-in.html",{'s_msg':s_msg})
                        else:
                                e_msg = "something went wrong"
                                return render(request,"company/sign-in.html",{'e_msg':e_msg})
                    else:
                            e_msg = "terms and condition must be agree "
                            return render(request,"company/sign-in.html",{'e_msg':e_msg})
                else:
                    pass
            else:
                print("----> only refresh without submit button")
                return render(request,"company/sign-in.html")
        except Exception as e:
            print("---> exception : ",e)
            e_msg = "Email already exist"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})
        
@csrf_exempt 
def company_signin(request):
    if "companyemail" in request.session:
        return redirect('home')
    elif "clientemail" in request.session:
        return redirect('home')
    else:
        try:
            if request.POST:
                email = request.POST['email']
                password = request.POST['password']
                print("---email ,",email)
                
                # uid = User.objects.get(email = email)
                uid = User.objects.filter(email = email)
                if uid:
                    if uid[0].password == password:
                        if uid[0].role == 'company':
                            uid = User.objects.get(email = email)
                            cid = Company.objects.get(user_id = uid)
                            request.session['companyemail'] = uid.email
                            call = Company_Gallary.objects.filter(company_id = cid)
                            calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
                            #send_mail("JobZilla","Welcome to jobZilla Portal","anjali.20.learn@gmail.com",[email])
                            context = {
                                    'uid':uid,
                                    'cid':cid,
                                    'call':call,
                                    'calljob':calljob,
                            }
                            return render(request,"company/company-profile.html",context)
                        else:
                            uid = User.objects.get(email = email)
                            clid = Client.objects.get(user_id = uid)
                            request.session['clientemail'] = uid.email
                            #send_mail("JobZilla","Welcome to jobZilla Portal","anjali.20.learn@gmail.com",[email])
                            clall = Client_Gallary.objects.filter(client_id = clid)
                            calljob = JobPost.objects.filter(status="open").order_by('-created_at')
                            
                            context = {
                                    'uid':uid,
                                    'clid':clid,
                                    'clall':clall,
                                    'calljob':calljob,
                            }
                            print("------> client ",clid.client_name)
                            return render(request,"company/user-profile.html",context)
                    else:
                        e_msg = "Invalid password"
                        return render(request,"company/sign-in.html",{'e_msg':e_msg})
                else:
                    e_msg = "email does not exist"
                    return render(request,"company/sign-in.html",{'e_msg':e_msg})                 
            else:
                return render(request,"company/sign-in.html")
        except:
            e_msg = "Something went wrong"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})    
            
def company_profile(request):
    if "companyemail" in request.session:
        return redirect('home')
    else:
        return redirect('company-signin')   

def client_profile(request):
    if "clientemail" in request.session:
        return redirect('home')
    else:
        return redirect('company-signin')

def company_logout(request):
    if "companyemail" in request.session:
        del request.session['companyemail']
        return redirect('company-signin')   
    else:
        return redirect('company-signin')   

def client_logout(request):
    if "clientemail" in request.session:
        del request.session['clientemail']
        return redirect('company-signin')   
    else:
        return redirect('company-signin')

def forgot_password(request):
    return render(request,"company/forgotpassword.html")

@csrf_exempt
def send_otp(request):
    try:
        if request.POST:
            email = request.POST['email']
            uid = User.objects.get(email = email)
            otp = randint(1111,9999)
            
            if uid:
                send_mail("Forgot - password","Use your otp for reset password : "+str(otp),"anjali.20.learn@gmail.com",[uid.email])
                uid.otp = otp 
                uid.save()
                return render(request,"company/reset-password.html",{'email':email})
        else:
            return render(request,"company/forgotpassword.html")
    except:
        e_msg="something went wrong - please check your email"
        return render(request,"company/forgotpassword.html",{'e_msg':e_msg})
    
@csrf_exempt
def reset_password(request):
    try:
        if request.POST:
            email = request.POST['email']
            newpassword = request.POST['newpassword']
            repassword = request.POST['repassword']
            otp = request.POST['otp']
            uid = User.objects.get(email = email)
            print("newpassword---->",newpassword)
            print("repassword---->",repassword)
            print("email---->",email)
            if uid:
                print("uid ---->",uid)
                if newpassword == repassword:
                    # update new password password 
                    print("---> password change ")
                    print("----> inside the msg ")
                    if str(uid.otp) == otp :
                        uid.password = newpassword 
                        uid.save() 
                        s_msg="successfully password reset"
                        return render(request,"company/sign-in.html",{'s_msg':s_msg})
                    else:
                        e_msg="invalid otp"
                        return render(request,"company/reset-password.html",{'e_msg':e_msg,'email':email})    
                else:
                    e_msg = "password does not match !!!"
                    print("-----> error msg ",e_msg)
                    return render(request,"company/reset-password.html",{'e_msg':e_msg,'email':email})
        else:
            return render(request,"company/forgotpassword.html")
    except Exception as e:
        print("errorr22-------------> ",e)
        e_msg="something went wrong - please check your email"
        return render(request,"company/reset-password.html",{'e_msg':e_msg})

def companies(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        
        call = Company.objects.exclude(user_id = uid)
        
        
        context = {
            'uid':uid,
            'cid':cid,
            "company_all":call,
        }
        return render(request,"company/companies.html",context)
    elif "clientemail" in request.session:
        call = Company.objects.all()
        context = {
            "company_all":call,
        }
        return render(request,"company/companies.html",context)
    else:
        return redirect('company-signin')
    
def clients(request):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        
        clall = Client.objects.exclude(user_id = uid)
        context = {
            "clall":clall,
        }
        return render(request,"company/userprofiles.html",context)
    elif "companyemail" in request.session:
        clall = Client.objects.all()
        context = {
            "clall":clall,
        }
        return render(request,"company/userprofiles.html",context)
    else:
        return redirect('company-signin') 
    
def company_profile_settings(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        context = {
            'uid':uid,
            'cid':cid,
        }
        return render(request,"company/profile-account-setting.html",context)
    else:
        return redirect('company-signin')   

def client_profile_settings(request):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        context = {
            'uid':uid,
            'clid':clid,
        }
        return render(request,"company/user-account-setting.html",context)
    else:
        return redirect('company-signin')
    
def upload_company_logo(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        if "company_logo" in request.FILES:
            company_logo = request.FILES['company_logo']
            cid.company_logo = company_logo
            cid.save() # update 
        
        if "company_cover_pic" in request.FILES:
            company_cover = request.FILES['company_cover_pic']
            cid.company_cover = company_cover
            cid.save() 
            
        context = {
            'uid':uid,
            'cid':cid,
            'call':call,
            'calljob':calljob,
        }
        return render(request,"company/company-profile.html",context)
    else:
        return redirect('company-signin') 
    
def company_password_change(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        
        if request.POST:
        
            old_password = request.POST['old-password']
            new_password = request.POST['new-password']
            repeat_password = request.POST['repeat-password']
            
            if uid.password == old_password:
                if new_password == repeat_password:
                    uid.password = repeat_password
                    uid.save() 
                    context = {
                        'uid':uid,
                        'cid':cid,
                        's_msg':"password succefully updated"
                    }                        
                    return render(request,"company/profile-account-setting.html",context)
                else:
                    context = {
                        'uid':uid,
                        'cid':cid,
                        'e_msg':"password does not match !!!"
                    }                        
                    return render(request,"company/profile-account-setting.html",context)
            else:
                context = {
                        'uid':uid,
                        'cid':cid,
                        'e_msg':"Invalid old password"
                    }                        
                return render(request,"company/profile-account-setting.html",context)
        
        else:
            context = {
                'uid':uid,
                'cid':cid,
            }
            return render(request,"company/profile-account-setting.html",context)
    else:
        return redirect('company-signin')
    
def client_password_change(request):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        
        if request.POST:
            old_password = request.POST['old-password']
            new_password = request.POST['new-password']
            repeat_password = request.POST['repeat-password']
            
            if uid.password == old_password:
                if new_password == repeat_password:
                    uid.password == repeat_password
                    uid.save() 
                    context = {
                        'uid':uid,
                        'clid':clid,
                        's_msg':"password succefully updated"
                    }                        
                    return render(request,"company/user-account-setting.html",context)
                else:
                    context = {
                        'uid':uid,
                        'clid':clid,
                        'e_msg':"password does not match !!!"
                    }                        
                    return render(request,"company/user-account-setting.html",context)
            else:
                context = {
                        'uid':uid,
                        'clid':clid,
                        'e_msg':"Invalid old password"
                    }                        
                return render(request,"company/user-account-setting.html",context)
        else:
            context = {
                'uid':uid,
                'clid':clid,
            }
            return render(request,"company/user-account-setting.html",context)
    else:
        return redirect('company-signin')
        
    
def company_details(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        
        print("inside the update table data ")
        if request.POST:
            company_name = request.POST['company_name']
            company_established = request.POST['company_established']
            company_info = request.POST['company_info']
            company_address = request.POST['company_address']
            
            print("---> company info",company_info)
            cid.company_name = company_name
            cid.company_established = company_established
            cid.company_info = company_info
            cid.company_address = company_address
            
            cid.save()
            
            context = {
                'uid':uid,
                'cid':cid,
            }
            return render(request,"company/profile-account-setting.html",context)
    else:
        return redirect('company-signin')

def client_details(request):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        
        print("inside the update table data ")
        if request.POST:
            client_name = request.POST['client_name']
            client_qualification = request.POST['client_qualification']
            client_skills = request.POST['client_skills']
            client_address = request.POST['client_address']
            
            clid.client_name = client_name
            clid.client_qualification = client_qualification
            clid.client_skills = client_skills
            clid.client_address = client_address
            
            clid.save()
            
            context = {
                'uid':uid,
                'clid':clid,
            }
            return render(request,"company/user-account-setting.html",context)
    else:
        return redirect('company-signin')
                        
def upload_client_logo(request):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        
        if "client_logo" in request.FILES:
            client_logo = request.FILES['client_logo']
            clid.client_logo = client_logo
            clid.save() # update 
        
        if "client_cover_pic" in request.FILES:
            client_cover = request.FILES['client_cover_pic']
            clid.client_cover = client_cover
            clid.save() 
        
        context = {
            'uid':uid,
            'clid':clid,
        }
        return render(request,"company/user-profile.html",context)
    else:
        return redirect('company-signin')
    
    
def view_other_company_profile(request,pk):
    cid = Company.objects.get(id = pk)
    call = Company_Gallary.objects.filter(company_id = cid)
    print('----> pk ',pk)
    context = {
        'cid':cid,
        'call':call
    }
    return render(request,"company/view-other-company-profile.html",context)

def view_other_client_profile(request,pk):
    clid = Client.objects.get(id = pk)
    # clall = Company_Gallary.objects.filter(company_id = cid)
    print('----> pk ',pk)
    context = {
        'clid':clid,
        # 'call':call
    }
    return render(request,"company/view-other-client-profile.html",context)

def update_companyportfolio(request):
     if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        if request.FILES:
            pic = request.FILES['portfolio']
            cid_pic = Company_Gallary.objects.create(company_id = cid,picture = pic)
            call = Company_Gallary.objects.filter(company_id = cid)
            
            if cid_pic:        
                context = {
                    'uid':uid,
                    'cid':cid,
                    'call':call,
                    'calljob':calljob,
                }
                return render(request,"company/company-profile.html",context)
            else:
                context={
                    'uid':uid,
                    'cid':cid,
                    'calljob':calljob,
                    'e_msg':"something went wrong in company portfolio - please try again !!!"
                }
                return render(request,"company/profile-account-setting.html",context)
        else:
            context = {
                    'uid':uid,
                    'cid':cid,
                    'calljob':calljob,
                }
            return render(request,"company/profile-account-setting.html",context)
        
def update_clientportfolio(request):
     if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        calljob = JobPost.objects.all().order_by('-created_at')
                
        if request.FILES:
            pic = request.FILES['portfolio']
            clid_pic = Client_Gallary.objects.create(client_id = clid,picture = pic)
            clall = Client_Gallary.objects.filter(client_id = clid)
            if clid_pic:        
                context = {
                    'uid':uid,
                    'clid':clid,
                    'clall':clall,
                    'calljob':calljob,
                }
                return render(request,"company/user-profile.html",context)
            else:
                context={
                    'uid':uid,
                    'clid':clid,
                    'calljob':calljob,
                    'e_msg':"something went wrong in company portfolio - please try again !!!"
                }
                return render(request,"company/user-account-setting.html",context)
        else:
            context = {
                    'uid':uid,
                    'clid':clid,
                }
            return render(request,"company/user-account-setting.html",context)

def create_new_jobpost(request):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        if request.POST:    
            title= request.POST['jobtitle']
            type = request.POST['jobtype']
            salary = request.POST['jobsalary']
            description = request.POST['jobdescription']
            tags = request.POST['jobtag']
            emp_requirement = request.POST['emp-requirements']
                
            cid_job= JobPost.objects.create(company_id = cid,
                                            post_title = title,
                                            job_type = type,
                                            job_salary = salary,
                                            job_description = description,
                                            job_tags = tags,
                                            emp_requirement = emp_requirement,
                                            )
                
            calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
            
            if cid_job:
                    context = {
                        'uid':uid,
                        'cid':cid,
                        'calljob':calljob,
                        'call':call,
                    }
                    return render(request,"company/company-profile.html",context)
            else:
                    context={
                        'uid':uid,
                        'cid':cid,
                        'call':call,
                        'calljob':calljob,
                    }
                    return render(request,"company/company-profile.html",context)
        else:
            return redirect('home')
            
    else:
        return redirect('home')

def like_jobpost(request,pk):
    if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        context = {
                        'uid':uid,
                        'cid':cid,
                        'call':call,
                        'calljob':calljob,
        }
        return render(request,"company/company-profile.html",context)   
    
    elif "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        calljob = JobPost.objects.all().order_by('-created_at')
        
        jid = JobPost.objects.get(id = pk)
        print("---->job like pk",pk)
        like_jobs = PostLike.objects.filter(jobPost_id=pk)
        if like_jobs:
            
            # jid.likes = jid.likes+1
            
            # jid.save()
            pall = PostLike.objects.all()
            
            all_clients = [] 
            
            for i in pall:
                all_clients.append(i.client_id)
            
            if clid in all_clients:
                print("you have already like this post")
            else:
                like_id = PostLike.objects.create(jobPost_id = jid,client_id = clid,likes= like_jobs[0].likes+1)
                print("---> already liked")
        else:
            
            like_id = PostLike.objects.create(jobPost_id = jid,client_id = clid,likes=1)
            
            print("---->no ones likes")
        
        
        calljob = JobPost.objects.all().order_by('-created_at') # retrive all jobs 
        
        for job in calljob:
            print("----> job title",job.post_title)
            all_likes = PostLike.objects.filter(jobPost_id= job.id)
            print("-----> all likes",all_likes)
            for item in all_likes:
                print("---> likes",item.likes)
        
        context = {
                        'uid':uid,
                        'clid':clid,
                        'calljob':calljob,
        }
        
        
        return render(request,"company/user-profile.html",context)
    return redirect('home')

def post_likes(request,pk):
     if "companyemail" in request.session:
        uid = User.objects.get(email = request.session['companyemail'])
        cid = Company.objects.get(user_id = uid)
        call = Company_Gallary.objects.filter(company_id = cid)
        calljob = JobPost.objects.filter(company_id = cid).order_by('-created_at')
        
        jid = JobPost.objects.get(id=pk)
        p_likes_by = PostLike.objects.filter(jobPost_id = jid)
        
        context = {
                        'uid':uid,
                        'cid':cid,
                        'call':call,
                        'calljob':calljob,
                        'p_likes_by':p_likes_by,
        }
        
        return render(request,"company/post_likes.html",context)
        # return render(request,"company/company-profile.html",context)   
def follow(request,pk):
    if "clientemail" in request.session:
        uid = User.objects.get(email = request.session['clientemail'])
        clid = Client.objects.get(user_id = uid)
        cid = Company.objects.get(id = pk)
        company_all = Company.objects.all()
        
        
        fall = CompanyFollower.objects.all()
        
        all_companies = []
        all_clients = [] 
        
        for i in fall:
            all_companies.append(i.company_id)
            all_clients.append(i.client_id)
        
        if cid in all_companies and clid in all_clients:
            print("---> already following request added")
        else:
            fid = CompanyFollower.objects.create(client_id = clid,company_id = cid)
            print("---> company following request added")
            
        print("---> all companies",all_companies)
        print("----> all clients ",all_clients) 
        
        
        #follow_by = CompanyFollower.objects.filter(client_id = clid)
        context = {
                        'uid':uid,
                        'clid':clid,
                        'company_all':company_all,
                        'all_companies':all_companies,
                        'all_clients':all_clients
        }
        return render(request,"company/companies.html",context)
    
def delete_post(request,pk):
    if "companyemail" in request.session:
        calljob_id = JobPost.objects.get(id = pk)
        calljob_id.delete()
        return redirect('home')
    else:
        return redirect('home')  

def close_post(request,pk):
    if "companyemail" in request.session:
        calljob_id = JobPost.objects.get(id = pk)
        calljob_id.status = "close"
        calljob_id.save()
        return redirect('home')
    else:
        return redirect('home') 