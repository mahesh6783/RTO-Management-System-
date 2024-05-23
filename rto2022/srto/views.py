from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from srto.forms import RtofficeForm, TaxForm, LicenseForm, EmployeeForm, DealerForm, LeanersForm, LapptableForm,VehicleForm, QuestionForm,DrivingForm
from srto.models import Rtoffice,Taxrate,Licenserate, Useraccount, Employee, Dealers, Leaners ,Lapptable, Vehicleregister, Question, Drivinglicense
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.db.models import Avg, Max, Min
from datetime import datetime, timedelta
import time
# Create your views here.

def index(request):
    return render(request,'rto/home.html')

def aboutus(request):
    return render(request,'rto/AboutUs.html')

def addrtoffice(request):
    if request.method == "POST":
        form = RtofficeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showrt/')
            except:
                pass
    else:
        form = RtofficeForm()
    return render(request,'rto/addrto.html',{'form':form})

def showrtoffice(request):
    rtos = Rtoffice.objects.all()
    return render(request,"rto/showrto.html",{'rtos':rtos})

def editrtoffice(request, rcode):
    rtos = Rtoffice.objects.get(rcode=rcode)
    form=RtofficeForm(instance = rtos)
    return render(request,'rto/editrto.html', {'form':form,'rcode': rcode})

def updatertoffice(request, rcode):
    rtos = Rtoffice.objects.get(rcode=rcode)
    form = RtofficeForm(request.POST, instance = rtos)
    if form.is_valid():
        form.save()
        return redirect("/showrt/")
    return render(request, 'rto/editrto.html', {'rcode': rcode})

def destroyrtoffice(request, rcode):
    rtos = Rtoffice.objects.get(rcode=rcode)
    rtos.delete()
    return redirect("/showrt/")

## tax rate
#
#

def addtax(request):
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showtax/')
            except:
                pass
    else:
        form = TaxForm()
    return render(request,'tax/addrto.html',{'form':form})

def showtax(request):
    rtos = Taxrate.objects.all()
    return render(request,"tax/showrto.html",{'rtos':rtos})

def edittax(request, taxcode):
    rtos = Taxrate.objects.get(taxcode=taxcode)
    form=TaxForm(instance = rtos)
    return render(request,'tax/editrto.html', {'form':form,'taxcode':taxcode})

def updatetax(request, taxcode):
    rtos = Taxrate.objects.get(taxcode=taxcode)
    form = TaxForm(request.POST, instance = rtos)
    if form.is_valid():
        form.save()
        return redirect("/showtax/")
    return render(request, 'tax/editrto.html', {'rtos': rtos})

def destroytax(request, taxcode):
    rtos = Taxrate.objects.get(taxcode=taxcode)
    rtos.delete()
    return redirect("/showtax/")

## License Rate
##
##
def addlic(request):
    if request.method == "POST":
        form = LicenseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showlic/')
            except:
                pass
    else:
        form = LicenseForm()
    return render(request,'licence/addrto.html',{'form':form})

def showlic(request):
    rtos = Licenserate.objects.all()
    return render(request,"licence/showrto.html",{'rtos':rtos})

def editlic(request, id):
    rtos = Licenserate.objects.get(lcode=id)
    form=LicenseForm(instance = rtos)
    return render(request,'licence/editrto.html', {'form':form,'id':id})

def updatelic(request, id):
    rtos = Licenserate.objects.get(lcode=id)
    form = LicenseForm(request.POST, instance = rtos)
    if form.is_valid():
        form.save()
        return redirect("/showlic/")
    return render(request, 'licence/editrto.html', {'rtos': rtos})

def destroylic(request, id):
    rtos = Licenserate.objects.get(lcode=id)
    rtos.delete()
    return redirect("/showlic/")

## report section
## report section

def viewoffices(request):
    rtos = Rtoffice.objects.all()
    return render(request,"reports/rtoreport.html",{'rtos':rtos})

def viewtaxrate(request):
    rtos = Taxrate.objects.all()
    return render(request,"reports/taxreport.html",{'rtos':rtos})

