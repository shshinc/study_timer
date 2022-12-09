from django.shortcuts import render,redirect

def index(request):
    return render(request, 'index.html')

def after(request):
    today_goal = request.POST.get('today_goal')
    week_goal = request.POST.get('week_goal')
    context = {'today_goal': today_goal,'week_goal':week_goal}
    return render(request, 'after.html', context)

def image(request):
    size = request.POST.get('size')
    doing_study = picture.get_study_time()
    return render(request, 'end.html', {'size':size,  'study_time' : doing_study})
