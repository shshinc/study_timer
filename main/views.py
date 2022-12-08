from django.shortcuts import render,redirect

def index(request):
    return render(request, 'index.html')

def after(request):
    goal = request.POST.get('goal')
    context = {'goal': goal,}
    return render(request, 'after.html', context)