from django.shortcuts import render,redirect
from .models import SignUp,Contactfom,Hospitals,AdminBloodRequest,UserDonorRequest,AcceptDonorList,RejectDonorList,AcceptBloodList,RejectBloodList
from django.contrib.auth.models import User,auth
from django.contrib import messages
from twilio.rest import Client
from django.conf import settings
from django.db.models import Count
from django.core.mail import send_mail
from .filters import BloodgroupFilter
import smtplib
from email.message import EmailMessage
from django.db import connection, transaction


# Create your views here.
def Home(request):
    return render(request,'Homepage.html')

def Register(request):
    return render(request,'Register.html')

def SignIn(request):
    if request.COOKIES.get('Phone'):
        getfullname = request.COOKIES['Fullname']
        getphone = request.COOKIES['Phone']
        return render(request,'SignIn.html',{'getfullnamedata':getfullname,'getphonedata':getphone})
    return render(request,'SignIn.html')

def Userprofile(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')

        totaldonors = AcceptDonorList.objects.all().count()
        totalapprovedrequest = AcceptBloodList.objects.all().count()

        return render(request,'UserProfile.html',{'user':getsession,'approvedcount':totalapprovedrequest,'approveddonors':totaldonors})
    return redirect('/signin')

def Adminprofile(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        totaldonors = AcceptDonorList.objects.all().count()
        totalapprovedrequest = AcceptBloodList.objects.all().count()
        totaldonorpending = UserDonorRequest.objects.all().count()
        totalbloodpending = AdminBloodRequest.objects.all().count()

        #FOR EACH BLOODGROUP AVAIABLE COUNT
        queryset = AcceptDonorList.objects.values('d_bloodgroup').annotate(count=Count('d_bloodgroup'))
        queryset1 = AcceptBloodList.objects.values('p_blood_needed').annotate(count=Count('p_blood_needed'))
        table1 = {}
        table2 = {}
        count=0
        for item in queryset:
            table1[item['d_bloodgroup']] = item['count']     #table1[loop[key]] = loop[value]
        for item in queryset1:
            table2[item['p_blood_needed']] = item['count']

        for i in table1:
            if i in table2:
                count = table1[i] - table2[i]
                print(i,'=',count)
            if i not in table2:
                count = table1[i]
                print(i," = ",count)
        return render(request,'AdminProfile.html',{'admin':getsession,'table1':table1,'table2':table2,'count':count,'queryset':queryset,'queryset1':queryset1,'approvedcount':totalapprovedrequest,'approveddonors':totaldonors,'totaldonorpending':totaldonorpending,'totalbloodpending':totalbloodpending})
    return redirect('/adminsignin')

def Blog(request):
    return render(request,'Blogs.html')

def blog1(request):
    return render(request,'blogs/WhyDonateBlood.html')

def blog2(request):
    return render(request,'blogs/WhatisBloodDonation.html')

def blog3(request):
    return render(request,'blogs/Apheresis.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def FuncContactform(request):
        contactdata = Contactfom.objects.get()
        firstname = request.POST.get('fname','')
        lastname = request.POST.get('lname','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        area = request.POST.get('area','')
        subject = request.POST.get('subject','')
        content = request.POST.get('comment','')
        if request.method == 'POST' and email and firstname:
            send_mail(subject, content, settings.EMAIL_HOST_USER, ['msaranya480@gmail.com'], fail_silently=False)
        obj = {'contactdata':contactdata,'firstname':firstname,'lastname':lastname,'mobile':mobile,'email':email,'area':area}
        return render(request,'Contact.html',obj)

def Viewhospitals(request):
    result = Hospitals.objects.all()
    return render(request,'ViewHospitals.html',{'res':result})

def Addhospitals(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        return render(request,'AddHospitals.html',{'admin':getsession})
    return redirect('/adminsignin')

def Adminregister(request):
    return render(request,'AdminRegister.html')

def AdminSignIn(request):
    return render(request,'AdminSignIn.html')

#-------------FOR USER---------------

def FuncRegister(request):
    if request.method == 'POST':
        vfname = request.POST.get('full_name')
        vemail = request.POST.get('email')
        vage = request.POST.get('age')
        vgender = request.POST.get('gender')
        vpassword = request.POST.get('password')
        vcpassword = request.POST.get('cpassword')
        vblood = request.POST.get('blood')
        vphone = request.POST.get('phone')
        vcity = request.POST.get('city')
        vhealth = request.POST.get('health')
        vzip = request.POST.get('zip')
        if vpassword==vcpassword:
            if SignUp.objects.filter(phone=vphone).exists():
                messages.success(request,' Mobile Number is already Signed Up/exists')
                return redirect('/register')
            elif SignUp.objects.filter(email=vemail).exists():
                messages.success(request,'This Mail Id already exists')
                return redirect('/register')
            else:
                obj = SignUp()
                obj.full_name =vfname
                obj.email = vemail
                obj.age = vage
                obj.gender = vgender
                obj.password = vpassword
                obj.blood = vblood
                obj.phone = vphone
                obj.city = vcity
                obj.health = vhealth
                obj.zip = vzip
                obj.save()
                return redirect('/signin')
        else:
            messages.success(request,'Your Password does not match ')
            return redirect('/register')

def FuncSignin(request):
    if request.method=='POST':
        vfname = request.POST.get('full_name')
        vphone = request.POST.get('phone')
        vpassword = request.POST.get('password')
        user = SignUp.objects.filter(phone=vphone,password=vpassword).count()
        if user==1:
            request.session['Fullname'] = vfname
            if request.POST.get('gridCheck'):
                var_response = redirect('/signin')
                var_response.set_cookie('Fullname',vfname)
                var_response.set_cookie('Phone',vphone)
                return var_response
            return redirect('/userprofile')
        else:
            return redirect('/signin')

def FuncSignout(request):
    request.session.flush()
    return redirect('/signin')

def UserViewHopsital(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        result = Hospitals.objects.all()
        return render(request, 'UserViewHospitals.html', {'res': result,'user':getsession})
    return redirect('/signin')

def SendRequests(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        return render(request,'BothRequestsuserPage.html',{'user':getsession})
    return redirect('/signin')

def UserSendRequest(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        return render(request,'UserSendRequest.html',{'user':getsession})
    return redirect('/signin')

def FuncUserSendRequest(request):
    if request.method == 'POST':
        vpname = request.POST.get('p_name')
        vpage = request.POST.get('p_age')
        vpgender = request.POST.get('p_gender')
        vpcontact = request.POST.get('p_contact')
        vbloodneeded = request.POST.get('p_blood_needed')
        vpreason = request.POST.get('p_reason')
        vplocation = request.POST.get('p_location')
        obj = AdminBloodRequest()
        obj.p_name = vpname
        obj.p_age = vpage
        obj.p_gender = vpgender
        obj.p_contact = vpcontact
        obj.p_blood_needed = vbloodneeded
        obj.p_reason = vpreason
        obj.p_location = vplocation
        obj.save()
        messages.success(request,'Request Sent! You will be notified to your mobile number, mentioning if you request has been accepted or not. Thank You!')
        return redirect('/usersendrequest')         #<<<<<<<<<<<<<<<<<<<<<

#USER - CHECK BLOOD REQUEST
def UserBloodRequest(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        view_bloodrequests = AdminBloodRequest.objects.all()
        return render(request, 'UserBloodRequest.html', {'blood_data': view_bloodrequests,'user':getsession})
    return redirect('/signin')

#USER - DONOR REQUEST
def UserDonorRequests(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        return render(request,'UserDonorRequest.html',{'user':getsession})
    return redirect('/signin')

def FuncUserDonorRequests(request):
    if request.method == 'POST':
        vdname = request.POST.get('d_name')
        vdage = request.POST.get('d_age')
        vdgender = request.POST.get('d_gender')
        vdcontact = request.POST.get('d_contact')
        vbloodgroup = request.POST.get('d_bloodgroup')
        vdhealthissues = request.POST.get('d_healthissues')
        vdvisit = request.POST.get('d_visit')
        vdlocation = request.POST.get('d_location')
        obj = UserDonorRequest()
        obj.d_name = vdname
        obj.d_age = vdage
        obj.d_gender = vdgender
        obj.d_contact = vdcontact
        obj.d_bloodgroup = vbloodgroup
        obj.d_healthissues = vdhealthissues
        obj.d_visit = vdvisit
        obj.d_location = vdlocation
        obj.save()
        messages.success(request,'Request Sent! You will be notified to your mobile number, mentioning if you request has been accepted or not. Thank You!')
        return redirect('/userdonorrequest')

def my_view(request):
    api_key = settings.GOOGLE_API_KEY
    return render(request,'UserDonorRequest.html',{'api':api_key})
#------------------- ADMIN FUNCTIONS ----------------

def FuncAdminRegister(request):
    if request.method == 'POST':
        vfname = request.POST.get('fullname')
        vusername = request.POST.get('username')
        vemail = request.POST.get('email')
        vpassword = request.POST.get('password')
        vcpassword = request.POST.get('cpassword')
        if vpassword==vcpassword:
            if User.objects.filter(username=vusername).exists():
                messages.success(request,'This username already exists')
                return redirect('/adminregister')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request,'Email already exists')
                return redirect('/adminregister')
            else:
                adminuser = User.objects.create_superuser(fullname=vfname,username=vusername,email=vemail,password=vpassword)
                adminuser.save()
                messages.success(request,'You are registered successfully. Kindly LogIn now.')
                return redirect('/adminsignin')
        else:
            messages.success(request,'Passwords should match. Your password is wrong')
            return redirect('/adminregister')

def FuncAdminSignin(request):
    if request.method=='POST':
        vusername = request.POST.get('username')
        vpassword = request.POST.get('password')
        adminuser = auth.authenticate(username=vusername,password=vpassword)
        if adminuser is not None:
            auth.login(request,adminuser)
            request.session['Username'] = vusername
            return redirect('/adminprofile')
        else:
            messages.success(request,'Incorrect Password or Username')
            return redirect('/adminsignin')

def FuncAdminSignOut(request):
    auth.logout(request)
    request.session.flush()
    messages.success(request,'Successfully Logged Out')
    return redirect('/')

#-------------HOSPITALS ADD/DELETE/UPDATE-------------

#ADMIN - ADD HOSPITAL
def Funcaddhospitals(request):
    if request.method == 'POST':
        vhospital = request.POST.get('hospital')
        varea = request.POST.get('area')
        vcontact = request.POST.get('contact')
        if Hospitals.objects.filter(contact=vcontact).exists():
            messages.success(request, ' Mobile Number is already Signed Up/exists')
            return redirect('/addhospitals')
        else:
            object = Hospitals()
            object.hospital =vhospital
            object.area = varea
            object.contact = vcontact
            object.save()
            return redirect('/viewhospitals')
    return redirect('/addhospitals')

#ADMIN/USER - CHECK BLOOD REQUEST
def BloodRequest(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        view_bloodrequest = AdminBloodRequest.objects.all()
        return render(request, 'BloodRequest.html', {'blood_data': view_bloodrequest, 'admin': getsession})
    return redirect('/adminsignin')

#ADMIN - CHECK DONOR REQUEST
def DonorRequest(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        view_donorrequest = UserDonorRequest.objects.all()
        return render(request, 'DonorRequest.html', {'donor_data':view_donorrequest, 'admin': getsession})
    return redirect('/adminsignin')

def DonorsUserview(request):
    if 'Fullname' in request.session:
        getsession = request.session.get('Fullname','Guest')
        donor_data = AcceptDonorList.objects.all()
        myFilter = BloodgroupFilter(request.GET,queryset=donor_data)
        donor_data = myFilter.qs
        return render(request,'DonorsUserView.html',{'getsession':getsession,'donor_data':donor_data,'myFilter':myFilter})
    return redirect('/signin')

def Donors(request):
    donor_data = AcceptDonorList.objects.all()
    myFilter = BloodgroupFilter(request.GET,queryset=donor_data)
    donor_data = myFilter.qs
    return render(request,'AcceptedDonors.html',{'donor_data':donor_data,'myFilter':myFilter})

def Patients(request):
    blood_data = AcceptBloodList.objects.all()
    return render(request,'AcceptedPatients.html',{'blood_data':blood_data})

#ADMIN - ACCEPT DONOR
def AcceptDonor(request,did,dphone):
    table1_rows = UserDonorRequest.objects.filter(id=did)
    deldata = UserDonorRequest.objects.get(id=did,d_contact=dphone)

    for row in table1_rows.values():
        AcceptDonorList.objects.create(**row)

        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=dphone,
            from_=settings.TWILIO_PHONE_NUMBER,
            body='Greetings from Nevon Foundation! Your request for donating blood has been ACCEPTED. Our staff will contact you shortly. Thanks!')
        print(message.body)
        print(deldata)
        deldata.delete()
        return redirect('/donorrequest')

#ADMIN - REJECT DONOR
def RejectDonor(request,rdid,rdphone):
    table1_rows = UserDonorRequest.objects.filter(id=rdid)
    deldata = UserDonorRequest.objects.get(id=rdid,d_contact=rdphone)

    for row in table1_rows.values():
        RejectDonorList.objects.create(**row)

        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=rdphone,
            from_=settings.TWILIO_PHONE_NUMBER,
            body='Greetings from Nevon Foundation! Your request for donating blood has been REJECTED. Our staff will contact you shortly to let you know the reason. Thanks!')
        print(message.body)
        print(deldata)
        deldata.delete()
        return redirect('/donorrequest')

#ADMIN - ACCEPT BLOOD
def AcceptBlood(request,pid,pphone):
    table1_rows = AdminBloodRequest.objects.filter(id=pid)
    deldata = AdminBloodRequest.objects.get(id=pid,p_contact=pphone)

    for row in table1_rows.values():
        AcceptBloodList.objects.create(**row)

        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=pphone,
            from_=settings.TWILIO_PHONE_NUMBER,
            body='Greetings from Nevon Foundation! Your blood request has been ACCEPTED. Our staff will contact you shortly. Thanks!')
        print(message.body)
        print(deldata)

        deldata.delete()
        return redirect('/bloodrequest')

#ADMIN - REJECT BLOOD
def RejectBlood(request,rpid,rpphone):
    table1_rows = AdminBloodRequest.objects.filter(id=rpid)
    deldata = AdminBloodRequest.objects.get(id=rpid,p_contact=rpphone)

    for row in table1_rows.values():
        RejectBloodList.objects.create(**row)

        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=rpphone,
            from_=settings.TWILIO_PHONE_NUMBER,
            body='Greetings from Nevon Foundation! Your blood request has been REJECTED since we do not have sufficient stock. Kindly try in another blood bank. Thanks!')
        print(message.body)
        print(deldata)
        deldata.delete()
        return redirect('/bloodrequest')

#ADMIN - SEND REQUEST
def AdminSendRequest(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        return render(request,'AdminSendRequest.html', {'admin': getsession})
    return redirect('/adminsignin')

def FuncAdminSendRequest(request):
    if request.method == 'POST':
        vpname = request.POST.get('p_name')
        vpage = request.POST.get('p_age')
        vpgender = request.POST.get('p_gender')
        vpcontact = request.POST.get('p_contact')
        vbloodneeded = request.POST.get('p_blood_needed')
        vpreason = request.POST.get('p_reason')
        vplocation = request.POST.get('p_location')
        obj = AdminBloodRequest()
        obj.p_name = vpname
        obj.p_age = vpage
        obj.p_gender = vpgender
        obj.p_contact = vpcontact
        obj.p_blood_needed = vbloodneeded
        obj.p_reason = vpreason
        obj.p_location = vplocation
        obj.save()
        messages.success(request,'Request Sent!')
        return redirect('/adminsendrequest')

#VIEW USERS
def GetUsers(request):
    if 'Username' in request.session:
        getsession = request.session.get('Username','Guest')
        view_users = SignUp.objects.all()
        return render(request,'ViewEditUsers.html', {'view_data':view_users,'admin': getsession})
    return redirect('/adminsignin')

#REMOVE USERS
def deleteUser(request,uid):
    getdata = SignUp.objects.get(id=uid)
    getdata.delete()
    return redirect('/getusers')

