from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        user_name = request.user.first_name or request.user.username
        return render(request, 'home/welcome.html', {
            'user_name': user_name,
            'template_data': {'title': 'Welcome back'}
        })

    template_data = {}
    template_data['title'] = 'Chef++'
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    return render(request, 'home/about.html')