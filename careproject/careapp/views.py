from django.shortcuts import render,redirect
from careapp.models import User,Support
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):
    return render(request,'index_cms.html')

def about(request):
    return render(request,'aboutus.html')


def caretaker_registration(request):
    def handle_uploaded_file(f):  
        with open('careapp/static/files/'+f.name, 'wb+') as destination:  
            for chunk in f.chunks():  
                destination.write(chunk)
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            dateofbirth = request.POST['dateofbirth']
            resume = request.FILES['res']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            district = request.POST['district']
            state = request.POST['state']
            id_proof = request.POST['id_proof']
            handle_uploaded_file(request.FILES['res'])
            password=fname+phone[2:5]

            User.objects.create_user(first_name=fname, last_name=lname,username=email,email=email,phone=phone,password=password, d_o_b=dateofbirth, resume=resume, address=address, dist=district, state=state, id_proof=id_proof,usertype=2,cr_status=0)

            return redirect(index) # Redirect to a success page
        else:
            return render(request, 'care_reg.html')
    except:
        return render(request,'care_reg.html',{'data':"Fill the form properly"})


def client_reg(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            dateofbirth = request.POST['dateofbirth']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            district = request.POST['district']
            state = request.POST['state']

            id_proof = request.POST['id_proof']
            password=request.POST['password']
            cr_dist1=request.POST['cr_dist1']
            cr_dist2=request.POST['cr_dist2']

            
            User.objects.create_user(first_name=fname, last_name=lname,username=email,email=email,phone=phone,password=password, d_o_b=dateofbirth, address=address, dist=district, state=state, id_proof=id_proof,cr_dist1=cr_dist1,cr_dist2=cr_dist2,usertype=3)

            return redirect(index) # Redirect to a success page


        else:
            return render(request, 'client_reg.html')
    except:
        return render(request,'client_reg.html',{'data':"Fill the form properly"})


def logins(request):
    if request.method=='POST':
        usern = request.POST['username']
        passw = request.POST['password']
        print(usern)
        user = authenticate(request,username=usern,password=passw)
        print(user)
        if user is not None and user.usertype == 1:
            request.session['user_id'] = user.id
            login(request,user)
            return redirect(cms_dash)
        
        elif user is not None and user.usertype == 2:
            request.session['user_id'] = user.id
            login(request,user)
            return "hello"

        elif user is not None and user.usertype == 3:
            request.session['user_id'] = user.id
            login(request,user)
            return "HttpResponse('Success <br> <a href="
        else:
            return "HttpResponse('Sorry Invalid details')"
    else:
        return render(request,'loginbase.html')

def logouts(request):
    logout(request)
    return redirect(logins)

# CMS dash board
# @login_required
def cms_dash(request):
    try:
        if request.session['user_id']:
            client_count = User.objects.filter(usertype=3).count()
            cr_count = User.objects.filter(usertype=2,cr_status=1).count()
            msg_count=Support.objects.count()
            latest_records = User.objects.filter(usertype=2,cr_status=1).order_by('date_joined')[:5]

            
            return render(request,"cms_dash.html",{'c_count':client_count,'cr_count':cr_count,'msg_count':msg_count,'latest':latest_records})
    except:
        
        return redirect(logins)
def rec_request(request):
    cr_recruit=User.objects.filter(usertype=2,cr_status=0)
    return render(request,'rec_request.html',{'recruits':cr_recruit})

def apprv_cr(request,id):
    User.objects.filter(id=id).update(cr_status=1)
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return False

    # Generate a new password
    new_password = User.objects.make_random_password()

    # Reset the user's password
    user.set_password(new_password)
    user.save()

    subject = 'Welcome to Careline'
    message = f'You are selected for the caretaking job with the following credentials:\n\nUsername: {user.email}\nPassword: {new_password}\n\n\tPlease wait for Approval from the admin (Login After Visit to Office).'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, email_from, recipient_list)
    return redirect(rec_request)

def reject(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect(rec_request)


def view_support(request):
    msg=Support.objects.all()
    return render(request,'view_msg.html',{'msg':msg})

def rejectmsg(request,id):
    user=Support.objects.get(id=id)
    user.delete()
    return redirect(view_support)


#caretaker

def care_dash(request):
    return render(request,'care_dash.html')

#support

def support(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        message = request.POST['message']
        email = request.POST['email']
        Support.objects.create(fname=fname,lname=lname,message=message,email=email)
        messages.success(request, 'Submitted successful!')
        return redirect(index)
    else:
        return render(request,'support.html')
    



