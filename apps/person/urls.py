from django.urls import path
from .views import (
   CreateCollaborator, 
    
)



urlpatterns = [
    path('create_collaborator/', CreateCollaborator.as_view(), name='create_collaborator'),
]
