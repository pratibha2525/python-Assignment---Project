
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import *
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.mail import send_mail
from .utils import *
# Create your views here.
from random import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/index.html',context)
        elif uid.role=="member":
            mid = Member.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "mid":mid,
            }
            return render(request,'myapp/member-index.html',context)
        elif uid.role=="watchman":
            wid = watchman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "wid":wid,
            }
            return render(request,'myapp/watchman-index.html',context)
        else:
            pass
    else:
        return render(request,"myapp/login.html")

def about(request):
    return render(request,'myapp/about.html')

@csrf_exempt
def login(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            print("--> submit button clicked")
            p_email=request.POST['email']
            p_password=request.POST['password']
            try:
                uid = User.objects.get(email=p_email)
                
                if uid.password==p_password and uid.role=="chairman":
                    cid = Chairman.objects.get(user_id=uid)
                    #mid = Member.objects.get(user_id=uid)
                    print("------> firstname = ",cid.firstname)
                    request.session["email"] = p_email
                    context = {
                        'uid':uid,
                        'cid':cid,
                    }
                    subject = "confirmation mail"

                    mycustomer_mail(subject,"mail_template",p_email,{"uid":uid,"cid":cid})
                    return render(request,"myapp/index.html",context)
                elif uid.password==p_password and uid.role=="member":
                    if uid.is_verify:
                        mid = Member.objects.get(user_id=uid)
                        print("------> firstname = ",mid.firstname)
                        request.session["email"] = p_email
                        context = {
                            'uid':uid,
                            'mid':mid,
                        }
                        return render(request,"myapp/member-index.html",context)
                    else:
                        mid=Member.objects.get(user_id=uid)
                        context = {
                            "uid":uid,
                            "mid":mid,
                        }
                        return render(request,"myapp/change-password.html",context)
                elif uid.password==p_password and uid.role=="watchman": 
                        wid = watchman.objects.get(user_id=uid)
                        #mid = Member.objects.get(user_id=uid)
                        print("------> firstname = ",wid.firstname)
                        request.session["email"] = p_email
                        context = {
                            'uid':uid,
                            'wid':wid,
                        }
                        return render(request,"myapp/watchman-index.html",context)
                else:
                    context = {
                        "e_msg":"Invalid Password",
                    }
                    return render(request,"myapp/login.html",context)
            except Exception as e:
                print("-----> exception ",e)
                context = {
                    "e_msg":"Invalid email adress",
                    }
                return render(request,"myapp/login.html",context)
        else:
            print("--> Page just loaded")
            return render(request,"myapp/login.html")
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')


def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            # mid = Member.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
                # 'mid':mid,
            }
            return render(request,"myapp/profile.html",context)
        elif uid.role == "member":
            mid= Member.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "mid":mid,
            }
            return render(request,"myapp/profile-member.html",context)
        elif uid.role == "watchman":
            wid= watchman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "wid":wid,
            }
            return render(request,"myapp/profile-watchman.html",context)
    else:
        return redirect("login")