def viewlicenserate(request):
    rtos = Licenserate.objects.all()
    return render(request,"reports/licensereport.html",{'rtos':rtos})

## Employee Registration
## Dealer Registrstion

def employeeregistation(request):
    submitted=False
    if request.method =='POST':
        form= EmployeeForm(request.POST)
        if form.is_valid():
            un=request.POST.get('u')
            pn=request.POST.get('p')
            cd= form.cleaned_data
            jss = str(cd['rcode'])
            ac= Useraccount(uname=un, pword= pn, rights='EN', ids =cd['adharno'],rcode=jss )
            ac.save()
            form.save()
            return HttpResponseRedirect('/add_emp/?submitted=True')
    else:
        form = EmployeeForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'registration/addemp.html',{'form': form, 'submitted': submitted})

def printemployee(request):
    objectlist= Employee.objects.filter(status="EN")
    return render(request, 'registration/Applicationpage.html', {"objectlist": objectlist})

class Appoint(UpdateView):
    template_name = 'registration/empedit.html'
 #  form_class = EmployeeForm
    model = Employee
    fields = "__all__"
    slug_field = 'adharno'
    slug_url_kwarg = 'adharno'

    def form_valid(self, form):
        post = form.save(commit=False)
        id=post.adharno
        sts=post.status
        Useraccount.objects.filter(ids=id, rights='EN').update(rights=sts)
 #       print(id)
 #       print(sts)
        post.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/printemp')

    def get_success_url(self):
         return "http://127.0.0.1:8000/printemp"

## Dealer Section

def dealerregistation(request):
    submitted=False
    if request.method =='POST':
        form= DealerForm(request.POST)
        if form.is_valid():
            un=request.POST.get('u')
            pn=request.POST.get('p')
            cd= form.cleaned_data
            jss = str(cd['rcode'])
            ac= Useraccount(uname=un, pword= pn, rights='DN', ids =cd['dcode'],rcode=jss)
            ac.save()
            form.save()
            return HttpResponseRedirect('/add_dealer/?submitted=True')
    else:
        form= DealerForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'registration/adddealer.html',{'form': form, 'submitted': submitted})


def printdealers(request):
 #   drcode= request.session.get('rcode')
 #   rcode=drcode,
    objectlist= Dealers.objects.filter( status="DN")
    return render(request, 'registration/dealerapplication.html', {"objectlist": objectlist})


class Appointdealers(UpdateView):
    template_name = 'registration/dealeredit.html'
 #  form_class = EmployeeForm
    model = Dealers
    fields = "__all__"
    slug_field = 'dcode'
    slug_url_kwarg = 'dcode'

    def form_valid(self, form):
        post = form.save(commit=False)
        id=post.dcode
        sts=post.status
        Useraccount.objects.filter(ids=id, rights='DN').update(rights=sts)
 #       print(id)
 #       print(sts)
        post.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/printdealer')

    def get_success_url(self):
         return "http://127.0.0.1:8000/printdealer"
# LOGIN SECTION


class HomePageView(TemplateView):
    template_name = 'registration/loginPage.html'

def SearchResultsView(request):
    query = request.GET.get('u')
    query1= request.GET.get('p')
    object_list = Useraccount.objects.filter(uname=query, pword=query1)
  #  print (object_list[0])
    if object_list.filter(uname=query, pword =query1).exists():
        for event in object_list:
            x=event.ids
            y= event.rights
            r =event.rcode
            request.session['un']=query
            request.session['pw']=query1
            request.session['ids'] = x
            request.session['ri']=y
            request.session['rcode'] = r

        if object_list.filter(rights='A').exists():
            return render(request, 'registration/AdminPage.html')
        elif object_list.filter(rights='E').exists():
            data = Employee.objects.filter(adharno=x)
            for ev in data:
                shid = ev.ename
            request.session['names'] = shid
            return render(request, 'registration/EmployeePage.html',{"data": data})
        elif object_list.filter(rights='D').exists():
            data=Dealers.objects.filter(dcode=x)
            for ev in data:
                shid=ev.dname
            request.session['names'] = shid
            return render(request, 'registration/DealerPage.html', {"data": data})
        elif object_list.filter(rights='U').exists():
            return render(request, 'registration/UserPage.html')
        elif y=="EN" or y=="DN":
            return render(request, 'registration/WaitPage.html')
        elif y=="R":
            return render(request, 'registration/RejectPage.html')
    else:
        return render(request, 'registration/notfound.html')

