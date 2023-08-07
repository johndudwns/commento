from django.shortcuts import render
# from django.http import HttpResponse

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment, Post
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage


# Create your views here.


def index(request):
    #    return HttpResponse("Hello world")
    page = request.GET.get('page','1')
    content_list = MainContent.objects.order_by('-pub_date')
    paginator = Paginator(content_list,3)
    page_obj = paginator.get_page(page)
    context = {'content_list': page_obj}
    return render(request, 'mysite/content_list.html', context)


def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)


@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()
        context = {'content_list': content_list, 'form': form}
        return render(request, 'mysite/content_detail.html', context)


@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id=comment.content_list.id)

# def post_list(request):
#     content_list = Post.objects.all()
#     page = request.GET.get('page')
#     paginator = Paginator(content_list,3)
#     try:
#         page_obj = paginator.page(page)
#     except PageNotAnInteger:
#         page = 1
#         page_obj = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         page_obj = paginator.page(page)
#     return render(request, 'mysite/content_list.html',{'content_list':content_list, 'page_obj':page_obj,'paginator':paginator})
