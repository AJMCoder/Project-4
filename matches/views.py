# matches/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Match
from .forms import MatchForm
from django.contrib import messages

@login_required
def submit_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Match result submitted successfully.')
                return redirect('recent_matches')
            except Exception as e:
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = MatchForm()
    return render(request, 'matches/submit_match.html', {'form': form})

def recent_matches(request):
    matches = Match.objects.order_by('-date_played')[:10]
    return render(request, 'matches/recent_matches.html', {'matches': matches})