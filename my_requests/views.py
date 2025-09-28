from django.shortcuts import render

def open_my_requets(request):
    return render(request, 'my_requests.html')