def change_password(request):
    if "email" in request.session:
        if request.POST:
            currentpassword=request.POST['currentpassword']
            newpassword=request.POST['newpassword']
            uid=User.objects.get(email=request.session['email'])
            if uid.role=="chairman":
                if uid.password==currentpassword:
                    uid.password=newpassword
                    uid.save()
                    cid=Chairman.objects.get(user_id=uid)
                    # mid = Member.objects.get(user_id=uid)
                    context={
                        'msg':"Succesfully password reset",
                        'uid':uid,
                        'cid':cid,
                        # 'mid':mid,
                    }
                    return render(request,"myapp/profile.html",context)
                else:
                    cid=Chairman.objects.get(user_id=uid)
                    # mid = Member.objects.get(user_id=uid)
                    context={
                        'uid':uid,
                        'cid':cid,
                        # 'mid':mid,
                        'msg': "Invalid password",    
                    }
                    return render(request,"myapp/profile.html",context)
            elif uid.role=="member":
                if uid.password==currentpassword:
                    uid.password=newpassword
                    uid.save()
                    mid=Member.objects.get(user_id=uid)
                    # mid = Member.objects.get(user_id=uid)
                    context={
                        'msg':"Succesfully password reset",
                        'uid':uid,
                        'mid':mid,
                        # 'mid':mid,
                    }
                    return render(request,"myapp/profile-member.html",context)
                else:
                    mid=Member.objects.get(user_id=uid)
                    # mid = Member.objects.get(user_id=uid)
                    context={
                        'uid':uid,
                        'mid':mid,
                        # 'mid':mid,
                        'msg': "Invalid password",    
                    }
                    return render(request,"myapp/profile-member.html",context)
            elif uid.role=="watchman":
                if uid.password==currentpassword:
                    uid.password=newpassword
                    uid.save()
                    wid=watchman.objects.get(user_id=uid)
                    # wid = watchman.objects.get(user_id=uid)
                    context={
                        'msg':"Succesfully password reset",
                        'uid':uid,
                        'wid':wid,
                        # 'wid':wid,
                    }
                    return render(request,"myapp/profile-watchman.html",context)
                else:
                    wid=watchman.objects.get(user_id=uid)
                    # wid = watchman.objects.get(user_id=uid)
                    context={
                        'uid':uid,
                        'wid':wid,
                        # 'mid':mid,
                        'msg': "Invalid password",    
                    }
                    return render(request,"myapp/profile-watchman.html",context)
        else:
            return redirect("profile")
    else:
        return redirect("login")

def change_details(request):
    if "email" in request.session:
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            
            # mid = Member.objects.get(user_id=uid)
            if uid.role=='chairman':
                fname=request.POST['firstname']
                lastname=request.POST['lastname']
                contact=request.POST['contact']
                block_no=request.POST['block_no']
                house_no=request.POST['house_no']
                about_me=request.POST['about_me']
                if "pic" in request.FILES:
                    cid.pic=request.FILES['pic']
                    cid.save()
                cid.firstname=fname
                cid.lastname=lastname
                cid.contact=contact
                cid.block_no=block_no
                cid.house_no=house_no
                cid.about_me=about_me
                
                cid.save()
                context={
                    'msg':"Succesfully details reset",
                    'uid':uid,
                    'cid':cid,
                    # 'mid':mid,
                }
                return render(request,"myapp/profile.html",context)
            else:
                return redirect("profile")
            
        else:
            return redirect("profile")
    else:
        return redirect("login")
def change_details_member(request):
    if "email" in request.session:
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            mid = Member.objects.get(user_id=uid)
            if uid.role=='member':
                mid.firstname=request.POST['firstname']
                mid.lastname=request.POST['lastname']
                mid.contact=request.POST['contact']
                mid.work=request.POST['work']
                mid.family_members=request.POST['family_members']
                mid.vehicle=request.POST['vehicle']
                mid.block_no=request.POST['block_no']
                mid.house_no=request.POST['house_no']
                mid.about_member=request.POST['about_member']
                if "pic" in request.FILES:
                    mid.pic=request.FILES['pic']
                    mid.save()
                
                mid.save()
                context={
                    'msg':"Succesfully details reset",
                    'uid':uid,
                    'mid':mid,
                    # 'mid':mid,
                }
                return render(request,"myapp/profile-member.html",context)
            else:
                return redirect("profile-member")
        
            
        else:
            return redirect("profile-member")
    else:
        return redirect("login")

def change_details_watchman(request):
    if "email" in request.session:
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            wid = watchman.objects.get(user_id=uid)
            if uid.role=='watchman':
                wid.firstname=request.POST['firstname']
                wid.lastname=request.POST['lastname']
                wid.contact=request.POST['contact']
                wid.address=request.POST['address']
                if "pic" in request.FILES:
                    wid.pic=request.FILES['pic']
                    wid.save()
                
                wid.save()
                context={
                    'msg':"Succesfully details reset",
                    'uid':uid,
                    'wid':wid,
                    # 'mid':mid,
                }
                return render(request,"myapp/profile-watchman.html",context)
            else:
                return redirect("profile-watchman")
        
            
        else:
            return redirect("profile-watchman")
    else:
        return redirect("login")

