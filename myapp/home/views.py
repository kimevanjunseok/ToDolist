from django.shortcuts import render, redirect
from .models import Boards

# Create your views here.
def index(request):
    boards = Boards.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        finished_at = request.POST.get('finished_at')

        if finished_at:
            board = Boards(title=title, content=content, finished_at=finished_at)
        else:
            board = Boards(title=title, content=content)

        board.save()

        return redirect('home:index')
    else:

        return render(request, 'create.html')

def detail(request, board_pk):
    board = Boards.objects.get(pk=board_pk)
    context = {
        'board': board,
    }
    return render(request, 'detail.html', context)

def update(request, board_pk):
    board = Boards.objects.get(pk=board_pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.finished_at = request.POST.get('finished_at')

        board.save()

        return redirect('home:detail', board_pk)

    else:
        context = {
            'board': board,
        }
        return render(request, 'update.html', context)

def delete(request, board_pk):
    board = Boards.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('home:index')
    else:
        return redirect('home:detail', board_pk)
        
