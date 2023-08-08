from django.shortcuts import render

# Create your views here.
def mypage1(request):
    return render(request,'index1.html',{'title':'Rokibs Page1','robin':'Golapi'})

def mypage2(request):
    return render(request,'index2.html',{'title':'Akash Page1','robin':'Golapi'})

def mypage3(request):
    return render(request,'index3.html')