from django.shortcuts import render, get_object_or_404, redirect
from .models import Community, Comment
from .forms import CommunityForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

# List
@login_required(login_url='/login/') # django의 decorators
def community_list(request):
    community_list = Community.objects.all()
    return render(request, 'community_list.html', {'community_list':community_list})

# Create
@login_required(login_url='/login/') # django의 decorators
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
@login_required(login_url='/login/') # django의 decorators
def community_detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    # comment_form = CommentForm()
    # return render(request, 'community_detail.html', {'community':community, 'comment_form':comment_form})
    return render(request, 'community_detail.html', {'community':community})

# Update
@login_required(login_url='/login/') # django의 decorators
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
@login_required(login_url='/login/') # django의 decorators
def community_delete(request, community_id):
    community = Community.objects.get(pk=community_id)
    if request.user == community.user:
        community.delete()
        return redirect('/communitylist/')
    raise PermissionDenied # 권한없음 오류

''' Comment '''
@login_required(login_url='/login/') # django의 decorators
def create_comment(request, community_id):
    if request.method == 'POST':
        comment = Comment()
        comment.community = get_object_or_404(Community, pk=community_id)
        comment.author = request.user
        comment.content = request.POST['comment']
        comment.created_at = timezone.datetime.now()
        comment.save()
    # if comment_form.is_valid():
    #     temp_form = comment_form.save(commit=False)
    #     temp_form.author = request.user
    #     temp_form.community = Community.objects.get(pk=community_id)
    #     temp_form.save()
        return redirect('community-detail', community_id)

@login_required(login_url='/login/') # django의 decorators
def delete_comment(request, community_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('community-detail', community_id)
    else:
        raise PermissionDenied