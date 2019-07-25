from django.shortcuts import render
from .models import Board

# Create your views here.

def home(request):
    return render(request, 'newapp/index.html')
    
def newBoard(request):
    content={}
    try:
        title = request.POST.get('title')
        username = request.POST.get('userName')
        contents = request.POST.get('content')

        # DB에 새로운 게시글 DATA 생성하기
        board =Board(
            title=title,
            userName=username,
            contents=contents
        )
        board.save()
        content={'board':board}
    except:
        errMsg = "에러 발생!"
        content={'errMsg':errMsg}

    return render(request, 'newapp/readboard.html', content)

def board_view(request) :
    if Board.objects.all() != None :
        boards = Board.objects.all()
        context = {"boards" : boards }
        return render(request, 'newapp/boardview.html', context)
    else :
        return render(request, 'newapp/boardview.html')
        
def board(request, pk) :
    if Board.objects.all() != None :
        boards = Board.objects.get(pk=pk)
        context = {"board" : boards }
        return render(request, "newapp/board_one.html", context)

def board_update(request, pk) :
    if request.POST.get("pwd") == Board.objects.get(pk=pk).password :
       if request.POST.get("title") and request.POST.get("author") and request.POST.get("content") :
            board = Board.objects.get(pk=pk)
            board.title = request.POST.get("title")
            board.author = request.POST.get("author")
            board.content = requst.POST.get("content")
            board.save()
            return redirect('board')
    
    