from django.shortcuts import render, redirect


def welcome(request):
  if request.user.is_authenticated:
      return redirect('player_home')
  else:
    return render(request, 'tictactoe/welcome.html')

  #manila_pop = 1780148
  #3manila_area = 16.56
  #manila_pop_density = manila_pop / manila_area
  #return HttpResponse(manila_pop_density)
