from django.shortcuts import render

def index (request):
    """Página principal do learning_logs"""
    return render(request, 'learning_logs/index.html')