from datetime import datetime
from django.shortcuts import redirect
class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # FIrst method
        # print("Request Started")
        # response = self.get_response(request)
        # print("Request Ended")
        # return response

        # Second method
        print("-"*50)
        print("Request Received")
        print("Time :", datetime.now())
        print("URL :", request.path)
        print("Method :", request.method)
        print("User :", request.user)
        protected_urls = [
            "/employees/",
            "/employees/create/",
            "/employees/update/",
            "/employees/delete/",
            "/delete/<int:pk>/"
       ]
        if ( request.path in protected_urls and not request.user.is_authenticated
        ):
            print("Unauthorized User")
            return redirect("login")
        response = self.get_response(request)
        print("Status Code :", response.status_code)
        print("Response Sent")
        print("-" * 60)
        return response
