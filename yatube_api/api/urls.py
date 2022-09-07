from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

# добавляю роутер
router = DefaultRouter()
# Чтобы роутер создал необходимый набор эндпоинтов, необходимо вызвать его метод register() 
# (говорят «зарегистрировать эндпоинты»). В качестве аргументов этот метод 
# принимает URL-префикс и название вьюсета, для которого создаётся набор эндпоинтов.
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
]