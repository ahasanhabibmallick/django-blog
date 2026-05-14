from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from .models import Blog,Category, SocialLink, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status ='Published',category=category_id)
    #Use try/except when we want to do some custom action if the category does not exist 
    # try:
    #    category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    #  
    # use get_object_or_404 when you want to show error page if the category does not exist
    category  = get_object_or_404(Category, pk=category_id)  
    context = {
        'posts': posts,
        'category_id' : category,
    }

    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    categories = Category.objects.all()
    social_links = SocialLink.objects.all()
    context ={
        'single_blog': single_blog,
        'categories': categories,              
        'social_links': social_links,
        'comments': comments
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')

    blogs =Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    print(blogs)

    context ={
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request,'search.html',context)