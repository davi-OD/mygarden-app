from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'pizza/home.htm')

def order(request):
	return render(request, 'pizza/order.htm')