#
# Leaners Application Section
#

def selectlicrate(request):
    rtos = Licenserate.objects.all()
    return render(request,"leanersapp/showlicencerate.html",{'rtos':rtos})

def displayleanersapp(request, id):
    submitted=False
    if request.method =='POST':
        form= LapptableForm(request.POST)
        if form.is_valid():
            un=request.POST.get('u')
            pn=request.POST.get('p')
            lc=request.POST.get('lc')
            ln=request.POST.get('ln')
            lf = request.POST.get('lf')
            cd= form.cleaned_data
            jss = str(cd['rcode'])
            ar=cd['adharno']
            ac= Useraccount(uname=un, pword= pn, rights='U', ids =cd['adharno'],rcode=jss )
            ac.save()
            form.save()
            appdate =datetime.today()
            licdate= appdate + timedelta(20)
            rec= Lapptable.objects.all().aggregate(Max('id'))
            next_order = rec['id__max']
            Lapptable.objects.filter(id=next_order).update(lcode=lc, lname=ln,amtpaid=lf,testdate=licdate)
            Useraccount.objects.filter(uname=un, pword= pn, rights='U', ids =ar,rcode=jss).update(ids=next_order)
            apno="Your Application No %s " %(next_order)
            testdate = "Leaners Test on - %s" % (licdate)
 #           return HttpResponse("<h1> %s </h1><p> %s</p>" % (apno,testdate))
            return render(request,'leanersapp/mesg.html',{'apno':apno,'testdate':testdate})
    else:
        form = LapptableForm()
        if 'submitted' in request.GET:
            submitted=True
    rrtos = Licenserate.objects.filter(lcode=id)
    for event in rrtos:
        lcode = event.lcode
        lname = event.lname
        lfee = event.lfee
    return render(request,'leanersapp/applyleaners.html',{'form': form, 'lcode': lcode, 'lname':lname, 'lfee':lfee, 'submitted': submitted})


#
#vehicle registration
#

def viewvehicletax(request):
    taxrec=Taxrate.objects.all()
    if request.method=="POST":
        vn=request.POST.get('vname')
        veng=request.POST.get('veng')
        vchno=request.POST.get('vchass')
        vyear = request.POST.get('vyear')
        vmonth = request.POST.get('vmonth')
        pr = request.POST.get('price')
        tcode = request.POST.get('txcode')
        rtos = Taxrate.objects.filter(taxcode=tcode)
        for i in rtos:
            per= i.taxp
            dur= i.duration
        percent=int( pr) * int(per) / 100
        taxs = int(percent) * int(dur)
        dcode = request.session['ids']
        rtocode=request.session['rcode']
        vreg = Vehicleregister(rcode=rtocode, dcode=dcode, vname=vn, eno=veng, chno=vchno, ymanu=vyear, mnamu=vmonth, taxcode=tcode, vprice=pr,tax=taxs)
        vreg.save()
        rec = Vehicleregister.objects.all().aggregate(Max('id'))
        id = rec['id__max']
        vregs = Vehicleregister.objects.get(id=id)
        form = VehicleForm(instance=vregs)
        return render(request, 'vehiclereg/editvehicle.html', {'form': form, 'id': id})
 #       return HttpResponse("<h1> %s </h1><p> %s</p>" % (dcode, rtocode))
    else:
        return render(request, 'vehiclereg/selectvehicle.html', {"taxrec":taxrec})

