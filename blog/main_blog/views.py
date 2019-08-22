from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def blog(request):
	#data = SessionStore()
	#print(data.session_key)
	return render(request, 'blog.html', {'title': 'MDT | Blog'})