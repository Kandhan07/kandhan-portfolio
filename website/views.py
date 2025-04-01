from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact  # Import the model

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save the data to the database
        Contact.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your message was sent successfully!")
        return redirect("home")  # Redirect to prevent resubmission

    return render(request, "index.html")

