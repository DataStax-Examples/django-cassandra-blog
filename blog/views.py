from django.shortcuts import render, redirect
from blog.models import PostModel


# Create your views here.
def home(request):
    # Note: we are using the 'all()' method provided by the model:
    # this is acceptable as long as we know there are few posts!
    # If there are many posts, fetching all posts at once,
    # sorting them by date in this function and finally rendering them all
    # on the page at once is a bad idea (performance-wise).
    # Proper handling of this involves pagination and/or a careful choice
    # of the partitioning/clustering of the underlying Cassandra table.
    #
    # The structure of the Cassandra posts table does not guarantee
    # any specific ordering when fetching the posts, so we
    # explicitly sort by date the resulting list of posts.
    posts_list = sorted(list(PostModel.objects.all()),
                        key=lambda p: p.created_at)
    return render(request, 'index.html', {'posts': posts_list})


def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        new_post = PostModel.objects.create(title=title, body=body)
        new_post.save
        return redirect('/')
    else:
        return render(request, 'newpost.html')


def posts(request, pk):
    post = PostModel.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})


def about(request):
    return render(request, 'about.html')
