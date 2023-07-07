from django.shortcuts import redirect
from .models import uploaded_files

def my_books_wrapper(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user has uploaded any files
        # has_uploaded_files = request.user.exists()
        file = uploaded_files.objects.filter(Name=request.user.username).all()
        print(file)
        if file.exists():
        # if request.user.is_authenticated:
            # User has uploaded files, allow access to the "My Books" view
            return view_func(request, *args, **kwargs)
        else:
            # No uploaded files, redirect to the "Upload Books" section
            return redirect('upload')

    return wrapper