def vehcashupdation(request, id):
    rtos = Vehicleregister.objects.get(id=id)
    form = VehicleForm(request.POST, instance = rtos)
    if form.is_valid():
        un = request.POST.get('un')
        pn = request.POST.get('ps')
        jss = request.session['rcode']
        ac = Useraccount(uname=un, pword=pn, rights='VU', ids=id, rcode=jss)
        ac.save()
        form.save()
        Vehicleregister.objects.filter(id=id).update(status='P')
        apno = "Your Application No %s is submitted successfully" % (id)
        return HttpResponse("<h1> %s </h1>" % (apno))
    return render(request, 'vehiclereg/editvehicle.html', {'form': form, 'id': id})


def empnumissue(request):
    newrec= Vehicleregister.objects.filter(status='P')
    if 'find' in request.POST:
        vn = request.POST.get('appno')
        mrec=Vehicleregister.objects.filter(id=vn)
        for x in mrec:
            rtocode=x.rcode
            tcode=x.taxcode
        no=Vehicleregister.objects.filter(rcode=rtocode).aggregate(Max('regno'))
        vhno = no['regno__max']
        vhno= int(vhno)+1
        printno= rtocode+" "+ str(vhno)
        tax = Taxrate.objects.filter(taxcode=tcode)
        for i in tax:
            dur = i.duration
        da = int(dur) * 365
        fromdate = datetime.today()
        todate = fromdate + timedelta(da)
        vc=Vehicleregister.objects.filter(id=vn).update(regno=vhno,vfrom=fromdate, vto=todate,status='I')
        vrec = Vehicleregister.objects.get(id=vn)
#       vrec = Vehicleregister.objects.filter(id=vn).first()
        form = VehicleForm(instance=vrec)
        return render(request,'vehiclereg/vnumbering.html', {'form': form,'vn':vn, 'printno':printno,'fromdate':fromdate,'todate':todate, 'newrec': newrec})
    #    return HttpResponse("<h1> Add button click </h1>" )
#    if 'mul' in request.POST:
#        return HttpResponse("<h1> Multiply  button click </h1>")
    return render(request,'vehiclereg/vnumbering.html',{'newrec': newrec})

#
# QUESTION PAPER SECTION
#

def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showquest/')
            except:
                pass
    else:
        form = QuestionForm()
    return render(request,'questionbank/addquestion.html',{'form':form})

def showquestion(request):
    rtos = Question.objects.all()
    return render(request,"questionbank/showquestion.html",{'rtos':rtos})

def editquestion(request, id):
    rtos = Question.objects.get(id=id)
    form=QuestionForm(instance = rtos)
    return render(request,'questionbank/editquestion.html', {'form':form,'id': id})

def updatequestion(request, id):
    rtos = Question.objects.get(id=id)
    form = QuestionForm(request.POST, instance = rtos)
    if form.is_valid():
        form.save()
        return redirect("/showquest/")
    return render(request, 'questionbank/editquestion.html', {'id': id})

def destroyquestion(request, id):
    rtos = Question.objects.get(id=id)
    rtos.delete()
    return redirect("/showquest/")


def leanersexam(request):
    appno = request.session['ids']
    rto  =  request.session['rcode']
 #   while True:
 #       localtime = time.localtime()
 #       result = time.strftime("%I:%M:%S %p", localtime)
 #       print(result)
 #       time.sleep(1)

    if request.method == "POST":
        qno=request.POST.get('qno')
        aname=request.POST.get('aname')
        opt=request.POST.get('opts')
        score=request.POST.get('score')
        ans=request.session['ans']
        if not opt:
            opt=0
        if int(opt)==int(ans):
            score = int(score) +1
        qno= int(qno)+1
        if int(qno) > 20 or int(score)>=11:
           if int(score)>=11:
               ln = Lapptable.objects.filter(rcode=rto).aggregate(Max('lno'))
               lcno = ln['lno__max']
               lcno = int(lcno) + 1
               printno = rto + " " + str(lcno)
               fromdate = datetime.today()
               todate = fromdate + timedelta(180)
               vc = Lapptable.objects.filter(id=appno).update(lno=lcno, vfrom=fromdate, vto=todate, status='L')
               result = "Congratulation Your License No  %s \n Validity from %s to %s " % (printno,fromdate,todate)
               return render(request, 'leanerstest/issue.html',{'appno': appno, 'rto': rto, 'aname': aname, 'printno': printno, 'fromdate': fromdate, 'todate': todate})

           if int(qno>20):
               fromdate = datetime.today()
               todate = fromdate + timedelta(20)
               vc = Lapptable.objects.filter(id=appno).update(testdate=todate)
               result = "Sorry next testdate  %s " % ( todate)
               return render(request, 'leanerstest/failed.html',{'appno': appno, 'rto': rto, 'aname': aname, 'result': result})

        quest = Question.objects.filter(qno=qno)
        for i in quest:
            qno=i.qno
            qname=i.qname
            op1=i.op1
            op2=i.op2
            op3=i.op3
            op4=i.op4
            ans=i.ans
