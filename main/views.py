from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406401792',
        'name': 'Sean Marcello Maheron',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)