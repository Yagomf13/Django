from django.urls import path
from .views import PagesListView, PageDetailView, PageCreate, PageUpdate, PageDelete

pages_patterns = ([    #Cambio de nombre
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'), #manera de llamar a una url por la id y por su slug
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PageDelete.as_view(), name='delete'),
], 'pages')   