def add_notice(request):
    if "email" in request.session:
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            
            nid = Notice.objects.create(
                                user_id = uid,
                                title = request.POST['title'],
                                content = request.POST['content']
                                )
            if "pic" in request.FILES:
                    nid.pic=request.FILES['pic']
                    
            if "video" in request.FILES:
                    nid.pic=request.FILES['video']
            nid.save()
            context = {
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/add-notice.html',context)
        else:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/add-notice.html',context)
    else:
        return redirect("login")

def all_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='chairman':
            cid=Chairman.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context={
                "uid":uid,
                "cid":cid,
                "nall":nall,
            }
            return render(request,'myapp/view-notice.html',context)
        elif uid.role=='member':
            mid=Member.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context={
                "uid":uid,
                "mid":mid,
                "nall":nall,
            }
            return render(request,'myapp/view-notices.html',context)
        elif uid.role=='watchman':
            wid=watchman.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context={
                "uid":uid,
                "wid":wid,
                "nall":nall,
            }
            return render(request,'myapp/view-notices_watchman.html',context)
        else:
            pass
    else:
        return render(request,'myapp/login.html')
        

def add_member(request):
    if "email" in request.session:
        
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            
            email=request.POST['email']
            contact = request.POST['contact']
            data=["sd4c45","df56fg","5sd65f","dre654"]
            c_no = str(contact[4:9])
            e=str(email[5:8])
            password=choice(data)+c_no+e
            u_id = User.objects.create(email=request.POST['email'],
                                     password=password,
                                     role='member',
                                     )
            mid = Member.objects.create(user_id = u_id,
                                        email=request.POST['email'],
                                        
                                        firstname = request.POST['firstname'],
                                        lastname = request.POST['lastname'],
                                        work = request.POST['work'],
                                        family_members = request.POST['family_members'],
                                        block_no = request.POST['block_no'],
                                        house_no = request.POST['house_no'],
                                        vehicle = request.POST['vehicle'],
                                        contact = request.POST['contact'],
                                        about_member = request.POST['about_member'],
                                )
            if "pic" in request.FILES:
                    mid.pic=request.FILES['pic']

            print("add completed")
            context = {
                "uid":uid,
                "cid":cid,
            }
            mid.save()
            u_id.save()
            msg="your password is "+str(password)
            send_mail("Password confirmation",msg,"shubhammakwana45@gmail.com",[email])
            return render(request,'myapp/add-member.html',context)
        
        else:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            print("add not completed")
            return render(request,'myapp/add-member.html',context)
    else:
        return redirect('login')

def all_member(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='chairman':
            cid=Chairman.objects.get(user_id=uid)
            u_all=User.objects.all()
            mall=Member.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "cid":cid,
                "u_all":u_all,
                "mall":mall,
            }
            return render(request,'myapp/all-members.html',context)
        elif uid.role=='member':
            mid=Member.objects.get(user_id=uid)
            u_all=User.objects.all()
            mall=Member.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "mid":mid,
                "u_all":u_all,
                "mall":mall,
            }
            return render(request,'myapp/all-member_member.html',context)
        elif uid.role=='watchman':
            wid=watchman.objects.get(user_id=uid)
            u_all=User.objects.all()
            mall=Member.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "wid":wid,
                "u_all":u_all,
                "mall":mall,
            }
            return render(request,'myapp/all-member_watchman.html',context)
        else:
            return render(request,'myapp/all-members.html')
    else:
        return render(request,'myapp/login.html')
