
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import CustomUser, Project

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages, auth


def signin(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        password1 = request.POST['password_c']

        email = request.POST['email']

        description = request.POST['description']

        git = request.POST['git']


        if password == password1:

            if CustomUser.objects.filter(username=username).exists():

                messages.error(request, "Username already exists. Please choose a different one.")

                return render(request, "signup.html")

            else:

                user = CustomUser.objects.create_user(username=username, email=email, password=password)

                # Add additional fields (such as git and description) manually

                user.git = git

                user.description = description

                user.save()

                return redirect('login')

    return render(request, "signup.html")


def log_in(request):


    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        error = """

                                 You Have Enter Wrong Credidential\n

                                     Login To View Your Profile

                                 """

        if user is not None:

            login(request, user)

            return redirect('profile')

        else:

            messages.error(request, error)

            return redirect("login")

    return render(request, "login.html")


def logout(request):

    auth.logout(request)

    return redirect('login')

@login_required(login_url='login')
def profile(request):

    user = request.user  # Get the currently logged-in user

    if request.method == 'POST':

        if 'info'  in request.POST:  # Handle profile update

            description = request.POST['description']

            username = request.POST['username']

            git = request.POST['git']

            pict = request.FILES.get('pict')

            bg = request.FILES.get('bg')

            email = request.POST['email']

            tech = request.POST['tech']

            if pict:

                user.pict = pict

            if bg:

                user.cover = bg

            if username:

                user.username = username

            if git:

                user.git = git

            if description:
                user.description = description

            if email:

                user.email = email

            if tech:

                user.tech = tech

            user.save()  # Save updated user

        else:

            name = request.POST.get('name')

            img = request.FILES.get('img')

            description = request.POST.get('description')

            git = request.POST.get('git')

            tech = request.POST.get('tech')

            # Create and associate the project with the current user
            project = Project.objects.create(

                user=request.user,
                # Associate the project with the logged-in user
                name=name,

                img=img,

                description=description,

                git=git,

                tech=tech
            )

    project = Project.objects.filter(user=request.user)

    context = {
        'project': project,
        'user': user,
    }

    return render(request, "profile.html", context)

































































# <--- <button class="btn btn-danger btn-sm position-absolute" style="top: 10px; right: 10px;" name="delete" type="">Delete</button> --->