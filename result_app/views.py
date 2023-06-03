from django.shortcuts import render,redirect
from result_app.models import Result,User,LevelClass,Student,Fee
from result_app.forms import SignupForm,EditResultForm,AddFeeForm,EditFeeForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from result_app.forms import ResultForm,EditParentForm
from datetime import datetime,date,time,timedelta
from django.views.generic import DetailView,ListView
from django.template import loader
import pdfkit
import io
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def home(request): 
    results=Result.objects.all() 
    return render(request,'home.html',{'results':results})

def result(request):
    form=ResultForm()
    email=None
    comment=''
    stud_name=None
    arithmetic_marks=None
    arithmetic_grade=''
    arithmetic_grade_comment=''
    e_language_marks=None
    e_language_grade=''
    e_language_grade_comment=''
    kiswahili_marks=None
    kiswahili_grade=''
    kiswahili_grade_comment=''
    pre_science_marks=None
    pre_science_grade=''
    pre_science_grade_comment=''
    writing_marks=None
    writing_grade=''
    writing_grade_comment=''
    total=0
    number_of_subjects=0
    average=None
    grade=None
    if request.method=='POST':
        form=ResultForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            stud_name=form.cleaned_data['stud_name']
            arithmetic_marks=form.cleaned_data['arithmetic']
            if arithmetic_marks is not None:
                if arithmetic_marks >= 0 and arithmetic_marks <= 29 :
                    number_of_subjects +=1
                    arithmetic_grade='F'
                    arithmetic_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif arithmetic_marks >= 30 and arithmetic_marks <= 44 :
                    number_of_subjects +=1
                    arithmetic_grade='D'
                    arithmetic_grade_comment='Sio mazuri sana'
                elif arithmetic_marks >= 45 and arithmetic_marks <= 64 :
                    number_of_subjects +=1
                    arithmetic_grade='C'
                    arithmetic_grade_comment='Amejitahidi kufanya vizuri'
                elif arithmetic_marks >= 65 and arithmetic_marks <= 74 :
                    number_of_subjects +=1
                    arithmetic_grade='B'
                    arithmetic_grade_comment='Hongera, amefanya vizuri'
                elif arithmetic_marks >= 75 and arithmetic_marks <= 100 :
                    number_of_subjects +=1
                    arithmetic_grade='A'
                    arithmetic_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    arithmetic_grade='No grade'
                    arithmetic_grade_comment=''
            else:
                number_of_subjects +=0
                arithmetic_grade=''
                arithmetic_marks=0
                arithmetic_grade_comment=''
            e_language_marks=form.cleaned_data['e_language']
            if e_language_marks is not None:
                if e_language_marks >= 0 and e_language_marks <= 29 :
                    number_of_subjects +=1
                    e_language_grade='F'
                    e_language_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif e_language_marks >= 30 and e_language_marks <= 44 :
                    number_of_subjects +=1
                    e_language_grade='D'
                    e_language_grade_comment='Sio mazuri sana'
                elif e_language_marks >= 45 and e_language_marks <= 64 :
                    number_of_subjects +=1
                    e_language_grade='C'
                    e_language_grade_comment='Amejitahidi kufanya vizuri'
                elif e_language_marks >= 65 and e_language_marks <= 74 :
                    number_of_subjects +=1
                    e_language_grade='B'
                    e_language_grade_comment='Hongera, amefanya vizuri'
                elif e_language_marks >= 75 and e_language_marks <= 100 :
                    number_of_subjects +=1
                    e_language_grade='A'
                    e_language_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    e_language_grade='No grade'
                    e_language_grade_comment=''
            else:
                number_of_subjects +=0
                e_language_grade=''
                e_language_marks=0
                e_language_grade_comment=''
            kiswahili_marks=form.cleaned_data['kiswahili']
            if kiswahili_marks is not None:
                if kiswahili_marks >= 0 and kiswahili_marks <= 29 :
                    number_of_subjects +=1
                    kiswahili_grade='F'
                    kiswahili_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif kiswahili_marks >= 30 and kiswahili_marks <= 44 :
                    number_of_subjects +=1
                    kiswahili_grade='D'
                    kiswahili_grade_comment='Sio mazuri sana'
                elif kiswahili_marks >= 45 and kiswahili_marks <= 64 :
                    number_of_subjects +=1
                    kiswahili_grade='C'
                    kiswahili_grade_comment='Amejitahidi kufanya vizuri'
                elif kiswahili_marks >= 65 and kiswahili_marks <= 74 :
                    number_of_subjects +=1
                    kiswahili_grade='B'
                    kiswahili_grade_comment='Hongera, amefanya vizuri'
                elif kiswahili_marks >= 75 and kiswahili_marks <= 100 :
                    number_of_subjects +=1
                    kiswahili_grade='A'
                    kiswahili_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    kiswahili_grade='No grade'
                    kiswahili_grade_comment=''
            else:
                number_of_subjects +=0
                kiswahili_grade=''
                kiswahili_marks=0
                kiswahili_grade_comment=''
            pre_science_marks=form.cleaned_data['pre_science']
            if pre_science_marks is not None:
                if pre_science_marks >= 0 and pre_science_marks <= 29 :
                    number_of_subjects +=1
                    pre_science_grade='F'
                    pre_science_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif pre_science_marks >= 30 and pre_science_marks <= 44 :
                    number_of_subjects +=1
                    pre_science_grade='D'
                    pre_science_grade_comment='Sio mazuri sana'
                elif pre_science_marks >= 45 and pre_science_marks <= 64 :
                    number_of_subjects +=1
                    pre_science_grade='C'
                    pre_science_grade_comment='Amejitahidi kufanya vizuri'
                elif pre_science_marks >= 65 and pre_science_marks <= 74 :
                    number_of_subjects +=1
                    pre_science_grade='B'
                    pre_science_grade_comment='Hongera, amefanya vizuri'
                elif pre_science_marks >= 75 and pre_science_marks <= 100 :
                    number_of_subjects +=1
                    pre_science_grade='A'
                    pre_science_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    pre_science_grade='No grade'
                    pre_science_grade_comment=''
            else:
                number_of_subjects +=0
                pre_science_grade=''
                pre_science_marks=0
                pre_science_grade_comment=''
            writing_marks=form.cleaned_data['writing']
            if writing_marks is not None:
                if writing_marks >= 0 and writing_marks <= 29 :
                    number_of_subjects +=1
                    writing_grade='F'
                    writing_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif writing_marks >= 30 and writing_marks <= 44 :
                    number_of_subjects +=1
                    writing_grade='D'
                    writing_grade_comment='Sio mazuri sana'
                elif writing_marks >= 45 and writing_marks <= 64 :
                    number_of_subjects +=1
                    writing_grade='C'
                    writing_grade_comment='Amejitahidi kufanya vizuri'
                elif writing_marks >= 65 and writing_marks <= 74 :
                    number_of_subjects +=1
                    writing_grade='B'
                    writing_grade_comment='Hongera, amefanya vizuri'
                elif writing_marks >= 75 and writing_marks <= 100 :
                    number_of_subjects +=1
                    writing_grade='A'
                    writing_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    writing_grade='No grade'
                    writing_grade_comment=''
            else:
                number_of_subjects +=0
                writing_grade=''
                writing_marks=0
                writing_grade_comment=''
            total=arithmetic_marks+e_language_marks+kiswahili_marks+pre_science_marks+writing_marks
            resul=form.save(commit=False)
            resul.total=total
            average=round(total/number_of_subjects,2)
            resul.average=average
            if average >= 0 and average <= 29:
                grade='F'
            elif average >= 30 and average <= 44:
                grade='D'
            elif average >= 45 and average <= 64:
                grade='C'
            elif average >= 65 and average <= 74:
                grade='B'
            elif average >= 75 and average <= 100:
                grade='A'
            resul.grade=grade
            resul.arithmetic_grade=arithmetic_grade
            resul.e_language_grade=e_language_grade
            resul.kiswahili_grade=kiswahili_grade
            resul.pre_science_grade=pre_science_grade
            resul.writing_grade=writing_grade
            resul.arithmetic_grade_comment=arithmetic_grade_comment
            resul.e_language_grade_comment=e_language_grade_comment
            resul.kiswahili_grade_comment=kiswahili_grade_comment
            resul.pre_science_grade_comment=pre_science_grade_comment
            resul.writing_grade_comment=writing_grade_comment
            
            resul.save()
            messages.info(request,'result saved successfully')
            return redirect('admin_result')
        
    return render(request,'result.html',{'form':form})

