from django.shortcuts import render

def hairstyle(request):
    return render(request, 'design/hairstyle.html')

def about(request):
    return render(request, 'design/about.html', {'title': 'About'})

def hairdesign(request):
    return render(request, 'design/hairdesign.html', {'title': 'Hair Design'})

def news(request):
    return render(request, 'design/news.html', {'title': 'News'})

def contact(request):
    return render(request, 'design/contact.html', {'title': 'Contact'})

