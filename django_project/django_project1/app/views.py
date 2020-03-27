from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from .forms import ArticleForm
from django.urls import reverse
from django.shortcuts import redirect

#def home(request):
#	list_articles = Articles.objects.all()
#	context = {
#		'list_articles': list_articles
#	}
#
#	return render(request, 'home.html', context)

#def detail_page(request,id):
#	get_article = Articles.objects.get(id=id)
#	context = {
#		'get_article':get_article
#	}
#	return render(request, 'detail.html', context)

class HomeListView(ListView):
	model = Articles
	template_name = 'home.html'
	context_object_name = 'list_articles'

class HomeDetailView(DetailView):
	model = Articles
	template_name = 'detail.html'
	context_object_name = 'get_article'

def edit_page(request):
	succes = False
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			succes = True

	template = 'edit.html'
	context = {
		'list_articles': Articles.objects.all().order_by('-id'),
		'form': ArticleForm(),
		'succes':succes
	}
	return render(request,template,context)

def update_page(request, pk):
	succes_update = False
	get_article = Articles.objects.get(pk=pk)
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance = get_article)
		if form.is_valid():
			form.save()
			succes_update = True

	template = 'edit.html'
	
	context = {
		'get_article': get_article,
		'update': True,
		'form': ArticleForm(instance = get_article),
		'succes_update':succes_update
	}
	return render(request, template,context)

def delete_page(request,pk):
	get_article = Articles.objects.get(pk=pk)
	get_article.delete()
	return redirect(reverse('edit_page'))