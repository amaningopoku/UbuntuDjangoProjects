from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserInfo, ProfilePicture
from .forms import UserInfoForm

# Create your views here.
def index(request):

    user_data = UserInfo.objects.all()
    context = {'user_data':user_data}
    return render(request, 'userinfo/index.html', context)

def user_details(request, user_id):

    user_detail = UserInfo.objects.get(id=user_id)
    prof_pic = ProfilePicture.objects.filter(pic_name=user_detail).first()
    context = {
        'user_detail':user_detail, 'prof_pic':prof_pic
        }

    return render(request, 'userinfo/user_details.html', context)

def add_user(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse('userinfoapp:user_info'))
        else:
            return render(request, 'userinfo/add_user.html')
        
    return render(request, 'userinfo/add_user.html')
