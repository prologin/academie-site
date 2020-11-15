from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from . import viewsets

router = routers.DefaultRouter()
router.register('track', viewsets.TrackInstanceViewSet, basename='track')
router.register('submission', viewsets.SubmissionViewSet, basename='submission')

track_subrouter = nested_routers.NestedSimpleRouter(router, 'track', lookup='track')
track_subrouter.register('problem', viewsets.ProblemViewSet, basename='track-problems')


urlpatterns = router.urls
urlpatterns += track_subrouter.urls