def editresult(request,pk):
    res=Result.objects.get(id=pk)
    form=EditResultForm(instance=res)
    email=None
    comment=''
    stud_name=None
    arithmetic_marks=None
    arithmetic_grade=''
    arithmetic_grade_comment=''
    e_language_marks=None
    e_language_grade=''
    e_language_grade_comment=''
    kiswahili_marks=None
    kiswahili_grade=''
    kiswahili_grade_comment=''
    pre_science_marks=None
    pre_science_grade=''
    pre_science_grade_comment=''
    writing_marks=None
    writing_grade=''
    writing_grade_comment=''
    total=0
    number_of_subjects=0
    average=None
    grade=''
    if request.method=='POST':
        form=EditResultForm(request.POST,instance=res)
        if form.is_valid():
            email=form.cleaned_data['email']
            stud_name=form.cleaned_data['stud_name']
            arithmetic_marks=form.cleaned_data['arithmetic']
            if arithmetic_marks is not None:
                if arithmetic_marks >= 0 and arithmetic_marks <= 29 :
                    number_of_subjects +=1
                    arithmetic_grade='F'
                    arithmetic_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif arithmetic_marks >= 30 and arithmetic_marks <= 44 :
                    number_of_subjects +=1
                    arithmetic_grade='D'
                    arithmetic_grade_comment='Sio mazuri sana'
                elif arithmetic_marks >= 45 and arithmetic_marks <= 64 :
                    number_of_subjects +=1
                    arithmetic_grade='C'
                    arithmetic_grade_comment='Amejitahidi kufanya vizuri'
                elif arithmetic_marks >= 65 and arithmetic_marks <= 74 :
                    number_of_subjects +=1
                    arithmetic_grade='B'
                    arithmetic_grade_comment='Hongera, amefanya vizuri'
                elif arithmetic_marks >= 75 and arithmetic_marks <= 100 :
                    number_of_subjects +=1
                    arithmetic_grade='A'
                    arithmetic_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    arithmetic_grade='No grade'
                    arithmetic_grade_comment=''
            else:
                number_of_subjects +=0
                arithmetic_grade=''
                arithmetic_marks=0
                arithmetic_grade_comment=''
            e_language_marks=form.cleaned_data['e_language']
            if e_language_marks is not None:
                if e_language_marks >= 0 and e_language_marks <= 29 :
                    number_of_subjects +=1
                    e_language_grade='F'
                    e_language_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif e_language_marks >= 30 and e_language_marks <= 44 :
                    number_of_subjects +=1
                    e_language_grade='D'
                    e_language_grade_comment='Sio mazuri sana'
                elif e_language_marks >= 45 and e_language_marks <= 64 :
                    number_of_subjects +=1
                    e_language_grade='C'
                    e_language_grade_comment='Amejitahidi kufanya vizuri'
                elif e_language_marks >= 65 and e_language_marks <= 74 :
                    number_of_subjects +=1
                    e_language_grade='B'
                    e_language_grade_comment='Hongera, amefanya vizuri'
                elif e_language_marks >= 75 and e_language_marks <= 100 :
                    number_of_subjects +=1
                    e_language_grade='A'
                    e_language_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    e_language_grade='No grade'
                    e_language_grade_comment=''
            else:
                number_of_subjects +=0
                e_language_grade=''
                e_language_marks=0
                e_language_grade_comment=''
            kiswahili_marks=form.cleaned_data['kiswahili']
            if kiswahili_marks is not None:
                if kiswahili_marks >= 0 and kiswahili_marks <= 29 :
                    number_of_subjects +=1
                    kiswahili_grade='F'
                    kiswahili_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif kiswahili_marks >= 30 and kiswahili_marks <= 44 :
                    number_of_subjects +=1
                    kiswahili_grade='D'
                    kiswahili_grade_comment='Sio mazuri sana'
                elif kiswahili_marks >= 45 and kiswahili_marks <= 64 :
                    number_of_subjects +=1
                    kiswahili_grade='C'
                    kiswahili_grade_comment='Amejitahidi kufanya vizuri'
                elif kiswahili_marks >= 65 and kiswahili_marks <= 74 :
                    number_of_subjects +=1
                    kiswahili_grade='B'
                    kiswahili_grade_comment='Hongera, amefanya vizuri'
                elif kiswahili_marks >= 75 and kiswahili_marks <= 100 :
                    number_of_subjects +=1
                    kiswahili_grade='A'
                    kiswahili_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    kiswahili_grade='No grade'
                    kiswahili_grade_comment=''
            else:
                number_of_subjects +=0
                kiswahili_grade=''
                kiswahili_marks=0
                kiswahili_grade_comment=''
            pre_science_marks=form.cleaned_data['pre_science']
            if pre_science_marks is not None:
                if pre_science_marks >= 0 and pre_science_marks <= 29 :
                    number_of_subjects +=1
                    pre_science_grade='F'
                    pre_science_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif pre_science_marks >= 30 and pre_science_marks <= 44 :
                    number_of_subjects +=1
                    pre_science_grade='D'
                    pre_science_grade_comment='Sio mazuri sana'
                elif pre_science_marks >= 45 and pre_science_marks <= 64 :
                    number_of_subjects +=1
                    pre_science_grade='C'
                    pre_science_grade_comment='Amejitahidi kufanya vizuri'
                elif pre_science_marks >= 65 and pre_science_marks <= 74 :
                    number_of_subjects +=1
                    pre_science_grade='B'
                    pre_science_grade_comment='Hongera, amefanya vizuri'
                elif pre_science_marks >= 75 and pre_science_marks <= 100 :
                    number_of_subjects +=1
                    pre_science_grade='A'
                    pre_science_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    pre_science_grade='No grade'
                    pre_science_grade_comment=''
            else:
                number_of_subjects +=0
                pre_science_grade=''
                pre_science_marks=0
                pre_science_grade_comment=''
            writing_marks=form.cleaned_data['writing']
            if writing_marks is not None:
                if writing_marks >= 0 and writing_marks <= 29 :
                    number_of_subjects +=1
                    writing_grade='F'
                    writing_grade_comment='Amefeli ajitahidi mtihani ujao'
                elif writing_marks >= 30 and writing_marks <= 44 :
                    number_of_subjects +=1
                    writing_grade='D'
                    writing_grade_comment='Sio mazuri sana'
                elif writing_marks >= 45 and writing_marks <= 64 :
                    number_of_subjects +=1
                    writing_grade='C'
                    writing_grade_comment='Amejitahidi kufanya vizuri'
                elif writing_marks >= 65 and writing_marks <= 74 :
                    number_of_subjects +=1
                    writing_grade='B'
                    writing_grade_comment='Hongera, amefanya vizuri'
                elif writing_marks >= 75 and writing_marks <= 100 :
                    number_of_subjects +=1
                    writing_grade='A'
                    writing_grade_comment='Hongera,amefanya vizuri zaidi'
                else:
                    number_of_subjects +=1
                    writing_grade='No grade'
                    writing_grade_comment=''
            else:
                number_of_subjects +=0
                writing_grade=''
                writing_marks=0
                writing_grade_comment=''
            
            total=arithmetic_marks+e_language_marks+kiswahili_marks+pre_science_marks+writing_marks
            resul=form.save(commit=False)
            resul.total=total
            average=round(total/number_of_subjects,2)
            resul.average=average
            if average >= 0 and average <= 29:
                grade='F'
            elif average >= 30 and average <= 44:
                grade='D'
            elif average >= 45 and average <= 64:
                grade='C'
            elif average >= 65 and average <= 74:
                grade='B'
            elif average >= 75 and average <= 100:
                grade='A'
            resul.grade=grade
            resul.arithmetic_grade=arithmetic_grade
            resul.e_language_grade=e_language_grade
            resul.kiswahili_grade=kiswahili_grade
            resul.pre_science_grade=pre_science_grade
            resul.writing_grade=writing_grade
            resul.arithmetic_grade_comment=arithmetic_grade_comment
            resul.e_language_grade_comment=e_language_grade_comment
            resul.kiswahili_grade_comment=kiswahili_grade_comment
            resul.pre_science_grade_comment=pre_science_grade_comment
            resul.writing_grade_comment=writing_grade_comment
            resul.save()
            return redirect('admin_result')
    return render(request,'edit_result.html',{'form':form})


