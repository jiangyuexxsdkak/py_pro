from django.shortcuts import render,HttpResponse,render_to_response
from app1.models import Article
# Create your views here.

def index(request):
    body = "你好,江跃先生！"
    body = Article.objects.all()
    # return HttpResponse(body)
    return render_to_response('index.html',{"body":body}) #模板

def test(request):
    body = "你好,江跃先生！我是Test。"
    # body = Article.objects.all()
    return HttpResponse(body)
    # return render_to_response('index.html',{"body":body})