from django.shortcuts import render
from .models import Dogs, Cats
from PIL import Image

# Create your views here.
def index(request):
	
	return render(request, "dog/index.html")

def dogs(request):
	dogs = Dogs.objects.all()
	return render(request, "dog/dogs.html", {
		"dogs": dogs
	})

def cats(request):
	cats = Cats.objects.all()
	return render(request, "dog/cats.html", {
		"cats": cats
	})

def about(request):
	return render(request, "dog/about.html")

def volunteer(request):
	return render(request, "dog/volunteer.html")

def donation(request):
	return render(request, "dog/donation.html")