def delete_result(request,pk):
    result=Result.objects.get(id=pk)
    if request.method=='POST':   
       result.delete()
       return redirect('admin_result')
    return render(request,'delete_result.html',{'result':result})

def add_fee(request):
    form=AddFeeForm()
    debt=None
    if request.method=='POST':
        form=AddFeeForm(data=request.POST)
        if form.is_valid():
            required_amount=form.cleaned_data['required_amount']
            amount_paid=form.cleaned_data['amount_paid']
            if amount_paid < required_amount:
                debt=required_amount-amount_paid
            else:
                debt=0
            obj=form.save(commit=False)
            obj.debt=debt
            obj.save()
            return redirect('fee_list')
    return render(request,'add_fee.html',{'form':form})

def fee_list(request):
    fees=Fee.objects.all()
    if request.method=='GET':
       search=request.GET.get('search','')
       fei=Fee.objects.filter(Q(stud_name__full_name__icontains=search) | Q(month_paid__icontains=search))
    return render(request,'fee_list.html',{'fees':fees,'fei':fei,'search':search})

def edit_fee(request,pk):
    fee=Fee.objects.get(id=pk)
    amount_paid=fee.amount_paid
    required_amount=fee.required_amount
    debt=fee.debt
    if debt:
        required_amount=debt
        amount_paid=None
        fee.amount_paid=amount_paid
        fee.required_amount=required_amount
    form=EditFeeForm(instance=fee)
    if request.method=='POST':
        form=EditFeeForm(request.POST,instance=fee)
        if form.is_valid():
                
                required_amount=form.cleaned_data['required_amount']
                amount_paid=form.cleaned_data['amount_paid']
                if amount_paid < required_amount:
                    debt=required_amount-amount_paid
                else:
                    debt=0
                obj=form.save(commit=False)
                obj.debt=debt
                obj.save()
                return redirect('fee_list')
    return render(request,'edit_fee.html',{'form':form})
