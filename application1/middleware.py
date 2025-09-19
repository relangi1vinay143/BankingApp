from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(">>> AuthMiddleware running on:", request.path)

        # Protect only after login pages
        protected_paths = ["/t2/", "/t3/"]

        if request.path in protected_paths and not request.session.get("employee_id"):
            return redirect("S1")  # login page

        response = self.get_response(request)
        return response
