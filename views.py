from django.shortcuts import render,redirect
from resume.models import CustomUser,Resume



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser(name=name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(email=email, password=password).first()

        if user is not None:
            return redirect('form', user_id=user.id)
        else:
            return redirect('signup')

    return render(request, 'login.html')


def form(request, user_id):
    if request.method == 'POST':
        userimg=request.FILES.get('userimg')
        username=request.POST.get('username')
        usernumber=request.POST.get('usernumber')
        useremail=request.POST.get('useremail')
        useraddress=request.POST.get('useraddress')
        userhobbies=request.POST.get('userhobbies')
        userlang=request.POST.get('userlang')
        userprofile=request.POST.get('userprofile')
        userquali=request.POST.get('userquali')
        userachieve=request.POST.get('userachieve')
        userproject=request.POST.get('userproject')
        user = CustomUser.objects.get(id=user_id)
        resume = Resume(user=user,userimg=userimg,username=username,usernumber=usernumber,useremail=useremail,useraddress=useraddress,userhobbies=userhobbies,userlang=userlang,userprofile=userprofile,userquali=userquali,userachieve=userachieve,userproject=userproject)
        resume.save()
        return redirect('resume', user_id=user_id)
    return render(request, 'form.html')



def resume(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    resumes = Resume.objects.filter(user=user).order_by('-created_at')
    most_recent_resume = resumes.first()
    context = {'user': user, 'resume': most_recent_resume}
    return render(request, 'resume.html', context)






def form1(request):
    return render(request,"form1.html")



def home(request):
    return render(request,"home.html")

