from django.shortcuts import render,redirect
from django.contrib import messages
from application1.models import Employee
from .models import Account
from django.db.models import Q

def logout_view(request):
    # Clear all session data
    request.session.flush()  

    # Optional: Show a logout success message
    from django.contrib import messages
    messages.success(request, "You have been logged out successfully.")

    # Redirect back to login page
    return redirect('S1')
    
def Test_Case1(request):
    if request.method == "POST":
        user_id = request.POST.get('username')
        password = request.POST.get('password')

        try:
            employee = Employee.objects.get(user_id=user_id, password=password)

            # ✅ Store employee_id in session
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

        try:
            if acc_num:
                account = Account.objects.get(account_number=acc_num)
            elif aadhar_num:
                account = Account.objects.get(aadhar_number=aadhar_num)
            else:
                messages.error(request, "Please enter Account Number or Aadhar Number")
                return render(request, 'application/S2.html')

            # ✅ Store account_id in session
            request.session['account_id'] = account.id  

            return redirect('S3')

        except Account.DoesNotExist:
            return render(request, 'application/S2.html',{'error': 'Please enter valid details'})

    return render(request, 'application/S2.html')



def Test_Case3(request):
    account_id = request.session.get('account_id')
    if not account_id:
        return redirect('S2')

    account = Account.objects.get(id=account_id)
    return render(request, 'application/S3.html', {'account': account})
