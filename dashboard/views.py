from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from django.contrib.auth import logout
from .models import Profile, UserProfile
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from .forms import (AddEventCenterForm, AddFoodDrinkForm, AddRestaurantForm)
from index.functions import generate_random_value
from event_center.models import EventCenter
from food_drink.models import FoodDrink
from restaurant.models import Restaurant
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)


@login_required
def get_user_profile_info(request):
    user_a = get_object_or_404(UserProfile, pk=request.user.id)
    user_a1 = get_object_or_404(Profile, user=user_a.profile.user)
    return user_a1


@login_required
def index(request):
    event_center_count = EventCenter.objects.count()
    food_drink_count = FoodDrink.objects.count()
    return render(request, "arena/dashboard.html", {
        'event_center_count': event_center_count, 'food_drink_count': food_drink_count
    })


@login_required
def user_profile(request):
    return render(request, "arena/profile-contacts.html", {})


@login_required
def update_profile(request):
    """
    Updates Profile data according to values in request object from ajax
    :param request:
    :return: object
    """
    # data_object = request.POST.get('data_object')
    fname, lname, uname, passcode, pnumber, about, pub_id = '', '', '', '', '', '', ''
    if request.method == 'POST':
        if not request.user.is_superuser:
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('username')
            passcode = request.POST.get('passcode')
            pnumber = request.POST.get('pnumber')
            about = request.POST.get('about')
            pub_id = request.POST.get('pub_id')
            email = request.POST.get('email')

            # Check if user is authenticated
            if request.user.is_authenticated:
                user = get_object_or_404(UserProfile, pk=request.user.id)
                if len(fname) > 0:
                    user.first_name = fname
                if len(lname) > 0:
                    user.last_name = lname
                if (uname is not None) and (len(uname) > 0):
                    user.username = uname
                if (passcode is not None) and (len(passcode) > 0):
                    user.set_password(passcode)
                    update_session_auth_hash(request, user=user)
                if (pnumber is not None) and (len(pnumber) > 0):
                    user.profile.phone_number = pnumber
                if (about is not None) and (len(about) > 0):
                    user.profile.about = about
                if (pub_id is not None) and (len(pub_id) > 0):
                    user.profile.nick_name = pub_id
                if (email is not None) and (len(email) > 0):
                    user.email = email
                user.profile.save()
                user.save()
                # Send User information with success message after profile update
                re_data = {
                    'success_msg': 'Updated Successfully',
                    'fname': user.first_name,
                    'lname': user.last_name,
                    'email': user.email,
                    'username': user.username,
                    'phone': user.profile.phone_number,
                    'about': user.profile.about,
                    'pubId': user.profile.nick_name
                }
                return JsonResponse(data=re_data)
        else:
            return JsonResponse(data={})
    request.session.clear()
    return redirect(reverse('arena:index'))


@login_required
def profile_data_request(request):
    """
    Function to receive Ajax request and send user details
    :param request:
    :return: JSON Object
    """
    if request.user.is_authenticated:
        # superuser cannot edit profile from dashboard
        if not request.user.is_superuser:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            data_object = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'phone_number': user.profile.phone_number,
                'about': user.profile.about,
                'pub_id': user.profile.nick_name,
                'email': user.email
            }
            return JsonResponse(data=data_object)
        else:
            return JsonResponse(data={})
    request.session.clear()
    return redirect(reverse('arena:index'))


@login_required
def add_event_center(request):
    if request.user.is_staff:
        add_event_form = AddEventCenterForm()
        event_center_ref = request.GET.get('center')
        event_center_id = request.GET.get('id')
        if (event_center_ref is not None) or (event_center_id is not None):
            event_center = get_object_or_404(EventCenter, ref_id=event_center_ref, id=event_center_id)
            add_event_form = AddEventCenterForm(instance=event_center)
            return render(request, 'arena/admin/addEvent.html', {'form': add_event_form})
        return render(request, 'arena/admin/addEvent.html', {'form': add_event_form})
    return redirect(reverse('arena:arena_dashboard:index'))


@login_required
def modify_event_center(request):
    if request.user.is_staff and request.method == 'POST':
        event_center_ref = request.GET.get('center')
        event_center_id = request.GET.get('id')
        view_event_page_pos = request.GET.get('pos')
        event_center_to_change = get_object_or_404(EventCenter, ref_id=event_center_ref, id=event_center_id)
        form = AddEventCenterForm(request.POST, request.FILES, instance=event_center_to_change)
        form.save()
        # form = AddEventCenterForm()
        # page = request.GET.get('page')
        if view_event_page_pos is None:
            view_event_page_pos = 1
        event_center = EventCenter.objects.all().order_by('date_registered')
        paginator = Paginator(event_center, 10)
        try:
            event_centers = paginator.get_page(view_event_page_pos)
        except PageNotAnInteger:
            event_centers = paginator.get_page(1)
        except EmptyPage:
            event_centers = Paginator.get_page(paginator.num_pages)
        # After change redirect to page that displays all event centers at previous page position
        return render(request, 'arena/admin/viewAllEvent.html', {'all_event': event_centers, 'add_success': True, 'alert_script': True})
    return redirect(reverse('arena:index'))


