from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UserSignUp, UserLogin
from .models import UserProfile
from event_center.models import EventCenter, EventCenterReview
from food_drink.models import FoodDrink, FoodDrinkReview
from restaurant.models import Restaurant, RestaurantReview
from random import randint, shuffle
import os
# from django.core.paginator import Paginator, EmptyPage


def filter_model_objects_by_highest_rating(*model_object_args, item_count=0, randomize=False, shuffle_result=False):
    """
    Filter object in model by rating in descending order and return random
    model item based on the filtered result

    :param model_object_args: model objects
    :param item_count: Number of model objects to return for each model
    :param randomize: Return random result for model object filter
    :param shuffle_result: Shuffle list result
    :return: model_objects_list
    """
    if model_object_args:
        item_list_holder = []
        for model_object in model_object_args:
            if model_object:
                object_content = None
                object_item = model_object.filter(rating=5)
                if object_item.count() == 0:
                    object_item = model_object.filter(rating=4)
                if object_item.count() == 0:
                    object_item = model_object.filter(rating=3)
                if object_item.count() == 0:
                    object_item = model_object.filter(rating=2)
                if object_item.count() == 0:
                    object_item = model_object.filter(rating=1)
                if object_item.count() == 0:
                    object_item = model_object.filter(rating=0)
                if object_item.count() != 0:
                    rnd_val = 0
                    content_count = 0
                    obj_itm_count = object_item.count()
                    if obj_itm_count > 0:
                        content_count = item_count
                        if item_count <= 0:
                            # if specified number of model_object is greater than the model_object total number
                            if item_count > obj_itm_count:
                                content_count = obj_itm_count
                            elif item_count <= 0:
                                content_count = 1
                        # Loop through specified number of model_object to store each object in list
                        for num in range(content_count):
                            if randomize:   # Random Result if set
                                rnd_val = randint(0, (obj_itm_count - 1))
                                object_content = object_item.order_by('date_registered')[rnd_val]
                                if object_content:
                                    # Add model_objects to the list to be returned
                                    item_list_holder += [object_content]
                            else:
                                object_content = object_item.order_by('date_registered')[num]
                                if object_content:
                                    # Add model_objects to the list to be returned
                                    item_list_holder += [object_content]
        if shuffle_result:
            if len(item_list_holder) > 1:
                shuffle(item_list_holder)
        return item_list_holder
    return None


def get_model_top_review(model):
    """

    :param model: Event Center model
    :return: Model Object
    """
    all_objects = model
    models = []
    top_review_val = 0
    top_model_review = []

    def sort_acc_to_second_index(val):
        return val[1]

    if all_objects:
        for model in all_objects:
            no_of_review = 0
            if str(all_objects) == "EventCenter":
                try:
                    no_of_review = model.eventcenterreview.objects.count()
                except EventCenterReview.DoesNotExist:
                    no_of_review = 0
            if str(all_objects) == "Restaurant":
                try:
                    no_of_review = model.restaurantreview.objects.count()
                except RestaurantReview.DoesNotExist:
                    no_of_review = 0
            if str(all_objects) == "Food&Drink":
                try:
                    no_of_review = model.fooddrinkreview.objects.count()
                except FoodDrinkReview.DoesNotExist:
                    no_of_review = 0

            models.append([model, no_of_review])
        # Arrange reviews in ascending order
        models.sort(key=sort_acc_to_second_index, reverse=True)
        # models structure is  [ [ model1 , review_count ], [ model2 , review_count ], ... ]
        top_review_val = models[0][1]
        for model in models:
            # check for top review and similar alike and store all in list
            if model[1] == top_review_val:
                top_model_review += model
        top_review_len = len(top_model_review)
        if top_review_len > 0:
            top_review_len -= 1

        rnd_val = randint(0, top_review_len)
        model_result = top_model_review[rnd_val]
        if model_result:
            # return model with highest reviews
            return model_result


