# -*- coding: utf-8 -*-
import logging
import json
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *

logger = logging.getLogger("blog.views")

# Create your views here.
def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }

def getNav(path):
    """获取显示在导航栏的内容"""
    pathlist = path.split('/')[1:]
    cata = pathlist[1] if len(pathlist)>1 else ''
    List = []

    ReuLink = Link.objects.all().order_by('index')  # 获取导航栏的链接
    for link in ReuLink:
        List.append({
            'title': link.title,
            'href': link.href,
            'active': 'mdui-color-green-200' if link.href == path else ''
        })

    ReuCatagory = Catagory.objects.filter(isLink=True).order_by('index') # 获取要显示在导航栏的分类
    for catagory in ReuCatagory:
        List.append({
            'title': catagory.name,
            'href': '/catagory/'+catagory.name,
            'active': 'mdui-color-green-200' if catagory.name == cata else ''
        })

    return List

def getArticle(where = None):
    ArticleList = []
    try:
        if where:
            ReuArticle = Article.objects.filter(catagory__name=where).order_by('-id')
        else:
            ReuArticle = Article.objects.order_by('-id')
        for articles in ReuArticle:
            nick = articles.user.first_name if articles.user.first_name else articles.user.username
            email = articles.user.email if articles.user.email else '还没有设置邮箱'
            header = articles.user.avatar
            catagory = articles.catagory.name
            tags = articles.tags.name
            ArticleList.append({
                'id': articles.id,
                'nick': nick,
                'email': email,
                'header': header,
                'title': articles.title,
                'desc': articles.desc,
                'catagory': catagory,
                'tags': tags
            })
    except Exception as e:
        logger.error(e)
    return ArticleList


def index(request):
    return render(request, 'index.html',{'ArticleList': getArticle(), 'LinkList': getNav(request.path)})

def catagory(request):
    paths = request.path.split('/')[1:]
    content = {}
    commentList = []
    if len(paths)==3:
        articles = Article.objects.filter(id=paths[2].split('-')[0])[0]
        ReuComment = Comment.objects.filter(articleid=articles.id).order_by('-id')
        for comment in ReuComment:
            if not comment.onlyauthor:
                commentList.append({
                    'nick': comment.nick,
                    'email': comment.email,
                    'content': comment.content
                })
        nick = articles.user.first_name if articles.user.first_name else articles.user.username
        email = articles.user.email if articles.user.email else '还没有设置邮箱'
        header = articles.user.avatar
        catagory = articles.catagory.name
        tags = articles.tags.name
        content = {
            'id': articles.id,
            'nick': nick,
            'email': email,
            'header': header,
            'title': articles.title,
            'desc': articles.desc,
            'text': articles.content,
            'catagory': catagory,
            'tags': tags,
            't_up': articles.t_up,
            't_down': articles.t_down
        }
    return render(request, 'index.html', {'content': content, 'CommentList': commentList, 'ArticleList': getArticle(paths[1]),'LinkList': getNav(request.path)})

def comment(request):
    Result = {'Code': 0, 'Message': '参数无效'}
    if request.GET['type'] in 'addADD':
        if request.POST:
            onlyauthor = request.POST['onlyauthor']
            email = request.POST['email']
            nickname = request.POST['nickname']
            content = request.POST['content']
            articleid = request.POST['articleid']
            comments = Comment(
                nick=nickname,
                email=email,
                content=content,
                onlyauthor=onlyauthor,
                articleid=articleid
            )
            comments.save()
            Result['Code'] = 1
            Result['Message'] = "添加成功!"
    elif request.GET['type'] in "thumbTHUMB":
        if request.POST:
            thumb = int(request.POST['thumb'])
            articleid = request.POST['articleid']
            ReuArticle = Article.objects.get(id=articleid)
            if thumb:
                ReuArticle.t_up = ReuArticle.t_up+1
                Result['Message'] = "守护成功!"
            else:
                ReuArticle.t_down = ReuArticle.t_down+1
                Result['Message'] = "踩踏成功!"
            ReuArticle.save()
            Result['Code'] = 1

    return HttpResponse(json.dumps(Result))

def frpManger(request):
    Result = {'Code': 0, 'Message': '请给TOKEN参数!'}
    if request.GET:
        frplist = []
        ReuFrplist = FrpsList.objects.filter(token=request.GET['token'])
        for frp in ReuFrplist:
            frplist.append({
                'Id': frp.id,
                'name': frp.name,
                'data': frp.data,
                'message': frp.message
            })
        if len(frplist):
            Result['Code'] = 1
            Result['Message'] = "获取成功!"
            Result['Data'] = frplist
        else:
            Result['Code'] = 0
            Result['Message'] = "获取失败,此TOKEN没有Frp服务!"
    return HttpResponse(json.dumps(Result))