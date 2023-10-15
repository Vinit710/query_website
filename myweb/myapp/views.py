from django.shortcuts import render,redirect
from . models import ChatMessage,Resource


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

from django.shortcuts import render
from .models import ChatMessage

def query(request):
    parent_messages = ChatMessage.objects.filter(parent_message=None).order_by('-timestamp')
    return render(request, 'myapp/query.html', {'messages': parent_messages})





def about(request):
    return render(request, 'myapp/about.html')

def save_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        message = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        parent_message = ChatMessage.objects.get(id=parent_id) if parent_id else None
        ChatMessage.objects.create(sender=sender, message=message, parent_message=parent_message)
    return redirect('query')

def resources(request):
    # Retrieve resources data from the database
    mathematics_resources = Resource.objects.filter(subject='Mathematics')
    chemistry_resources = Resource.objects.filter(subject='Chemistry')
    # Add more subject-specific queries as needed

    context = {
        'mathematics_resources': mathematics_resources,
        'chemistry_resources': chemistry_resources,
        # Add more subject-specific resource variables as needed
    }

    return render(request, 'myapp/resources.html', context)

