from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import logout

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, f"Account created for has been created! Your are able to login")
				return redirect('login')				
			except:
				pass
	else:
		form = UserCreationForm()

	
	context = {
		'form': form
	}			
	return render(request, 'accounts/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('login')