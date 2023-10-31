from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def users_view(request):
    # 뷰 로직을 구현
    return HttpResponse("This is the users view.")
