from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'
    
    
##############
##CRUD VIEWS##
##############

class PostListView(ListView):
    model = Post
    
    ##how to get data in generic views
    def get_queryset(self):
        
        ## __ is for field conditions lte means less than equal to ...the current time and order it by  latest published date
        ##get queryset method
        ##
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    
class PostDetailView(DetailView):
    model = Post
    

##use decorator to limit who can alter this
##use mixin instead
##

class CreatePostView(LoginRequiredMixin, CreateView):
    ##for mixin
    ##
    ##redirect to login or detail view
    ##
    login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    
    ##import form created to create post
    ##
    form_class = PostForm
    
    ##for createpost
    model = Post
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
 
 
class PostDeleteView(LoginRequiredMixin, DeleteView):
     model = Post
     ##where to go after deleting
     ##
     success_url = reverse_lazy('post_list')


## draft list
##
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name='blog/draft_list.html'
    model = Post
    
    def get_queryset(self):
        ##is null = True means no publication date
        ##
       return Post.objects.filter(published_date__isnull=True).order_by('create_date')
    
    
    
#function views
###################################################################
###################################################################

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    
    ##if someone filled out form
    ##
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        ##if they didn't mess it up
        ##
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        
    ##if didn't comment
    ##
    else:
        form = CommentForm()
        
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk 
    comment.delete()
    return redirect('post_detail', pk = post_pk)
    
    
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)