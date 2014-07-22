Django CMS "Z1 CMS"
===================

Простая система управления контентом, разработанная на Django. 

Установка
---------

После создания проекта django выполните следующие действия

1. Добавьте z1_cms и зависимые приложения в settings.py
```
INSTALLED_APPS = (
	...
	'z1_cms',
	'ckeditor',
	'tagging',
)
```
2. Добавьте переменные содержащие пути загрузки файлов в settings.py
```
ROOT_PATH = '/home/pr0/p1/'
STATIC_ROOT = ROOT_PATH +'static/'
STATIC_URL = '/static/'
MEDIA_ROOT = ROOT_PATH + 'media/'
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = "uploads/"
```
3. Добавьте URL приложения и зависимых модулей в urls.py::
```
urlpatterns = patterns('',
	...
	url(r'^z1_cms/', include('z1_cms.urls')),
	(r'^ckeditor/', include('ckeditor.urls')),
)
```
4. Для создания БД выполните `python manage.py syncdb`.

5. Запустите отладочный сервер и зайдите в админку по адресу http://127.0.0.1:8000/admin/

6. Зайдите по адресу http://127.0.0.1:8000/z1_cms/ для просмотра содержимого.