def index(request):
    user_form = UserSignUp()
    user_login_form = UserLogin()
    events = EventCenter.objects.all()
    restaurants = Restaurant.objects.all()
    food_drink = FoodDrink.objects.all()
    top_review = EventCenter.objects.all()
    # for i in top_review:
    #     i.eventcenterreview.objects.exists()
    slider_items = filter_model_objects_by_highest_rating(events, restaurants, food_drink, randomize=True)
    checkout_items = filter_model_objects_by_highest_rating(
        restaurants, events, food_drink, item_count=2, randomize=True, shuffle_result=True
    )
    top_review_items = []
    top_review_models = [food_drink, restaurants, events]
    curr_count_val = 0
    total_count_val = len(top_review_models)
    for count in range(3):
        top_review_items.append([])
        if curr_count_val > total_count_val:
            curr_count_val = 0
        for count2 in range(4):
            model_review_object = get_model_top_review(model=top_review_models[curr_count_val])
            if model_review_object:
                top_review_items[count].append(model_review_object)
        curr_count_val += 1
        shuffle(top_review_items[count])

    return render(request, 'arena/index.html', {
        'forms': user_form, 'login_form': user_login_form,
        'slider_items': slider_items, 'checkout_items': checkout_items,
        'top_reviews': top_review_items
    })


def contact(request):
    return render(request, 'arena/contact.html', {})


def process_user_signup(request):
    error_message = []
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        login_form = UserLogin()
        if form.is_valid():
            user_fname = form.cleaned_data.get('first_name')
            user_lname = form.cleaned_data.get('last_name')
            user_uname = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password')
            user_repass = form.cleaned_data.get('password2')

            if user_pass == user_repass:
                enc_salt = os.urandom(10).hex()
                # enc_password = user_func.hash_password(user_pass, enc_salt)
                try:
                    new_user = UserProfile.objects.get(username=user_uname)
                except UserProfile.DoesNotExist:
                    new_user_form = UserProfile.objects.create(
                        first_name=user_fname, last_name=user_lname, username=user_uname,
                        email=user_email
                    )
                    new_user_form.set_password(user_pass)
                    new_user_form.save()
                    user_log = authenticate(username=user_uname, password=user_pass)
                    # user_log = user_func.authenticate_user(username=user_uname, password=user_pass)
                    if user_log is not None:
                        login(request, user_log)
                        return redirect(reverse('arena:arena_dashboard:index'))
                else:
                    error_message.append('Username already exist')
                    return render(request, 'arena/base.html', {
                        'forms': form, 'login_form': login_form, 'error': error_message
                    })
            else:
                error_message.append('Passwords do not match')
        return render(request, 'arena/index.html', {'forms': form, 'login_form': login_form, 'error': error_message})

    return redirect(reverse('arena:index'))


def user_login(request):
    error_message = []
    user_signup_form = UserSignUp()
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        next_value = request.POST.get('next')

        if form.is_valid():
            uname = form.cleaned_data['username']
            passcode = form.cleaned_data['password']

            # user = user_func.authenticate_user(username=uname, password=passcode)
            user = authenticate(username=uname, password=passcode)
            if user is not None:
                login(request, user)
                if next_value:
                    return redirect(next_value)
                else:
                    return redirect(reverse('arena:arena_dashboard:index'))
            else:
                error_message.append("Invalid Login Details")
        form = UserLogin()
    return render(request, 'arena/index.html', {'forms': user_signup_form, 'login_form': form, 'login_error': error_message})


def user_logout(request):
    logout(request)
    return redirect(reverse('arena:index'))


def event_center(request):
    return render(request, "arena/eventcenter.html", {})

@login_required
def dash(request):
    return render(request, 'arena/dashboard.html', {})


def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': UserProfile.objects.filter(username__iexact=username).exists(),
    }
    if data['is_taken']:
        data['error_message'] = 'username already exists'
    return JsonResponse(data=data)
