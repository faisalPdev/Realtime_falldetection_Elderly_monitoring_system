from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
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
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    return render(request,'add_caregiver.html')

def add_caregiver_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

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

    return HttpResponse('''<script>alert("Added succesfully");window.location='/myapp/view_caregiver/'</script>''')

def add_elderlyperson(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    return render(request,'add_elderlyperson.html')

def add_elderlyperson_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

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

    return HttpResponse('''<script>alert("Added succesfully");window.location='/myapp/view_elderlyperson/'</script>''')

def change_password(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    return render(request,'change_password.html')

def change_password_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    Current_password = request.POST['textfield']
    New_password = request.POST['textfield2']
    Confirm_password=request.POST['textfield3']

    res=Login.objects.filter(id=request.session['lid'],Password=Current_password)
    if New_password==Confirm_password:
        res = Login.objects.filter(id=request.session['lid'], Password=Current_password).update(Password=Confirm_password)
        return  HttpResponse('''<script>alert("Succesfuly updated the password");window.location='/myapp/login/'</script>''')
    return HttpResponse('''<script>alert("confirm password must be equal to new password");window.location='/myapp/change_password_post/'</script>''')


def add_allocation(request,cid):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Elderly_person.objects.all()
    return render(request,'add_allocation.html',{"data":res,"cid":cid})

def add_allocation_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

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
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Allocation.objects.all()
    return render(request,'view_allocated.html',{"data":res})

def view_caregiver(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Caregiver.objects.all()
    return render(request,'view_caregiver.html',{"data":res})

def search_caregiver(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    s=request.POST['textfield']
    res = Caregiver.objects.filter(name__icontains=s)
    return render(request, 'view_caregiver.html', {"data": res})

def view_elderlyperson(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Elderly_person.objects.all()
    return render(request,'view_elderlyperson.html',{"data":res})

def search_elderlyperson(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    s=request.POST['textfield']
    res = Elderly_person.objects.filter(name__icontains=s)
    return render(request, 'view_elderlyperson.html', {"data": res})


def edit_caregiver(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Caregiver.objects.get(id=id)
    return render(request,'edit_caregiver.html',{"data":res})

def edit_caregiver_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

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
    return HttpResponse('''<script>alert("Succesfully edited the Details");window.location='/myapp/view_caregiver/'</script>''')

def delete_caregiver(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res = Caregiver.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Deleted succesfully");window.location='/myapp/view_caregiver/'</script>''')

def edit_elderlyperson(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Elderly_person.objects.get(id=id)
    return render(request,'edit_elderlyperson.html',{"data":res})

def edit_elderlyperson_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

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

    return HttpResponse('''<script>alert("Succesfully edited the Details");window.location='/myapp/view_elderlyperson/'</script>''')

def delete_elderlyperson(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    res=Elderly_person.objects.filter(id=id).delete()

    return HttpResponse('''<script>alert("Deleted succesfully");window.location='/myapp/view_elderlyperson/'</script>''')

def logout(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Login Required");window.location='/myapp/login/'</script>''')

    request.session['lid']=''
    return redirect('/myapp/login/')

#---------------------------------------------------Flutter Login-----------------------------------------------------------------------------------
def login_flutter(request):
    username=request.POST['username']
    password=request.POST['password']
    login=Login.objects.filter(username=username,Password=password)
    if login.exists():
        log=Login.objects.get(username=username,Password=password)
        if log.type=='caregiver':
            lid=log.id
            return JsonResponse({'status':'ok','lid':str(lid),'type':'caregiver'})
        elif log.type=='Elderlyperson':
            lid=log.id
            return JsonResponse({'status':'ok','lid':str(lid),'type':'Elderlyperson'})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status':'no'})


# -----------------------------------------------------------Caregiver----------------------------------------------------------------------------

def view_allocated_elderly_person(request):
    lid=request.POST['lid']
    alloc=Allocation.objects.get(ELDERLY_PERSON__LOGIN_id=lid)

    return JsonResponse({'status':'ok','start_date':alloc.start_date,'end_date':alloc.end_date,'name':alloc.ELDERLY_PERSON.name,'place':alloc.place,'pin':alloc.pin,'post':alloc.post,'Housename':alloc.Housename,'gmail':alloc.gmail,'phone_no':alloc.phone_no,'Gender':alloc.Gender,'age':alloc.age,'photo':alloc.photo,'guardian_details':alloc.guardian_details})


def manual_alert(request):
    return JsonResponse({'status':'ok'})

def communication_caregiver(request):
    return JsonResponse({'status':'ok'})

def medication_remainder_tracking(request):
    date=request.POST['date']
    med_name=request.POST['med_name']
    time=request.POST['time']
    ELDERLYPERSON=request.POST['ELDERLYPERSON']
    med=Medication_remainder()
    med.Date=date
    med.Time=time
    med.ELDERLYPERSON_id=ELDERLYPERSON
    med.Name=med_name
    med.save()
    return JsonResponse({'status':'ok'})

def view_profile_caregiver(request):
    lid=request.POST['lid']
    a=Caregiver.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','name':a.name,'place':a.place,'pin':a.pin,'post':a.post,'Housename':a.Housename,'gmail':a.gmail,'phone_no':a.phone_no,'Gender':a.Gender,'age':a.age,'photo':a.photo})

def change_password_caregiver(request):
    lid=request.POST['lid']
    old_password=request.POST['old_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    change=Login.objects.filter(id=lid,Password=old_password)
    if change.exists():
        c=Login.objects.get(id=lid,Password=old_password)
        if c is not None:
            if new_password==confirm_password:
                c=Login.objects.filter(id=lid,Password=old_password).update(Password=confirm_password)
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status':'no'})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status':'no'})

# -------------------------------------Elderly Person-------------------------------------



def view_allocated_caregiver(request):
    lid = request.POST['lid']
    alloc = Allocation.objects.get(CAREGIVER__LOGIN_id=lid)

    return JsonResponse(
        {'status': 'ok', 'start_date': alloc.start_date, 'end_date': alloc.end_date, 'name': alloc.ELDERLY_PERSON.name,
         'place': alloc.place, 'pin': alloc.pin, 'post': alloc.post, 'Housename': alloc.Housename, 'gmail': alloc.gmail,
         'phone_no': alloc.phone_no, 'Gender': alloc.Gender, 'age': alloc.age, 'photo': alloc.photo})


def sos_manual_alert(request):
    return JsonResponse({'status':'ok'})

def communication_elderlyperson(request):
    return JsonResponse({'status':'ok'})

def medication_remainder(request):
    return JsonResponse({'status':'ok'})

def view_profile_elderlyperson(request):
    lid = request.POST['lid']
    a = Elderly_person.objects.get(LOGIN_id=lid)
    return JsonResponse(
        {'status': 'ok', 'name': a.name, 'place': a.place, 'pin': a.pin, 'post': a.post, 'Housename': a.Housename,
         'gmail': a.gmail, 'phone_no': a.phone_no, 'Gender': a.Gender, 'age': a.age, 'photo': a.photo,'guardian_details':a.guardian_details})


def change_password_elderlyperson(request):
    lid = request.POST['lid']
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    change = Login.objects.filter(id=lid, Password=old_password)
    if change.exists():
        c = Login.objects.get(id=lid, Password=old_password)
        if c is not None:
            if new_password == confirm_password:
                c = Login.objects.filter(id=lid, Password=old_password).update(Password=confirm_password)
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status': 'no'})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})