def add_watchman(request):
    if "email" in request.session:
        
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            
            
            u_id = User.objects.create(email=request.POST['email'],
                                     password=request.POST['password'],
                                     role='watchman',
                                     )
            wid = watchman.objects.create(user_id = u_id,
                                        email=request.POST['email'],
                                        password=request.POST['password'],
                                        firstname = request.POST['firstname'],
                                        lastname = request.POST['lastname'],
                                        contact = request.POST['contact'],
                                        address = request.POST['address'],
                                )
            if "pic" in request.FILES:
                    wid.pic=request.FILES['pic']
            
            print("add completed")
            context = {
                "uid":uid,
                "cid":cid,
            }
            wid.save()
            u_id.save()
            return render(request,'myapp/add-watchman.html',context)
        
        else:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            print("add not completed")
            return render(request,'myapp/add-watchman.html',context)
    else:
        return redirect('login')
def all_watchman(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='chairman':
            cid=Chairman.objects.get(user_id=uid)
            u_all=User.objects.all()
            wall=watchman.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "cid":cid,
                "u_all":u_all,
                "wall":wall,
            }
            return render(request,'myapp/view-watchman.html',context)
        elif uid.role=='watchman':
            mid=watchman.objects.get(user_id=uid)
            u_all=User.objects.all()
            wall=watchman.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "mid":mid,
                "u_all":u_all,
                "wall":wall,
            }
            return render(request,'myapp/view-watchman.html',context)
        else:
            return render(request,'myapp/view-watchman.html')
    else:
        return render(request,'myapp/login.html')

def add_event(request):
    if 'email' in request.session:
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)

            eid=Event.objects.create(
                user_id=uid,
                title=request.POST['title'],
                content=request.POST['content'],
                venue=request.POST['venue'],
                Date=request.POST['Date'],
                Time=request.POST['Time'],
            )

            if "pic" in request.FILES:
                    eid.pic=request.FILES['pic']
                    eid.save()
                    
            if "video" in request.FILES:
                    eid.pic=request.FILES['video']
                    eid.save()

            eid.save()
            context={
                "uid":uid,
                "cid":cid,
            }

            return render(request,'myapp/add-event.html',context)
        else:
            uid=User.objects.get(email=request.session['email'])
            cid=Chairman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            return render(request,'myapp/add-event.html',context)
    else:
        return redirect("login")
def add_visitor(request):
    if "email" in request.session:
        
        if request.POST:
            uid=User.objects.get(email=request.session['email'])
            wid=watchman.objects.get(user_id=uid)

            vid = visitor.objects.create(
                                        email=request.POST['email'],
                                        firstname = request.POST['firstname'],
                                        lastname = request.POST['lastname'],
                                        contact = request.POST['contact'],
                                        Nametomeet=request.POST['Nametomeet'],
                                        block_no = request.POST['block_no'],
                                        house_no = request.POST['house_no'],
                                        address = request.POST['address'],
                                )
            if "pic" in request.FILES:
                    vid.pic=request.FILES['pic']
            
            print("add completed")
            context = {
                "uid":uid,
                "wid":wid,
            }
            vid.save()
            
            return render(request,'myapp/add-visitor.html',context)
        
        else:
            uid=User.objects.get(email=request.session['email'])
            wid=watchman.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "wid":wid,
            }
            print("add not completed")
            return render(request,'myapp/add-visitor.html',context)
    else:
        return redirect('login')
