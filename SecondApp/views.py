from django.shortcuts import render

def showpage(request):
    return render(request,'index.html')
def handleform(request):
    name=request.post['t1']
    email=request.post['t2']
    data={'name':name,'email':email}
    return render(request,'showpage.html')
