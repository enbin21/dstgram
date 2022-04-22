from django.shortcuts import render, redirect
from .models import Photo
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect

# @login_required
# def photo_list(request):
#     photos = Photo.objects.all()
#     return render(request, 'photo/list.html', {'photos': photos})

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'photo/list.html'

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 현재 로그인 한 사용자로 설정
        if form.is_valid():  # 입력된 값 검증
            form.instance.save()  # 이상이 없다면, 데이터베이스에 저장하고,
            return redirect('/')  # 메인 페이지로 이동
        else:
            return self.render_to_response({'form': form})  # 이상이 있다면, 작성된 내용을 그대로 작성 페이지에 표시

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'   # site 메인 의미
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

@login_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'photo/profile.html')

class PhotoMyList(ListView):
    model = Photo
    template_name = 'photo/myphoto.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(PhotoMyList, self).dispatch(request, *args, **kwargs)