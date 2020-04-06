from django.shortcuts import render

# Create your views here.
def home(request):    
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()

    return render(request, 'wordcount/result.html', {'total': text})

