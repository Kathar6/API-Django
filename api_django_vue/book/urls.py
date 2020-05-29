from rest_framework import routers

from .viewsets import BookViewSet

# SimpleRouter Define the basic routes of the models, routes like GET, POST, PUT, DELETE, etc.
router = routers.SimpleRouter()
# Register the ViewSet that we created previously
router.register('books', BookViewSet)

urlpatterns = router.urls
