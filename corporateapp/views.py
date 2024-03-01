from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def sampleinner(request):
    return render(request, 'sample-inner-page.html')
