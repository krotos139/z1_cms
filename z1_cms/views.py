from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from cms.models import Entity,Category,CategoryTypes,MainMenu

# Create your views here.

from django.views.generic import ListView
class QCategory(ListView):
    model = Category
class QEntity(ListView):
    model = Entity

def index(request):
	mainmenu_list = MainMenu.objects.all()

	entity_all = Entity.objects.filter(category__type=CategoryTypes.mainpage).order_by('-pub_date')
	paginator = Paginator(entity_all, 10)
	page = request.GET.get('page')
	try:
		entity_list = paginator.page(page)
	except PageNotAnInteger:
		entity_list = paginator.page(1)
	except EmptyPage:
		entity_list = paginator.page(paginator.num_pages)

	context = {'mainmenu_list': mainmenu_list, 'entity_list': entity_list}
	return render(request, 'cms/index.html', context)

class index_rss(Feed):
    title = "Krotos139"
    link = "/"
    description = ""

    def items(self):
        return Entity.objects.filter(category__type=CategoryTypes.mainpage).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('cms:entity', kwargs={'entity_id':item.id})

def category_load(type, parrent):
    if parrent!=0:
    	category_list = Category.objects.filter(type=type, parrent=parrent)
    else:
	category_list = Category.objects.filter(type=type, parrent__isnull=True)
    for category in category_list:
    	category.chields = category_load(type, category.id)
    return category_list

def category_list(request):
    mainmenu_list = MainMenu.objects.all()

    mainpage_list = category_load(CategoryTypes.mainpage, 0)
    page_list = Category.objects.filter(type=CategoryTypes.page)
    article_list = Category.objects.filter(type=CategoryTypes.article)
    blog_list = Category.objects.filter(type=CategoryTypes.blog)
    forum_list = Category.objects.filter(type=CategoryTypes.forum)
    context = {'mainmenu_list': mainmenu_list, 'mainpage_list':mainpage_list, 'page_list': page_list, 'article_list':article_list, 'blog_list':blog_list, 'forum_list':forum_list }
    return render(request, 'cms/category_list.html', context)

def entity_list(request, category_id):
    mainmenu_list = MainMenu.objects.all()

    category_current = Category.objects.get(id=category_id)
    category_list = Category.objects.filter(parrent=category_id)
    entity_list = Entity.objects.filter(category=category_id)
    context = {'mainmenu_list': mainmenu_list, 'category_current': category_current, 'category_list': category_list, 'entity_list': entity_list}
    return render(request, 'cms/entity_list.html', context)

def entity(request, entity_id):
    mainmenu_list = MainMenu.objects.all()

    entity = Entity.objects.get(id=entity_id)
    context = {'mainmenu_list': mainmenu_list, 'entity': entity}
    return render(request, 'cms/entity.html', context)


