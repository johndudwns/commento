from django.shortcuts import render
#commit 확인용

# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')