#        request.session['qno'] = qno
        request.session['ans']=ans
#        request.session['score']=score
#        request.session['aname']=aname
        return render(request, 'leanerstest/leanerstest.html',
                      {'appno': appno, 'rto': rto, 'aname': aname, 'qno': qno, 'qname': qname, 'op1': op1, 'op2': op2,
                       'op3': op3, 'op4': op4, 'score': score})
    else:
        score = 0
        rec = Lapptable.objects.filter(id=appno)
        for j in rec:
            aname=j.aname
            sts=j.status
            lno=j.lno
            vfrom=j.vfrom
            vto=j.vto

        if sts=="L" or sts=="DA":
            return render(request, 'leanerstest/already.html',
                          {'appno': appno, 'rto': rto, 'aname': aname, 'lno': lno, 'vfrom': vfrom, 'vto': vto})
        quest = Question.objects.filter(qno=1)
        for i in quest:
            qno=i.qno
            qname=i.qname
            op1=i.op1
            op2=i.op2
            op3=i.op3
            op4=i.op4
            ans=i.ans
#        request.session['qno'] = qno
        request.session['ans']=ans
#        request.session['score']=score
#        request.session['aname']=aname
    return render(request,'leanerstest/leanerstest.html',{'appno':appno,'rto': rto,'aname':aname,'qno':qno, 'qname':qname,'op1':op1,'op2':op2,'op3':op3,'op4':op4,'score':score})


def drivingLicense(request):
    appno = request.session['ids']
    rto  =  request.session['rcode']
    licrec = Licenserate.objects.all()
    rec = Lapptable.objects.filter(id=appno)
    for j in rec:
        aname = j.aname
        sts = j.status
        lno = j.lno
        vfrom = j.vfrom
        vto = j.vto
        ph=j.phone
        em=j.email
    if sts == "N":
        return render(request, 'leanerstest/takeleaners.html')
    if sts =="D":
        drec=Drivinglicense.objects.filter(lno=lno)
        for k in drec:
            dlno=k.dlno
            lname=k.lname
            vfrom= k.vfrom
            vto= k.vto
        return render(request, 'leanerstest/alreadydriving.html',{'aname':aname,'rto':rto,'dlno':dlno,'vfrom':vfrom,'vto':vto})
    if sts=='DA':
        return render(request,"leanerstest/drivingapplied.html")
    if request.method == "POST":
        lcode = request.POST.get('lcode')

        if 'find' in request.POST:
            raterec = Licenserate.objects.filter(lcode=lcode)
            for event in raterec:
                lcode = event.lcode
                lname = event.lname
                lfee = event.lfee
            return render(request, 'leanerstest/drivinglicense.html',{'lcode': lcode, 'lname': lname, 'lfee': lfee,'lno':lno, 'vfrom': vfrom, 'vto': vto,'rto':rto,'aname':aname,'ph':ph,'em':em,'licrec':licrec})
        if "save" in request.POST:
            apdate= datetime.today()
            lname=request.POST.get('lname')
            amt = request.POST.get('lfee')
            carno = request.POST.get('cardno')
            aname = request.POST.get('aname')
            ltcode=request.POST.get('ltcode')
            driving = Drivinglicense(lno=lno,apdate=apdate,lcode=ltcode,lname=lname,amt=amt,cardno=carno,aname=aname,rcode=rto,status='N')
            driving.save()
            vc = Lapptable.objects.filter(id=appno).update(status='DA')
            return render(request,"leanerstest/applied.html")
    else:
        return render(request,'leanerstest/drivinglicense.html',{'licrec':licrec})

