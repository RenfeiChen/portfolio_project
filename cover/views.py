from django.shortcuts import render


def cover(request):
    return render(request, 'cover/cover.html')
