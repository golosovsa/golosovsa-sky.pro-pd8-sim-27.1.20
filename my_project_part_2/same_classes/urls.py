from same_classes import views
from django.urls import path

# TODO здесь необходимо настроить urls
urlpatterns = [
   path("feedback/", views.FeedbackView.as_view(), name="feedback"),
   path("feedback/<int:id>/", views.FeedbackEntityView.as_view(), name="feedback_entity"),
   path("destination/", views.DestinationView.as_view(), name="destination"),
   path("destination/<int:id>/", views.DestinationEntityView.as_view(), name="destination_entity"),
   path("gen-destination/", views.DestinationListView.as_view(), name="gen_destination"),
   path("gen-destination/<int:pk>/", views.DestinationDetailView.as_view(), name="gen_destination_entity"),
]
