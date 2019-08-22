from django.shortcuts import render

# Create your views here.
def home(request):
	#data = SessionStore()
	#print(data.session_key)
	return render(request, 'default.html', {'title': 'MDT | Home'})