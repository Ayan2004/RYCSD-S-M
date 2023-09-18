from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.utils.dateparse import parse_date
from openpyxl import Workbook
from django.templatetags.static import static
from django.contrib import messages

from decimal import Decimal

from .models import *
from .forms import *

# Create your views here.

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    
    return render(request,'login.html')


@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required
def home(request):

    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request,'index.html',context)


@login_required
def add_student(request):
    form = add_student_form()
    context = {
        'form': form,
        'heading':"Add Students"
    }

    if(request.method == 'POST'):
        form = add_student_form(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.Total_Fees = form.Course.Course_Fees
            form.save()
        return redirect('student_list')

    return render(request,'student/add_form.html',context)

@login_required
def update_student(request,id):
    student = Student.objects.get(id=id)
    form = add_student_form(instance=student)
    context = {'form': form,
               'heading':"Update Student"}
    
    if(request.method == 'POST'):
        form = add_student_form(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
        return redirect('student_view',id=id)
    return render(request,'student/add_form.html',context)

@login_required
def delete_student(request,id):
    student = Student.objects.get(id=id)
    context ={'student':student}

    if(request.method == 'POST'):
        student.delete()
        return redirect('home')
    return render(request,'student/delete.html',context)

@login_required
def student_list(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        students = Student.objects.filter(Date_Of_Admission__range=[min, max])
    else:
        students = Student.objects.all()

    context ={'students':students}
    return render(request,'student/student_list.html',context)

@login_required
def student_view(request, id):

    student = Student.objects.get(id=id)
    fees = Fees_Show.objects.all().filter(Student__id=id)
    context ={
        'student':student,
        'fees':fees
    }
    return render(request,'student/student_view.html',context)


@login_required
def student_reports(request):
    global students

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        students = Student.objects.filter(Date_Of_Admission__range=[min, max])
    else:
        students = Student.objects.all()

    context ={'students':students}
    return render(request,'student/student_reports.html',context)

@login_required
def student_reports_excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Student_Repots.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Student Reports"

    # Add headers
    headers = ["Enrollment_No", "Name", "Course", "DOB", "Father_Name", "Mother_Name", "Gender", "Caste", "Contact_No", "Email", "District", "Address", "Highest_Qualification", "Name_Of_School", "Name_Of_Board", "Year_Of_Pass", "Marks_Obtained", "Date_Of_Admission"]
    ws.append(headers)

    # Add data from the model

    for student in students:
        ws.append([student.Enrollment_No, student.Name, student.Course.Name, student.DOB, student.Father_Name, student.Mother_Name, student.Gender, student.Caste, student.Contact_No, student.Email, student.District, student.Address, student.Highest_Qualification, student.Name_Of_School, student.Name_Of_Board, student.Year_Of_Pass, student.Marks_Obtained, student.Date_Of_Admission])

    # Save the workbook to the HttpResponse
    wb.save(response)
    return response 


@login_required
def student_list_with_fees(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        students = Student.objects.filter(Date_Of_Admission__range=[min, max])
    else:
        students = Student.objects.all()

    context ={'students':students}
    return render(request,'student/student_list_with_fees.html',context)


@login_required
def student_view_with_fees(request,id):

    student = Student.objects.get(id=id)
    fees = Fees_Show.objects.all().filter(Student__id=id)
    context ={
        'student':student,
        'fees':fees
    }
    return render(request,'student/student_view_with_fees.html',context)

@login_required
def add_show_fee(request,id):
    student = Student.objects.get(id=id)
    # fees = Fees.objects.all().filter(Student__id=id)
    form = add_show_fees_form(initial={'Student': student})
    context ={'form': form}

    if(request.method == 'POST'):
        form = add_show_fees_form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('student_view_with_fees',id=id)
    return render(request,'student/pay_installment.html',context)

@login_required
def delete_show_fee(request,sid,id):
    fee = Fees_Show.objects.get(id=id)
    context ={'fee':fee}

    if(request.method == 'POST'):
        fee.delete()
        # return redirect('home')
        return redirect('student_view_with_fees',id=sid)
    return render(request,'student/delete.html',context)

@login_required
def student_list_with_installment(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        students = Student.objects.filter(Date_Of_Admission__range=[min, max])
    else:
        students = Student.objects.all()

    context ={'students':students}
    return render(request,'student/student_list_with_installment.html',context)

@login_required
def student_view_with_installment(request,id):

    student = Student.objects.get(id=id)
    fees = Fees_Payment.objects.all().filter(Student__id=id)
    fees_show = Fees_Show.objects.all().filter(Student__id=id)
    context ={
        'student':student,
        'fees':fees,
        'fees_show':fees_show
    }
    return render(request,'student/student_view_with_installment.html',context)

@login_required
def pay_installment(request,id):
    student = Student.objects.get(id=id)
    form = pay_installment_form(initial={'Student': student})
    context ={'form': form}

    if(request.method == 'POST'):
        form = pay_installment_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = student
            form.Due = student.Total_Fees - form.Emi
            student.Total_Fees = form.Due
            student.save()
            form.save()
            
            return redirect('student_view_with_installment',id=id)
    return render(request,'student/pay_installment.html',context)

@login_required
def edit_installment_fee(request,sid,id):

    fee = Fees_Payment.objects.get(id=id)
    student = Student.objects.get(id=sid)
    student.Total_Fees += fee.Emi
    form = pay_installment_form(instance=fee)
    context = {'form': form,
               'Heading':"Fee Edit"}
    
    if(request.method == 'POST'):
        form = pay_installment_form(request.POST,instance=fee)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = student
            form.Due = student.Total_Fees - form.Emi
            student.Total_Fees = form.Due
            student.save()
            form.save()
        return redirect('student_view_with_installment',id=sid)
    return render(request,'student/pay_installment.html',context)


@login_required   
def delete_installment_fee(request,sid,id):

    fee = Fees_Payment.objects.get(id=id)
    context ={'fee':fee}

    if(request.method == 'POST'):
        student = Student.objects.get(id=sid)
        student.Total_Fees += fee.Emi
        student.save()
        fee.delete()
        return redirect('student_view_with_installment',id=sid)
    return render(request,'student/delete.html',context)

@login_required
def Fees_Reports(request):
    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        students = Student.objects.filter(created__range=[min, max])
    else:
        students = Student.objects.all()

    fees = Fees_Payment.objects.all()
        

    context ={'students':students,
              'fees':fees}
    return render(request,'student/student_fees_reports.html',context)

@login_required
def Fees_Payment_Reports(request):
    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        fees = Fees_Show.objects.filter(Emi_Payment_Date__range=[min, max])
    else:
        fees = ''

    feesPay = Fees_Payment.objects.all()

    flag = ''
        

    context ={'fees':fees,
              'feesPay':feesPay,
              'flag':flag}
    return render(request,'student/student_fees_payment_reports.html',context)



# student end



# courses start
@login_required
def courses(request):

    courses = Courses.objects.all()
    context ={'courses':courses,
              'mode':'view'}
    return render(request,'student/courses.html',context)

@login_required
def courses_view(request,id):

    course = Courses.objects.get(id=id)
    context ={'course':course}
    return render(request,'student/courses_view.html',context)

@login_required
def courses_alter_view(request):
    courses = Courses.objects.all()
    context ={'courses':courses,
              'mode':'alter'}
    return render(request,'student/courses.html',context)

@login_required
def courses_add(request):
    form = add_courses_form()
    context = {'form':form,
               'heading':'Add Courses'}

    if(request.method == 'POST'):
        form = add_courses_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('courses_alter_view')
    return render(request,'student/add_form.html',context)

@login_required
def courses_alter(request,id):
    course = Courses.objects.get(id=id)
    form = add_courses_form(instance=course)
    context = {'form':form,
               'heading':'Alter Courses'}

    if(request.method == 'POST'):
        form = add_courses_form(request.POST , instance=course)
        if form.is_valid():
            form.save()
        return redirect('courses_alter_view')
    return render(request,'student/add_form.html',context)

@login_required
def courses_delete(request,id):
    course = Courses.objects.get(id=id)
    context = {'course':course}

    if(request.method == 'POST'):
        course.delete()
        return redirect('courses_alter_view')
    return render(request,'student/delete.html',context)

@login_required
def course_reports(request):
    courses = Courses.objects.all()
    context ={'courses':courses,
              'mode':'view'}
    return render(request,'student/course_reports.html',context)

# courses end



#enquries start
@login_required
def enquries(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        enquries = Enquries.objects.filter(created__range=[min, max])
    else:
        enquries = Enquries.objects.all()

    context ={'enquries':enquries,
              'mode':'view'}
    
    return render(request,'student/enquries.html',context)    

@login_required
def enquries_view(request,id):

    enquries = Enquries.objects.get(id=id)
    context ={'enquries':enquries,
              'col':2}
    return render(request,'student/enquries_view.html',context)

@login_required
def enquries_alter_view(request):
    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        enquries = Enquries.objects.filter(created__range=[min, max])
    else:
        enquries = Enquries.objects.all()

    context ={'enquries':enquries,
              'mode':'alter'}
    return render(request,'student/enquries.html',context)

@login_required
def enquries_add(request):
    form = add_enquries_form()
    context = {'form':form,
               'heading':'Add Enquries'}

    if(request.method == 'POST'):
        form = add_enquries_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'enqury successfully added')
        else:
            messages.error(request,'error')
        return redirect('enquries_alter_view')
    return render(request,'student/add_form.html',context)

@login_required
def enquries_delete(request,id):
    enquries = Enquries.objects.get(id=id)
    context = {'enquries':enquries}

    if(request.method == 'POST'):
        enquries.delete()
        return redirect('enquries_alter_view')
    return render(request,'student/delete.html',context)

@login_required
def enquries_reports(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')

    if (min and max != ''):
        enquries = Enquries.objects.filter(created__range=[min, max])
    else:
        enquries = Enquries.objects.all()

    context ={'enquries':enquries}
    return render(request,'student/enquries_reports.html',context)


# enquries end


# Accounts
@login_required
def Make_Transaction(request):

    form = Transaction_form()
    balance = Account.objects.get(a_id=1)
    transactions = Transaction.objects.all().order_by('-created')

    context = {'transactions':transactions,
               'form':form,
               'balance':balance,
               'type':'Add',
               'heading':'Make Transaction'}

    if(request.method == 'POST'):
        Cr = request.POST.get('Cr')
        Dr = request.POST.get('Dr')

        form = Transaction_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if Cr != '':
                form.Amount += Decimal(Cr)

            if Dr != '':
                form.Amount -= Decimal(Dr)

            balance.Balance += form.Amount
            balance.save()
            form.save()
            return HttpResponseRedirect("make_transactions")
    return render(request,'Transaction/add.html',context)


@login_required
def View_Transaction(request):
    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')
    t_type = request.POST.get('c/b')
    balance = 0
    flag=''

    if ((min and max != '') and t_type == 'All'):
        transactions = Transaction.objects.filter(Date__range=[min, max])
        for t in transactions:
            balance += t.Amount

    elif((min and max != '') and t_type == 'Cash'):
        transactions = Transaction.objects.filter(Date__range=[min, max] , P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif((min and max != '') and t_type == 'Bank'):
        transactions = Transaction.objects.filter(Date__range=[min, max] , P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif(t_type == 'Cash'):
        transactions = Transaction.objects.filter(P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif(t_type == 'Bank'):
        transactions = Transaction.objects.filter(P_method=t_type)
        for t in transactions:
            balance += t.Amount

    else:
        transactions = Transaction.objects.all()
        balance = Account.objects.get(a_id=1)

    context ={'transactions':transactions,
              'balance':balance,
              'flag':flag}
    return render(request,'Transaction/alter_list.html',context)


@login_required
def Edit_Transaction(request,id):
    balance = Account.objects.get(a_id=1)
    transaction = Transaction.objects.get(id=id)
    balance.Balance -= transaction.Amount
    form = Transaction_form(instance=transaction)

    context = {'transaction':transaction,
               'form':form,
               'balance':balance,
               'type':'Update',
               'heading':'Update Transaction'}

    if(request.method == 'POST'):
        Cr = request.POST.get('Cr')
        Dr = request.POST.get('Dr')

        form = Transaction_form(request.POST,instance=transaction)
        if form.is_valid():
            form = form.save(commit=False)
            form.Amount = 0
            if Cr != '':
                form.Amount += Decimal(Cr)

            if Dr != '':
                form.Amount -= Decimal(Dr)

            balance.Balance += form.Amount
            balance.save()
            form.save()
            return redirect('View_Transaction')
    return render(request,'Transaction/add.html',context)


@login_required
def Delete_Transaction(request,id):
    balance = Account.objects.get(a_id=1)
    transaction = Transaction.objects.get(id=id)
    context = {'transaction':transaction}

    if(request.method == 'POST'):
        if transaction.Amount > 0:
            balance.Balance -= transaction.Amount
        if transaction.Amount < 0:
            balance.Balance += abs(transaction.Amount)
        balance.save()
        
        transaction.delete()
        return redirect('View_Transaction')

    return render(request,'student/delete.html',context)


@login_required
def Transaction_Reports(request):

    min = parse_date(request.POST.get('min') if request.POST.get('min')!=None else '')
    max = parse_date(request.POST.get('max') if request.POST.get('max')!=None else '')
    t_type = request.POST.get('c/b')
    balance = 0
    flag=''

    if ((min and max != '') and t_type == 'All'):
        transactions = Transaction.objects.filter(Date__range=[min, max])
        for t in transactions:
            balance += t.Amount

    elif((min and max != '') and t_type == 'Cash'):
        transactions = Transaction.objects.filter(Date__range=[min, max] , P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif((min and max != '') and t_type == 'Bank'):
        transactions = Transaction.objects.filter(Date__range=[min, max] , P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif(t_type == 'Cash'):
        transactions = Transaction.objects.filter(P_method=t_type)
        for t in transactions:
            balance += t.Amount

    elif(t_type == 'Bank'):
        transactions = Transaction.objects.filter(P_method=t_type)
        for t in transactions:
            balance += t.Amount

    else:
        transactions = Transaction.objects.all()
        balance = Account.objects.get(a_id=1)

    context ={'transactions':transactions,
              'balance':balance,
              'flag':flag}
    return render(request,'Transaction/transaction_reports.html',context)