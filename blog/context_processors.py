from .views import Post

def rooms(request):
    rooms = Post.objects.all()
    return {"rooms": rooms}