@login_required
def process_add_new_event_center(request):
    form = AddEventCenterForm()
    if request.method == 'POST':
        form = AddEventCenterForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_staff:
            tmp_addr = form.cleaned_data['address']
            # Prevent re-saving already saved event center
            event = EventCenter.objects.filter(address=tmp_addr).exists()
            if not event:
                owner = form.cleaned_data['owner']
                name = form.cleaned_data['name']
                category = form.cleaned_data['category']
                phone = form.cleaned_data['phone'].replace('-', "")
                mail = form.cleaned_data['mail']
                website = form.cleaned_data['website']
                can_book = form.cleaned_data['can_book']
                address = form.cleaned_data['address']
                availability = form.cleaned_data['availability']
                country = form.cleaned_data['country']
                state = form.cleaned_data['state']
                image = form.cleaned_data['image_rep']
                history = form.cleaned_data['date_history']
                ref_id = generate_random_value(10)
                # FIXME:Validate for same reference id found
                new_event = EventCenter.objects.create(
                    owner=owner, name=name, ref_id=ref_id, category=category,
                    phone=phone, mail=mail, website=website, can_book=can_book,
                    address=address, availability=availability, country=country,
                    state=state, image_rep=image, date_history=history
                )
                new_event.save()
                form = AddEventCenterForm()
                return render(request, 'arena/admin/addEvent.html', {'form': form, 'add_success': True, 'alert_script': True})
            else:
                form = AddEventCenterForm()
    return render(request, 'arena/admin/addEvent.html', {'form': form})


# class EventAllView(LoginRequiredMixin, generic.ListView):
#     model = EventCenter
#     login_url = '/'
#     redirect_field_name = 'redirect_to'
#     template_name = 'arena/admin/viewAllEvent.html'
#     context_object_name = 'all_event'
#     paginate_by = 3
#     queryset = EventCenter.objects.all()


