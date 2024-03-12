from django.shortcuts import render

# Create your views here.
def skill(request):
    context = {'ski':'active'}
    return render(request, 'edu/skill.html', context)