def issuedrivinglic(request):
    drec = Drivinglicense.objects.filter(status='N')
    rto  =  request.session['rcode']
    if request.method == "POST":
        if 'find' in request.POST:
            lno=request.POST.get('lno')
            apprec = Drivinglicense.objects.filter(lno=lno)
            for event in apprec:
                adate=event.apdate
                ltcode = event.lcode
                lname = event.lname
                amt = event.amt
                cardno=event.cardno
                aname = event.aname
                rto=event.rcode
            return render(request, 'leanerstest/issuedrivinglicense.html',
                          {'lno': lno, 'adate':adate,'ltcode':ltcode,'lname': lname, 'amt': amt,'cardno': cardno, 'aname': aname,'rto':rto, 'drec': drec})
        if "pass" in request.POST:
            lno= request.POST.get('tlno')
            apdate = datetime.today()
            apprec = Drivinglicense.objects.filter(lno=lno)
            for event in apprec:
                adate = event.apdate
                ltcode = event.lcode
                lname = event.lname
                amt = event.amt
                cardno = event.cardno
                aname = event.aname
                rto = event.rcode
                ln = Drivinglicense.objects.filter(rcode=rto).aggregate(Max('dlno'))
                lcno = ln['dlno__max']
                lcno = int(lcno) + 1
                dlno = rto + " " + str(lcno)
                vfrom = datetime.today()
                vto = vfrom + timedelta(10950)
                vc = Drivinglicense.objects.filter(lno=lno).update(dlno=lcno, vfrom=vfrom, vto=vto, status='D')
            return render(request, 'leanerstest/issuedrivinglicense.html',
                          {'lno': lno, 'adate': adate, 'ltcode': ltcode, 'lname': lname, 'amt': amt, 'cardno': cardno,'dlno':dlno,'vfrom':vfrom,'vto':vto,'aname': aname, 'rto': rto, 'drec': drec})

    return render(request,'leanerstest/issuedrivinglicense.html',{'drec':drec})


def printleaners(request):
    appno = request.session['ids']
    rto  =  request.session['rcode']
    rec = Lapptable.objects.filter(id=appno)
    for j in rec:
        aname = j.aname
        sts = j.status
        lno = j.lno
        vfrom = j.vfrom
        vto = j.vto
    if sts == "L" or sts == "DA":
        return render(request, 'leanerstest/already.html',
                      {'appno': appno, 'rto': rto, 'aname': aname, 'lno': lno, 'vfrom': vfrom, 'vto': vto})

    else:
        return render(request, 'leanerstest/notfound.html')

def printdriving(request):
    appno = request.session['ids']
    rto = request.session['rcode']
    rec = Lapptable.objects.filter(id=appno)
    for j in rec:
        lno = j.lno
    apprec = Drivinglicense.objects.filter(lno=lno,rcode=rto)
    sts="k"
    for k in apprec:
        sts= k.status

    if sts == "D":
        apprec = Drivinglicense.objects.get(lno=lno,rcode=rto)
        form =DrivingForm (instance=apprec)
        return render(request, 'leanerstest/printdriving.html',{'form':form})
    else:
        return render(request, 'leanerstest/notfound.html')

def changepassword(request):
    uname = request.session['un']
    pword = request.session['pw']
    if request.method == "POST":
        oldp = request.POST.get('a')
        newp = request.POST.get('b')
        rp= request.POST.get('c')
        if(pword==oldp):
            if(newp==rp):
                vc = Useraccount.objects.filter(uname=uname).update(pword=newp)
                return render(request, 'reports/successpass.html')
            else:
                return render(request, 'reports/missmatch.html')
        else:
            return render(request, 'reports/invalidpass.html')
    return render(request, 'registration/changepassword.html')


def printveh(request):
    dcode= request.session['ids']
    drec = Vehicleregister.objects.filter(dcode=dcode)
    return render(request, 'vehiclereg/printveh.html', {'drec': drec})
