from django.shortcuts import render, get_object_or_404, redirect
from .models import Community
from .forms import CommunityForm
from django.core.exceptions import PermissionDenied

# Create your views here.

# List
def community_list(request):
    community_list = Community.objects.all()
    return render(request, 'community_list.html', {'community_list':community_list})

# Create
def community(request):
    if request.method == 'POST':
        username = Community.objects.create(user=request.user)
        community_form = CommunityForm(request.POST, request.FILES, instance=username)
        
        if community_form.is_valid():
            community_form.save()
            return redirect('/communitylist/')
    else:
        community_form = CommunityForm()
    return render(request, 'community.html', {'community_form':community_form})

# Read
def community_detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    # comment_form = CommentForm()
    # return render(request, 'community_detail.html', {'community':community, 'comment_form':comment_form})
    return render(request, 'community_detail.html', {'community':community})

# Update
def community_update(request, community_id):
    community_update = get_object_or_404(Community, pk=community_id)
    if request.user == community_update.user:
        if request.method == 'POST':
            community_form = CommunityForm(request.POST, instance=community_update)
            if community_form.is_valid():
                community_form.save()
                return redirect('/community/'+str(community_id))
        else:
            community_form = CommunityForm(instance=community_update)
        return render(request, 'community_update.html', {'community_form':community_form})
    raise PermissionDenied # 권한없음 오류

# Delete
def community_delete(request, community_id):
    community = Community.objects.get(pk=community_id)
    if request.user == community.user:
        community.delete()
        return redirect('/communitylist/')
    raise PermissionDenied # 권한없음 오류