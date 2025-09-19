from django.shortcuts import render,redirect
from django.contrib import messages
from application1.models import Employee
from .models import Account
from django.db.models import Q

def account_logout(request):
    print(">>> account_logout called")
    request.session.pop('account_id', None)   # remove only account_id
    return redirect('S2')   # go back to account selection page

def employee_logout(request):
    print(">>> employee_logout called")
    request.session.flush()   # clear entire session
    return redirect('S1')



    
def Test_Case1(request):
    if request.method == "POST":
        user_id = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            employee = Employee.objects.get(user_id=user_id, password=password)

         
            request.session['employee_id'] = employee.id  

            return redirect('S2')

        except Employee.DoesNotExist:
            messages.error(request, "Invalid User ID or Password")
            return render(request, 'application/S1.html')

    return render(request, 'application/S1.html')


def Test_Case2(request):
    if request.method == "POST":
        acc_num = request.POST.get('account_number')
        aadhar_num = request.POST.get('aadhar_number')

        account = None

      
        if acc_num:
            try:
                account = Account.objects.get(account_number=acc_num)
            except Account.DoesNotExist:
                return render(request, 'application/S2.html', {
                    "error_message": "Please enter valid Account Number."
                })


        elif aadhar_num:
            try:
                account = Account.objects.get(aadhar_number=aadhar_num)
            except Account.DoesNotExist:
                return render(request, 'application/S2.html', {
                    "error_message": "Please enter valid Aadhar Number."
                })

        else:
            return render(request, 'application/S2.html', {
                "error_message": "Please enter Account Number or Aadhar Number."
            })

        request.session['account_id'] = account.id
        return redirect('S3')

    return render(request, 'application/S2.html')



def Test_Case3(request):
    account_id = request.session.get('account_id')
    if not account_id:
        return redirect('S2')

    account = Account.objects.get(id=account_id)
    return render(request, 'application/S3.html', {'account': account})
