from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'hom':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context = {'con':'active'}
    return render(request, 'core/contact.html', context)