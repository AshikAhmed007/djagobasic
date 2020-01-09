from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
def index(request):
	post=Article.objects.all()
	context={
	'post' : post
	}
	return render(request,'index.html',context)

def getauthor(request,name):
	return render(request,'profile.html')

def getsingle(request,id):
	post=get_object_or_404(Article,pk=id)
	first=Article.objects.first()
	last=Article.objects.last()
	related=Article.objects.filter(catagory=post.catagory).exclude(id=id)[ :4]
	context={
	"post":post,
	"first":first,
	"last":last,
	"related":related
	}
	return render(request,'single.html',context)

def gettopic(request,name):
	cat=get_object_or_404(Catagory,name=name)
	post=Article.objects.filter(catagory=cat.id)
	return render(request,'catagory.html',{'post':post,'cat':cat})