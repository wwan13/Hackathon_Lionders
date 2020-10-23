from django.urls import path
from . import views

urlpatterns = [
    path('communitylist/',views.community_list,name='community-list'), # List
    path('community/',views.community,name='community'), # Create
    path('community/<int:community_id>', views.community_detail, name='community-detail'), # Read
    path('community/<int:community_id>/update', views.community_update, name='community-update'), # Update
    path('community/<int:community_id>/delete', views.community_delete, name='community-delete'), # Delete

    # comment
    path('create_comment/<int:community_id>', views.create_comment, name="create_comment"),
    path('delete_comment/<int:community_id>/<int:comment_id>/', views.delete_comment, name="delete_comment"),
]