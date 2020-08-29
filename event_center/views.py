from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import EventCenter
from index.forms import UserSignUp, UserLogin

# Create your views here.


def index(request):
    page = request.GET.get("page")
    user_form = UserSignUp()
    user_login_form = UserLogin()
    if page is None:
        page = 1
    centers_models = EventCenter.objects.all().order_by("rating")[::-1]
    centers_page = Paginator(centers_models, 18)
    try:
        center_item = centers_page.get_page(page)
    except PageNotAnInteger:
        center_item = centers_page.get_page(1)
    except EmptyPage:
        center_item = centers_page.get_page(centers_page.num_pages)
    return render(request, "arena/eventcenter.html", {
        "forms": user_form,
        "login_form": user_login_form,
        "centers": center_item})


def center(request):
    return render(request, 'arena/center_content.html', {})
