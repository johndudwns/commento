from django.shortcuts import render
#commit 원격 확인용4

# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')