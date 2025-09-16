from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(">>> AuthMiddleware running on:", request.path)

        path = request.path

        # Allow homepage + login
        if path in ['/', '/t1']:
            return self.get_response(request)

        # Block /t2 if not logged in
        if path.startswith('/t2') and not request.session.get('employee_id'):
            return redirect('S1')

        # Block /t3 if not logged in or no account selected
        if path.startswith('/t3'):
            if not request.session.get('employee_id'):
                return redirect('S1')
            if not request.session.get('account_id'):
                return redirect('S2')

        return self.get_response(request)