class FeeDetail(DetailView):
    model=Fee
    context_object_name='fee'
    template_name='fee_detail.html'
class Student_list(ListView):
    model=Student
    context_object_name='students'
    template_name='student_list.html'
class Student_detail(DetailView):
    model=Student
    context_object_name='student'
    template_name='student_detail.html'

def res_detail(request,pk):
    # user1=User.objects.get(id=pk)
    # results=Result.objects.all().values_list('average').order_by('-average')
    # res=Result.objects.get(id=pk)
    # pos=results.index(res)
    detail=Result.objects.get(id=pk)
    return render(request,'res_detail.html',{'result':detail})

def download_pdf(request,pk):
    detail=Result.objects.get(id=pk)
    template=loader.get_template('res_detail.html')
    html=template.render({'result':detail})
    pdf=pdfkit.from_string(html,False,options={'page-size':'Letter','encoding':'UTF-8'})
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename='result.pdf'
    return response

def signup(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    return render(request,'signup.html',{'form':form})

def edit_parent(request,pk):
    parent=User.objects.get(id=pk)
    form=EditParentForm(instance=parent)
    if request.method=='POST':
        form=EditParentForm(request.POST,instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    return render(request,'edit_parent.html',{'form':form})
def delete_parent(request,pk):
    parent=User.objects.get(id=pk)
    if request.method=='POST':   
       parent.delete()
       return redirect('parent_list')
    return render(request,'delete_parent.html',{})



def parent_detail(request,pk):
    detail=User.objects.get(id=pk)
    return render(request,'parent_detail.html',{'parent':detail})

def parent_list(request):
    users=User.objects.all()
    if request.method=='GET':
       search=request.GET.get('search','')
       res=User.objects.filter(full_name__icontains=search)
    
    return render(request,'parent_list.html',{'users':users,'res':res,'search':search})

def admin_result(request):
    if request.method=='GET':
       search=request.GET.get('search','')
       res=Result.objects.filter(stud_name__full_name__icontains=search)
    results=Result.objects.all().order_by('-average')
    return render(request,'admin_result.html',{'results':results,'res':res,'search':search})

def dashboard(request):
    users=User.objects.all()
    levels=LevelClass.objects.all()
    num_results=Result.objects.all().count()
    students=Student.objects.all()
    return render(request,'dashboard.html',{'num_results':num_results,'levels':levels,'students':students,'users':users})

def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username','')
            password=form.cleaned_data.get('password','')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,'You are logged in website')
                return redirect('home')
        else:
            messages.info(request,'Login failed')

    return render(request,'login.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')