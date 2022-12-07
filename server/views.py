from django.shortcuts import render,redirect
def index(request):
    return render(request, 'index.html')

def post(request):
    #post방식
    if request.method == 'POST':
        post = Post()
        post.text = request.POST['text']
        post.save()
        return redirect('post')
    #get방식
    else:
        post = Post.objects.all()
        return render(request, 'index.html', {'post':post})