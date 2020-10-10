from django.urls import path
from . import views

urlpatterns = [
    path('communitylist/',views.community_list,name='community-list'),
    path('community/',views.community,name='community'),
    path('community/<int:column_id>', views.community_detail, name='community-detail'),
    path('community/<int:column_id>/update', views.community_update, name='community-update'),
    path('community/<int:column_id>/delete', views.community_delete, name='community-delete'),
]