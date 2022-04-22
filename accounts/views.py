from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST': # 회원가입 데이터 입력 완료 상황
        user_form = RegisterForm(request.POST) # request.POST-사용자가 입력한 값
        if user_form.is_valid(): # 데이터형식이 맞는지 확인, validation 호출
            new_user = user_form.save(commit=False) # 해당 form 모델의 인스턴스를 얻어옴
            new_user.set_password(user_form.cleaned_data['password']) # password 할당
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else: # 회원가입 내용을 입력하는 상황
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})

@login_required
def dropout(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('login')
    return render(request, 'registration/dropout.html')