def all_visitor(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        
        if uid.role=='watchman':
            wid=watchman.objects.get(user_id=uid)
            vall=visitor.objects.all()
            print("display completed")
            context={
                "uid":uid,
                "wid":wid,
                "vall":vall,
            }
            return render(request,'myapp/view-visitor.html',context)
        else:
            return render(request,'myapp/view-visitor.html')
    else:
        return render(request,'myapp/login.html')

def all_event(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='chairman':
            cid=Chairman.objects.get(user_id=uid)
            eall=Event.objects.all()
            # print("event accessed-----------------------------------------------------  ",eall.Date)
            context={
                "uid":uid,
                "cid":cid,
                "eall":eall,
            }
            return render(request,'myapp/all-event.html',context)
        elif uid.role=='member':
            mid=Member.objects.get(user_id=uid)
            eall=Event.objects.all()
            # print("event accessed-----------------------------------------------------  ",eall.Date)
            context={
                "uid":uid,
                "mid":mid,
                "eall":eall,
            }
            return render(request,'myapp/all-events.html',context)
        elif uid.role=='watchman':
            wid=watchman.objects.get(user_id=uid)
            eall=Event.objects.all()
            # print("event accessed-----------------------------------------------------  ",eall.Date)
            context={
                "uid":uid,
                "wid":wid,
                "eall":eall,
            }
            return render(request,'myapp/all-events_watchman.html',context)
        else:
            return render(request,'myapp/add-event.html')
    else:
        return render(request,'myapp/login.html')
        
def update_password(request):
    email=request.POST['email']
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    repassword=request.POST['repassword']
    uid = User.objects.get(email=email)
    if uid.password==password:
        if newpassword==repassword:
            uid.password=newpassword
            uid.is_active=True
            uid.is_verify=True
            uid.save()
            
            return render(request,'myapp/login.html')
        else:
            context={
                "e_msg": "new password and re password are not same"
            }
            return render(request,'myapp/change-password.html',context)
    else:
        return redirect("login")

def forgot_password(request):
    # if request.POST:
    #         print("--> submit button clicked")
    #         p_email=request.POST['email']
    #         # p_password=request.POST['password']
    #         uid = User.objects.get(email=p_email)
    #         if uid.email==p_email:
    return render(request,"myapp/forgot-password1.html")
    # if 'email' in request.session:
    #     if request.POST:
    #         p_email=request.POST['email']
            
    #         uid = User.objects.get(email=p_email)
    #         if uid.email==p_email:
    #             return render(request,'myapp/reset.html')
    #         else:
    #             return render(request,'myapp/forgot-password.html')

    #     else:
    #         return render(request,'myapp/forgot-password.html')
    # else:
    #     return redirect("login")
                # data=["sd4c45","df56fg","5sd65f","dre654"]
                
            
            

            
                # email=User.objects.get[email]
                # password=request.POST['password']
                # newpassword=request.POST['newpassword']
                # repassword=request.POST['repassword']
                # uid = User.objects.get(email=email)
                # e=str(email[5:8])
                # password=choice(data)+e
                # if uid.email==email:
                #     msg="your password is "+str(password)
                #     send_mail("Password confirmation",msg,"shubhammakwana45@gmail.com",[email])
                #     if uid.password==password:
                        
                #         if newpassword==repassword:
                #             uid.password=newpassword
                            
                #             uid.save()
                #             return render(request,'myapp/login.html')
                #         else:
                #             context={
                #                 "e_msg": "new password and re password are not same"
                #             }
                #             return render(request,'myapp/change-forgot-password.html',context)
                #     else:
                #         return render(request,'myapp/forgot-password.html')
def reset_password(request):
    if request.POST:
        print("--> submit button clicked")
        p_email=request.POST['email']
        # p_password=request.POST['password']
        uid = User.objects.get(email=p_email)
        if uid.email==p_email:
            data=["sd4c45","df56fg","5sd65f","dre654"]      
            password=choice(data)
            msg="your password is "+str(password)
            send_mail("Password confirmation",msg,"shubhammakwana45@gmail.com",[p_email])
            uid.password = password
            uid.save()
            context = {
                    "uid":uid,
                    }
            
            return render(request,'myapp/change-forgot-password.html',context)
        else:
            return render(request,'myapp/forgot-password1.html')
    else:
        return redirect("login")

def update_forgot_password(request):
    email=request.POST['email']
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    repassword=request.POST['repassword']
    uid = User.objects.get(email=email)
    try:
        if uid.password==password and newpassword==repassword:
            
            uid.password=newpassword
            
            uid.is_active=True
            uid.is_verify=True
            uid.save()
            return render(request,'myapp/login.html')
    except Exception as e:
        print("exception is ---------",e)
        context={
            
            "e_msg": "new password and re password are not same",
        }
        return render(request,'myapp/change-forgot-password.html',context)
    else:
        return redirect("login")

