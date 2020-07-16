from django.views import generic
from .models import Post, Faq
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

class FaqList(generic.ListView):
    queryset = Faq.objects.filter()
    template_name = 'faq.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostPage(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'games.html'

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        fullmessage = 'Sender: ' + message_name + '\nEmail: ' + message_email + '\nMessage: ' + message
        
        # send an email
        send_mail(
            'Get Away Games MESSAGE', # subject
            fullmessage, # message
            settings.EMAIL_HOST_USER, # from email
            ['TonyTVKay@gmail.com'], # To Email
            )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def deals(request):
    return render(request, 'deals.html', {})