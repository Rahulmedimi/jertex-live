from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Serviceprovider,Postmsg,Search,occupations,numberofserviceproviders
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user!=None:
            login(request, user)
            return redirect('feed')
    return render(request,"home.html")

@login_required(login_url='login')
def feed(request):
    text=request.GET.get('q') if request.GET.get('q')!=None else ''
    feedinfo=Postmsg.objects.filter(workname__work__icontains=text)
    info=request.user
    type=info.last_name
    services=occupations.objects.all()
    countposts=Postmsg.objects.all().count()
    number=numberofserviceproviders.objects.all()
    searchinfo=Search.objects.filter(searcheduser=request.user)
    context={'data1':info,'data2':feedinfo,'data4':services,'data5':countposts,'data6':number,'data7':type,'data3':searchinfo}
    return render(request,'feed.html',context)   

    class Meta:
        ordering=['-edited','-posted']


def serviceproviderregister(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        f_name=request.POST.get('f_name')
        age=request.POST.get('age')
        occupation=str(request.POST.get('servicename'))
        experience=int(request.POST.get('experience'))
        l_name='ServiceProvider'
        try:
                 
              b=User.objects.filter(email=email)
              messages.error(request, 'email already exists')   
        except:       
                myuser=User.objects.create_user(username,email,password)
                myuser.first_name=f_name
                myuser.last_name=l_name
                myuser.save()
                serviceuserdetails=User.objects.get(username=username)
                serviceproviderdetails=Serviceprovider.objects.create(f_name=f_name,serviceusername=serviceuserdetails,age=age,occupation=occupation,experience=experience)
                serviceproviderdetails.save()
        number=Postmsg.objects.filter(workname__work=occupation).count()
        try:
             a=numberofserviceproviders.objects.get(workname=occupation)
             a.count=number
             a.save()
           
        except numberofserviceproviders.DoesNotExist:
            countofproviders=numberofserviceproviders.objects.create(workname=occupation,count=number)
            countofproviders.save()
            return redirect('sucesspage')
    return render(request,"serviceproviderregister.html")

def registeroption(request):
    return render(request,'registeroption.html')    

def socialaccountsconsumer(request):
    return render(request,'socialaccountlogin.html') 

def consumerregister(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         email=request.POST.get('email')
         f_name=request.POST.get('f_name')
      
         l_name='consumer'
         try:
            a=User.objects.filter(username=username)
            messages.error(request, 'Usarname already exists')
            b=User.objects.filter(email=email)
            messages.error(request, 'email already exists') 
         except: 
             
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=f_name
            myuser.last_name=l_name
            myuser.save()
            return redirect('sucesspage')  



    return render(request,'consumerregister.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(request,username=username,password=password)
        if myuser!=None:
            login(request,myuser)
            return redirect('feed')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("home")    

def userprofile(request):
    return render(request,'profile.html')

def orderservice(request):
    
    return render(request,'orderservice.html')    

def serviceproviderinfo(request,text):
    providerdetails=User.objects.get(username=text)
    moredetails=Serviceprovider.objects.get(serviceusername=providerdetails)
    context={'data1':providerdetails,'data2':moredetails}
    return render(request,'serviceproviderinfo.html',context)

def sucesspage(request):
    return render(request,'sucesspage.html')

def serviceproviderpost(request):
    if request.method=='POST':
        host=request.user
        servicename=request.POST.get('servicename')
        try:
             worknameinstance=occupations.objects.get(work=servicename)
        except occupations.DoesNotExist:
             workname=occupations.objects.create(work=servicename)
             workname.save()
             worknameinstance=occupations.objects.get(work=servicename)
        costdetails=request.POST.get('costingdetails')
        msg=request.POST.get('msgtext')
        post=Postmsg.objects.create(host=host,workname=worknameinstance,message=msg)
        post.save()
        number=Postmsg.objects.filter(workname__work=servicename).count()  
        try:
             a=numberofserviceproviders.objects.get(workname=servicename)
             a.count=number
             a.save()
             return redirect('feed')
           
        except numberofserviceproviders.DoesNotExist:
            countofproviders=numberofserviceproviders.objects.create(workname=servicename,count=number)
            countofproviders.save()
            return redirect('feed')
    return render(request,'serviceproviderpost.html')    

