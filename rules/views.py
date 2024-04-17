from django.shortcuts import render
from .models import Rule

# Create your views here.
def rules(request):
    """
    Renders the Rules page
    """
    rules = Rule.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "rules/rules.html",
        {"rule": rules},
    )