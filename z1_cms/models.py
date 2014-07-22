from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
import datetime
from filebrowser.fields import FileBrowseField
from tagging.fields import TagField
from ckeditor.fields import RichTextField

class MainMenu(models.Model):
    parrent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)


class CategoryTypes:
    uncknown = 0;
    mainpage = 1;
    page = 2;
    article = 3;
    blog = 4;
    private = 5;
    forum = 6;
    choices = (
        (uncknown, _('Uncknown')),
        (mainpage, _('Main page content')),
        (page, _('Static page')),
        (article, _('Article')),
        (blog, _('Blog')),
        (private, _('Private data')),
        (forum, _('Forum'))
    )


class Category(models.Model):
    parrent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=CategoryTypes.choices, default=CategoryTypes.uncknown)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Entity(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50, blank = False)
    content  = RichTextField(verbose_name=_('Content'), blank = False)
    author = models.ForeignKey(User, verbose_name=_('Author'))
    pub_date = models.DateTimeField(verbose_name=_('Date of publication'), default=datetime.datetime.now)
    category = models.ForeignKey(Category, verbose_name=_('Category'), blank = False)
    tags = TagField(verbose_name=_('Tags'))
    stat_views = models.IntegerField(verbose_name=_('Number of views'), default=0)
    stat_rating = models.IntegerField(verbose_name=_('Rating'), default=0)

    def published(self):
        return self.pub_date >= timezone.now()

    def __unicode__(self):
        return u'%s' % (self.name)



