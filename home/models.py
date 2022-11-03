from django.db import models
class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    sal=models.IntegerField()
    languages=models.CharField(max_length=50)
    def __str__(self):
        return self.tname+" "+self.languages
class Course(models.Model):
    cname=models.CharField(max_length=20)
    duration=models.CharField(max_length=20)
    fees=models.IntegerField()
    trainers=models.ManyToManyField(Trainer)
    def __str__(self):
        return str(self.id)+" "+self.cname+" "+self.duration+" "+str(self.fees)
class Student(models.Model):
    sname=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    college=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    sem=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    cources=models.ManyToManyField(Course)
    enquirydate=models.DateField(auto_now=True)
    status_choice=(
        ('enquiry','enquiry'),
        ('joined','joined')
    )
    status = models.CharField(
        max_length = 20,
        choices = status_choice,
        default = 'enquiry'
        )
    def __str__(self):
        return str(self.id)+" "+self.sname
class FeePay(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    fees=models.IntegerField()
    pay=models.IntegerField()
    remaining=models.IntegerField()
    fdate=models.DateField(auto_now=False, auto_now_add=False)
class Batch(models.Model):
    bname=models.CharField(max_length=20)
    status_batch=(
        ('new','new'),
        ('running','running'),
        ('finished','finished'),
    )
    batchstatus = models.CharField(
        max_length = 20,
        choices = status_batch,
        default = 'new'
        )
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    time=models.CharField(max_length=20)
    students=models.ManyToManyField(Student)
    startdate=models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.bname