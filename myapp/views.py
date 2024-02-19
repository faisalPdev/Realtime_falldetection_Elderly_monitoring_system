from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'login_index.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=Login.objects.filter(username=username,Password=password)
    if res.exists():
        ress=Login.objects.get(username=username,Password=password)
        request.session['lid']=ress.id
        if ress.type=='admin':
            return redirect('/myapp/admin_home/')
    return HttpResponse('''<script>alert("Invalid user");window.location='/myapp/login/'</script>''')

def admin_home(request):
    return render(request,'admin_home.html')

def add_caregiver(request):
    return render(request,'add_caregiver.html')

def add_caregiver_post(request):
    Name=request.POST['textfield']
    Place=request.POST['textfield2']
    Pin=request.POST['textfield3']
    Post=request.POST['textfield4']
    HouseName=request.POST['textfield5']
    Gmail=request.POST['textfield6']
    Phone=request.POST['textfield7']
    Gender=request.POST['RadioGroup1']
    Age=request.POST['textfield9']
    photo=request.FILES['fileField']

    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,photo)
    path=fs.url(date)

    l=Login()
    l.username=Gmail
    import random
    password=random.randint(0000,9999)
    l.Password=str(password)
    l.type='caregiver'
    l.save()

    c=Caregiver()
    c.LOGIN=l
    c.name=Name
    c.place=Place
    c.pin=Pin
    c.post=Post
    c.Housename=HouseName
    c.gmail=Gmail
    c.phone_no=Phone
    c.Gender=Gender
    c.age=Age
    c.photo=path
    c.save()

    return HttpResponse('OK')

def add_elderlyperson(request):
    return render(request,'add_elderlyperson.html')

def add_elderlyperson_post(request):
    Name = request.POST['textfield']
    Place = request.POST['textfield2']
    Pin = request.POST['textfield3']
    Post = request.POST['textfield4']
    HouseName = request.POST['textfield5']
    Gmail = request.POST['textfield6']
    Phone = request.POST['textfield7']
    Guardian = request.POST['textfield8']
    Gender = request.POST['RadioGroup1']
    Age = request.POST['textfield9']
    photo = request.FILES['fileField']
    fs=FileSystemStorage()
    date='Elderly_person/'+datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fn=fs.save(date,photo)
    path=fs.url(date)


    l = Login()
    l.username = Gmail
    import random
    password = random.randint(0000, 9999)
    l.Password = str(password)
    l.type = 'Elderly Person'
    l.save()

    c=Elderly_person ()
    c.LOGIN=l
    c.name = Name
    c.place = Place
    c.pin = Pin
    c.post = Post
    c.Housename = HouseName
    c.gmail = Gmail
    c.phone_no = Phone
    c.guardian_details=Guardian
    c.Gender = Gender
    c.age = Age
    c.photo = path
    c.save()

    return HttpResponse('OK')

def change_password(request):
    return render(request,'change_password.html')

def change_password_post(request):
    Current_password = request.POST['textfield']
    New_password = request.POST['textfield2']
    Confirm_password=request.POST['textfield3']

    res=Login.objects.filter(id=request.session['lid'],Password=Current_password)
    if New_password==Confirm_password:
        res = Login.objects.filter(id=request.session['lid'], Password=Current_password).update(Password=Confirm_password)
        return  HttpResponse('''<script>alert("Succesfuly updated the password");window.location='/myapp/login/'</script>''')
    return HttpResponse('''<script>alert("confirm password must be equal to new password");window.location='/myapp/change_password_post/'</script>''')


def add_allocation(request,cid):
    res=Elderly_person.objects.all()
    return render(request,'add_allocation.html',{"data":res,"cid":cid})

def add_allocation_post(request):
    elder_id=request.POST['elderly_person']
    care_id=request.POST['c_id']
    enddate=request.POST['enddate']
    alloc=Allocation()
    alloc.CAREGIVER_id=care_id
    alloc.ELDERLY_PERSON_id=elder_id
    alloc.start_date=datetime.now()
    alloc.end_date=enddate
    alloc.save()
    return HttpResponse('''<script>alert("Succesfuly adedd the allocation");window.location='/myapp/view_allocated/'</script>''')

def view_allocated(request):
    res=Allocation.objects.all()
    return render(request,'view_allocated.html',{"data":res})

def view_caregiver(request):
    res=Caregiver.objects.all()
    return render(request,'view_caregiver.html',{"data":res})

def view_elderlyperson(request):
    res=Elderly_person.objects.all()
    return render(request,'view_elderlyperson.html',{"data":res})

def edit_caregiver(request,id):
    res=Caregiver.objects.get(id=id)
    return render(request,'edit_caregiver.html',{"data":res})

def edit_caregiver_post(request):
    Name = request.POST['textfield']
    Place = request.POST['textfield2']
    Pin = request.POST['textfield3']
    Post = request.POST['textfield4']
    HouseName = request.POST['textfield5']
    Gmail = request.POST['textfield6']
    Phone = request.POST['textfield7']
    Gender = request.POST['RadioGroup1']
    Age = request.POST['textfield9']

    cid=request.POST['id']
    c = Caregiver.objects.get(id=cid)
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fn = fs.save(date, photo)
        path = fs.url(date)
        c.photo = path
        c.save()
    c.name = Name
    c.place = Place
    c.pin = Pin
    c.post = Post
    c.Housename = HouseName
    c.gmail = Gmail
    c.phone_no = Phone
    c.Gender = Gender
    c.age = Age
    c.save()
    return HttpResponse('OK')

def delete_caregiver(request,id):
    res = Caregiver.objects.filter(id=id).delete()
    return HttpResponse('OK')

def edit_elderlyperson(request,id):
    res=Elderly_person.objects.get(id=id)
    return render(request,'edit_elderlyperson.html',{"data":res})

def edit_elderlyperson_post(request):
    Name = request.POST['textfield']
    Place = request.POST['textfield2']
    Pin = request.POST['textfield3']
    Post = request.POST['textfield4']
    HouseName = request.POST['textfield5']
    Gmail = request.POST['textfield6']
    Phone = request.POST['textfield7']
    Guardian = request.POST['textfield8']
    Gender = request.POST['RadioGroup1']
    Age = request.POST['textfield9']

    cid = request.POST['id']
    c = Elderly_person.objects.get(id=cid)
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        date = 'Elderly_person/' + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fn = fs.save(date, photo)
        path = fs.url(date)
        c.photo = path
        c.save()

    c.name = Name
    c.place = Place
    c.pin = Pin
    c.post = Post
    c.Housename = HouseName
    c.gmail = Gmail
    c.phone_no = Phone
    c.guardian_details = Guardian
    c.Gender = Gender
    c.age = Age
    c.save()

    return HttpResponse('OK')

def delete_elderlyperson(request,id):
    res=Elderly_person.objects.filter(id=id).delete()

    return HttpResponse('OK')

# def logout(request):
#     ret