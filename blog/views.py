from django.shortcuts import render, redirect
from blog.models import PostModel

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from decouple import config

cloud_config = {
    'secure_connect_bundle': config("BUNDLE_PATH")
}
auth_provider = PlainTextAuthProvider(config("CLIENT_ID"), config("CLIENT_SECRET"))
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('tech_blog')


# Create your views here.
def home(request):
    posts_list = []
    rows = session.execute('SELECT title, body, created_at, id FROM post_model')
    for row in rows:
        lists = row.title, row.body, row.created_at, row.id
        posts_list.append(lists)
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