@login_required
def view_all_event_center(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    event_center = EventCenter.objects.all().order_by('date_registered')
    paginator = Paginator(event_center, 10)
    try:
        event_centers = paginator.get_page(page)
    except PageNotAnInteger:
        event_centers = paginator.get_page(1)
    except EmptyPage:
        event_centers = Paginator.get_page(paginator.num_pages)
    return render(request, 'arena/admin/viewAllEvent.html', {'all_event': event_centers})


@login_required
def add_new_food_drink(request):
    if request.user.is_staff:
        add_food_drink_form = AddFoodDrinkForm()
        item_ref = request.GET.get('item')
        item_id = request.GET.get('id')
        if (item_ref is not None) or (item_id is not None):
            item = get_object_or_404(FoodDrink, ref_id=item_ref, id=item_id)
            add_item_form = AddFoodDrinkForm(instance=item)
            return render(request, 'arena/admin/addFoodDrink.html', {'form': add_item_form})
        return render(request, 'arena/admin/addFoodDrink.html', {'form': add_food_drink_form})
    return redirect(reverse('arena:arena_dashboard:index'))


@login_required
def process_add_new_food_drink(request):
    form = AddFoodDrinkForm()
    if request.method == 'POST':
        form = AddFoodDrinkForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_staff:
            name = form.cleaned_data['name']
            country = form.cleaned_data['assoc_country']
            state = form.cleaned_data['assoc_states']
            category = form.cleaned_data['category']
            ingredients = form.cleaned_data['ingredients']
            item_image = form.cleaned_data['image_rep']
            # Prevent re-saving already saved food_drink item
            item = FoodDrink.objects.filter(
                name=name, assoc_country=country, assoc_states=state, category=category
            ).exists()
            if not item:
                ref_id = generate_random_value(10)
                # FIXME:Validate for same reference id found
                new_item = FoodDrink.objects.create(
                    category=category, ref_id=ref_id, name=name, ingredients=ingredients,
                    assoc_country=country, assoc_states=state, image_rep=item_image
                )
                new_item.save()
                form = AddFoodDrinkForm()
                return render(request, 'arena/admin/addFoodDrink.html',
                              {'form': form, 'add_success': True, 'alert_script': True})
            else:
                form = AddFoodDrinkForm()
    return render(request, 'arena/admin/addFoodDrink.html', {'form': form})


@login_required
def view_all_food_drink_item(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    item = FoodDrink.objects.all().order_by('date_registered')
    paginator = Paginator(item, 10)
    try:
        item = paginator.get_page(page)
    except PageNotAnInteger:
        item = paginator.get_page(1)
    except EmptyPage:
        item = Paginator.get_page(paginator.num_pages)
    return render(request, 'arena/admin/viewAllFoodDrink.html', {'all_item': item})


@login_required
def modify_food_drink_item(request):
    if request.user.is_staff and request.method == 'POST':
        item_ref = request.GET.get('item')
        item_id = request.GET.get('id')
        view_item_page_pos = request.GET.get('pos')
        item_to_change = get_object_or_404(FoodDrink, ref_id=item_ref, id=item_id)
        form = AddFoodDrinkForm(request.POST, request.FILES, instance=item_to_change)
        form.save()
        # form = AddEventCenterForm()
        # page = request.GET.get('page')
        if view_item_page_pos is None:
            view_item_page_pos = 1
        item = FoodDrink.objects.all().order_by('date_registered')
        paginator = Paginator(item, 10)
        try:
            items = paginator.get_page(view_item_page_pos)
        except PageNotAnInteger:
            items = paginator.get_page(1)
        except EmptyPage:
            items = Paginator.get_page(paginator.num_pages)
        # After change redirect to page that displays all event centers at previous page position
        return render(request, 'arena/admin/viewAllFoodDrink.html', {'all_item': items, 'add_success': True, 'alert_script': True})
    return redirect(reverse('arena:index'))


@login_required
def add_restaurant(request):
    if request.user.is_staff:
        add_restaurant_form = AddRestaurantForm()
        restaurant_ref = request.GET.get('center')
        restaurant_id = request.GET.get('id')
        if (restaurant_ref is not None) or (restaurant_id is not None):
            restaurant = get_object_or_404(Restaurant, ref_id=restaurant_ref, id=restaurant_id)
            add_restaurant_form = AddRestaurantForm(instance=restaurant)
            return render(request, 'arena/admin/addRestaurant.html', {'form': add_restaurant_form})
        return render(request, 'arena/admin/addRestaurant.html', {'form': add_restaurant_form})
    return redirect(reverse('arena:arena_dashboard:index'))


@login_required
def process_add_restaurant(request):
    form = AddRestaurantForm()
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_staff:
            tmp_addr = form.cleaned_data['address']
            # Prevent re-saving already saved restaurant
            restaurant = Restaurant.objects.filter(address=tmp_addr).exists()
            if not restaurant:
                owner = form.cleaned_data['owner']
                name = form.cleaned_data['name']
                category = form.cleaned_data['category']
                phone = form.cleaned_data['phone'].replace('-', "")
                mail = form.cleaned_data['mail']
                website = form.cleaned_data['website']
                has_extras = False
                can_book = form.cleaned_data['can_book']
                can_place_order = form.cleaned_data['can_place_order']
                can_make_home_delivery = form.cleaned_data['can_make_home_delivery']
                address = form.cleaned_data['address']
                country = form.cleaned_data['country']
                state = form.cleaned_data['state']
                open_time = form.cleaned_data['open_time']
                close_time = form.cleaned_data['close_time']
                image = form.cleaned_data['image_rep']
                history = form.cleaned_data['date_history']
                ref_id = generate_random_value(10)
                if can_book or can_make_home_delivery or can_place_order:
                    has_extras = True
                # FIXME:Validate for same reference id found
                new_restaurant = Restaurant.objects.create(
                    owner=owner, name=name, ref_id=ref_id, category=category,
                    phone=phone, mail=mail, website=website, has_extras=has_extras,
                    can_book=can_book, can_place_order=can_place_order, can_make_home_delivery=can_make_home_delivery,
                    address=address, country=country, state=state, open_time=open_time, close_time=close_time,
                    image_rep=image, date_history=history
                )
                new_restaurant.save()
                form = AddRestaurantForm()
                return render(request, 'arena/admin/addRestaurant.html',
                              {'form': form, 'add_success': True, 'alert_script': True})
            else:
                form = AddRestaurantForm()
    return render(request, 'arena/admin/addRestaurant.html', {'form': form})


@login_required
def view_all_restaurants(request):
    page = request.GET.get('page')
    if page is None:
        page = 1
    restaurant = Restaurant.objects.all().order_by('date_registered')
    paginator = Paginator(restaurant, 10)
    try:
        restaurants = paginator.get_page(page)
    except PageNotAnInteger:
        restaurants = paginator.get_page(1)
    except EmptyPage:
        restaurants = Paginator.get_page(paginator.num_pages)
    return render(request, 'arena/admin/viewAllRestaurant.html', {'all_restaurant': restaurants})


@login_required
def modify_restaurant(request):
    if request.user.is_staff and request.method == 'POST':
        restaurant_ref = request.GET.get('center')
        restaurant_id = request.GET.get('id')
        view_restaurant_page_pos = request.GET.get('pos')
        restaurant_to_change = get_object_or_404(Restaurant, ref_id=restaurant_ref, id=restaurant_id)
        form = AddRestaurantForm(request.POST, request.FILES, instance=restaurant_to_change)
        form.save()
        # form = AddEventCenterForm()
        # page = request.GET.get('page')
        if view_restaurant_page_pos is None:
            view_restaurant_page_pos = 1
        restaurant = Restaurant.objects.all().order_by('date_registered')
        paginator = Paginator(restaurant, 10)
        try:
            restaurants = paginator.get_page(view_restaurant_page_pos)
        except PageNotAnInteger:
            restaurants = paginator.get_page(1)
        except EmptyPage:
            restaurants = Paginator.get_page(paginator.num_pages)
        # After change redirect to page that displays all event centers at previous page position
        return render(request, 'arena/admin/viewAllRestaurant.html', {'all_restaurant': restaurants, 'add_success': True, 'alert_script': True})
    return redirect(reverse('arena:index'))