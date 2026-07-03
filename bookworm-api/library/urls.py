from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register('category',CategoryViewSet)
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)

urlpatterns = router.urls
