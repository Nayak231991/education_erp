from django.shortcuts import render,redirect
from .models import Trainer,Course,Student,Batch,FeePay
from django.contrib import messages
import datetime
def home(request):
    return render(request,'addstudent.html')
def addtrainer(request):
    if request.method=='POST':
        t=Trainer()
        t.tname=request.POST['name']
        t.qualification=request.POST['quli']
        t.sal=request.POST['sal']
        t.languages=request.POST['language']
        t.save()
        return redirect("/addtrainer")
    else:
        return render(request,'addtrainer.html')
def showtrainers(request):
    tr=Trainer.objects.all()
    return render(request,'showtrainers.html',{'tr':tr})
def addcourse(request):
    tr=Trainer.objects.all()
    if request.method=='POST':
        c=Course()
        c.cname=request.POST['cname']
        c.duration=request.POST['duration']
        c.fees=request.POST['fees']
        trainers=request.POST.getlist('trainers')
        c.save()
        for i in trainers:
            t=Trainer.objects.filter(id=int(i)).get()
            c.trainers.add(t.id)
        return redirect('/')
    else:
        return render(request,'addcourse.html',{'tr':tr})
def showcourse(request):
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})
def addstudent(request):
    if request.method=='POST':
        s=Student()
        s.sname=request.POST['name']
        s.email=request.POST['email']
        s.mobile=request.POST['mobile']
        s.address=request.POST['address']
        s.dob=request.POST['dob']
        s.college=request.POST['college']
        s.branch=request.POST['branch']
        s.year=request.POST['year']
        s.sem=request.POST['sem']
        s.status=request.POST['status']
        courses=request.POST.getlist('course')
        s.enquirydate=datetime.datetime.now()
        s.save()
        for i in courses:
            t=Course.objects.filter(id=int(i)).get()
            s.cources.add(t.id)
        return redirect("/")
    else:
        cr=Course.objects.all()
        tr=Trainer.objects.all()
        return render(request,'addstudent.html',{'cr':cr,'tr':tr})
def searchstudent(request):
    if request.method=='POST':
        sname=request.POST['name']
        st=Student.objects.filter(sname=sname).all()
        return render(request,'showstudent.html',{'st':st})
    else:
        return render(request,'searchstudent.html')
def searchenquiry(request):
    if request.method=='POST':
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=Student.objects.filter(enquirydate__range=(fdt, tdt)).all()
        return render(request,'showstudent.html',{'st':st})
    else:
        return render(request,'searchenquiry.html')
def createbatch(request):
    if request.method=='POST':
        b=Batch()
        b.bname=request.POST['bname']
        b.batchstatus=request.POST['status']
        b.time=request.POST['time']
        b.startdate=request.POST['date']
        tid=request.POST['trainers']
        students=request.POST.getlist('students')
        t=Trainer.objects.filter(id=int(tid)).get()
        b.trainer=t
        b.save()
        for i in students:
            s=Student.objects.filter(id=int(i)).get()
            b.students.add(s.id)
        return redirect('/')
    else:
        st=Student.objects.all()
        tr=Trainer.objects.all()
        return render(request,'createbatch.html',{'st':st,'tr':tr})
def feepay(request):
    if request.method=='POST':
        f=FeePay()
        f.pay=request.POST['pay']
        f.fees=request.POST['total']
        f.remaining=request.POST['remaining']
        id=students=request.POST['students']
        f.student=Student.objects.filter(id=int(id)).get()
        f.fdate=datetime.datetime.now()
        f.save()
        return redirect("/")
    else:
        st=Student.objects.all()
        return render(request,'feepay.html',{'st':st})
def showtrans(request):
    if request.method=='POST':
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=FeePay.objects.filter(fdate__range=(fdt, tdt)).all()
        s=0
        for i in st:
            s=s+i.pay
        print(s)
        return render(request,'showt.html',{'total':s,'st':st})
    else:
        return render(request,'showtrans.html')