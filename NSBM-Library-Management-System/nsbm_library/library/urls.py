from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet


router = DefaultRouter()
router.register('author', AuthorViewSet)
router.register('category', CategoryViewSet)
router.register('book', BookViewSet)

urlpatterns = router.urls