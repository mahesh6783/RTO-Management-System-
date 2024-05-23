from django.db import models
from django.utils import timezone
from datetime import date


dealerchoice =(
    ("DN", "DN"),
    ("R", "Rejected"),
    ("D", "Approved"),
)
empchoice =(
    ("EN", "EN"),
    ("R", "Rejected"),
    ("E", "Appoint"),
)
job = (
    ('Nil', 'Nil'),
    ('RTO', 'RTO'),
    ('JRTO', 'JRTO'),
    ('ACCOUNTANT', 'ACCOUNTANT'),
    ('TYPIST', 'TYPIST'),
)
sex = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('None', 'None'),
)
ansopt =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)

# Create your models here.
class Rtoffice(models.Model):
    rcode = models.CharField('RT Office Code',max_length=50, primary_key=True)
    rname = models.CharField('RT Office Name', max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.rcode

class Taxrate(models.Model):
    taxcode = models.IntegerField("Tax Code",primary_key=True)
    vhtype = models.CharField("Type of Vehicle", max_length=100)
    mop = models.CharField("Mode of Operation", max_length=100)
    taxp = models.IntegerField("Tax Percentage")
    duration = models.IntegerField("Validity in Years")
    def __int__(self):
        return self.taxcode

class Licenserate(models.Model):
    lcode = models.IntegerField("License  Code", primary_key=True)
    lname = models.CharField("License Name", max_length=100)
    lfee = models.IntegerField("License Fee")
    validity = models.IntegerField("Validity in Years")
    def __int__(self):
        return self.lcode

class Useraccount(models.Model):
    uname = models.CharField(max_length=100, primary_key=True)
    pword = models.CharField(max_length=100)
    ids = models.CharField(max_length=100)
    rights = models.CharField(max_length=15)
    rcode = models.CharField(max_length=50)
    def __str__(self):
        return self.rights

class Employee(models.Model):
    adharno = models.CharField("Adhar No", max_length=20, primary_key=True )
    ename = models.CharField("Employee Name", max_length=100)
    gender = models.CharField("Gender",max_length=20, choices=sex, default='Male')
    hname = models.CharField("House Name", max_length=100)
    place = models.CharField("Place",max_length=100)
    quali = models.CharField("Qualification",max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    job = models.CharField("Appointed as", max_length=50)
    rcode = models.ForeignKey(Rtoffice, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField("Application Status",max_length=50, choices=empchoice, default='EN')
    def __str__(self):
        return self.ename

class Dealers(models.Model):
    dcode = models.CharField("Dealer Code",max_length=20, primary_key=True)
    dname = models.CharField("Dealers Name",max_length=100)
    place = models.CharField("Building Address",max_length=100)
    phone = models.CharField("Phone No",max_length=15)
    email = models.EmailField()
    rcode = models.ForeignKey(Rtoffice,blank=True,null=True, on_delete=models.CASCADE)
    status = models.CharField("Application Status",max_length=50, choices=dealerchoice, default='DN')
    def __str__(self):
        return self.dname

class Leaners(models.Model):
    adate =  models.DateField("Application Date", default = date.today)
    rcode =models.ForeignKey(Rtoffice, on_delete=models.CASCADE)
    aname = models.CharField("Name of the Applicant",max_length=50)
    dob = models.DateField("Date of Birth")
    gender= models.CharField("Gender",max_length=20, choices=sex, default='Male')
    fname = models.CharField("Father's Name",max_length=50)
    address = models.CharField("Address",max_length=100)
    adharno = models.CharField("Adhar No", max_length=20)
    quali= models.CharField("Qualification", max_length=50)
    lcode = models.IntegerField()
    lname =models.CharField(max_length=50)
    cardno=models.CharField("Credit Card No",max_length=20)
    amtpaid = models.IntegerField()
    testdate = models.DateField()
    score =models.IntegerField(default=0)
    lno = models.IntegerField(default=0)
    vfrom = models.DateField()
    vto = models.DateField()
    status = models.CharField(max_length=50, default='N')

    def __str__(self):
        return self.aname

class Lapptable(models.Model):
    adate =  models.DateField("Application Date", default = date.today)
    rcode =  models.ForeignKey(Rtoffice, on_delete=models.CASCADE)
    aname = models.CharField("Name of the Applicant",max_length=50)
    dob = models.DateField("Date of Birth")
    gender= models.CharField("Gender",max_length=20, choices=sex, default='Male')
    fname = models.CharField("Father's Name",max_length=50)
    address = models.CharField("Address",max_length=100)
    adharno = models.CharField("Adhar No", max_length=20)
    quali= models.CharField("Qualification", max_length=50)
    phone =models.CharField("Phone Number",max_length=20,default='XXX')
    email =models.EmailField("Email",max_length=50,default='xxx@xx.com')
    lcode = models.IntegerField(default=0)
    lname =models.CharField(max_length=50, default='x')
    cardno=models.CharField("Credit Card No",max_length=20)
    amtpaid = models.IntegerField(default=0)
    testdate = models.DateField(default = date.today)
    score =models.IntegerField(default=0)
    lno = models.IntegerField("Your License No",default=0)
    vfrom = models.DateField(default = date.today)
    vto = models.DateField(default = date.today)
    status = models.CharField(max_length=50, default='N')

    def __str__(self):
        return self.aname

class Vehicleregister(models.Model):
    appdate = models.DateField("Application Date", default = date.today)
    rcode = models.CharField(max_length=50)
    dcode = models.CharField(max_length=50)
    vname = models.CharField("Vehicle Name",max_length=50)
    eno = models.CharField("Engine No",max_length=25)
    chno = models.CharField("Chaiss No", max_length=25)
    ymanu= models.IntegerField("Year of Manufacturing")
    mnamu = models.IntegerField("Month of Manufacturing")
    taxcode= models.IntegerField("Tax Category")
    vprice =models.IntegerField("Price of the Vehicle")
    tax =models.IntegerField("Tax Amount")
    cardno = models.CharField("Credit Card No", max_length=20)
    oname =models.CharField("Vehicle Owners Name", max_length=100)
    address = models.CharField("Owners Address",max_length=100)
    adharno = models.CharField("Adhar No", max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    regno= models.IntegerField("Reg. No", default=0)
    vfrom = models.DateField(default = date.today)
    vto = models.DateField(default = date.today)
    status= models.CharField(max_length=10, default='N')

    def __str__(self):
        return self.vname

class Question(models.Model):
    qno = models.IntegerField('Question No')
    qname = models.CharField('Question', max_length=250)
    op1 = models.CharField("Option 1", max_length=250)
    op2 = models.CharField("Option 2", max_length=250)
    op3 = models.CharField("Option 3",max_length=250)
    op4 = models.CharField("Option 4",max_length=250)
    ans = models.IntegerField("Answer Option", choices= ansopt, default=1)

    def __str__(self):
        return self.qname

class Drivinglicense(models.Model):
    lno = models.IntegerField("Licence No")
    apdate= models.DateField("Application Date",default = date.today)
    rcode =models.CharField(max_length=50)
    aname =models.CharField(max_length=100)
    lcode = models.IntegerField()
    lname = models.CharField(max_length=100)
    amt = models.IntegerField()
    cardno = models.CharField(max_length=20)
    dlno= models.IntegerField(default=0)
    ldate=models.DateField("Issue Date", default=date.today)
    vfrom = models.DateField(default=date.today)
    vto = models.DateField(default=date.today)
    status = models.CharField(max_length=10, default='N')

    def __int__(self):
        return self.lno



