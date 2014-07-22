from django.test import TestCase

from django.core.urlresolvers import reverse

from cms.models import MainMenu, Category, Entity, CategoryTypes

class TestsViewIndex(TestCase):
    def test_GeneratePage(self):
        response = self.client.get(reverse('cms:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mainmenu_list'], [])

    def test_GenerateMainmenuList(self):
        MainMenu.objects.create(name="[en]Test menu.", url="/")
        response = self.client.get(reverse('cms:index'))
	self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['mainmenu_list'],
            ['<MainMenu: [en]Test menu.>']
        )

class TestsViewCategoryList(TestCase):
    def test_GeneratePage(self):
        response = self.client.get(reverse('cms:types'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mainmenu_list'], [])
'''
class TestsViewEntityList(TestCase):
    def test_GeneratePage(self):
        response = self.client.get(reverse('cms:category', kwargs={'category_id':1} ))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mainmenu_list'], [])

class TestsViewEntity(TestCase):
    def test_GeneratePage(self):
        response = self.client.get(reverse('cms:entity', kwargs={'entity_id':1} ))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mainmenu_list'], [])
'''


