from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to USERS</h1></center>')