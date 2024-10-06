
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import get_user_model

from django.db.models import Q, Sum, Count

from control.models import Project

from control.models import Like


# Create your views here.


def main(request):
    # Get the custom user model
    user = get_user_model()

    query = request.GET.get('search')

    if query:
        # Filter users by username if search query exists
        users = user.objects.filter(Q(username__icontains=query)).annotate(
            total_projects=Count('project'),
            total_likes=Sum('project__likes')
        )
    else:
        # If no search query, display all users
        users = user.objects.all().annotate(
            total_projects=Count('project'),
            total_likes=Sum('project__likes')
        )

    context = {
        'users': users,
    }

    return render(request, 'index.html', context)

def profile(request, username):

    users = get_user_model()

    # Fetch the user by username or return 404 if not found
    user = get_object_or_404(users, username=username)

    project = Project.objects.filter(user=user)


    context = {
        'project': project,
        'user': user,
    }




    return render(request, 'p.html', context)


def like_project(request, project_id):

    if request.method == 'POST':

        project = get_object_or_404(Project, id=project_id)

        # Check if the user has already liked the project

        already_liked = Like.objects.filter(user=request.user, project=project).exists()

        if not already_liked:

            # Create a new Like object
            Like.objects.create(user=request.user, project=project)

            # Increase the number of likes on the project
            project.likes += 1

            project.save()

            return JsonResponse({'likes': project.likes, 'message': 'Liked'})

        else:

            return JsonResponse({'likes': project.likes, 'message': 'Already liked'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)