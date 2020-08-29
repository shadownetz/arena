from django import forms
from event_center.models import EventCenter
from food_drink.models import FoodDrink
from restaurant.models import Restaurant
# from index.functions import generate_random_value


class AddEventCenterForm(forms.ModelForm):

    class Meta:
        model = EventCenter
        fields = (
            'owner', 'name', 'category', 'phone', 'mail', 'website',
            'can_book', 'address', 'availability', 'country',
            'state', 'image_rep', 'date_history'
        )
        exclude = ['ref_id', 'date_registered', 'rating']
        widgets = {
            'owner': forms.TextInput(attrs={
                'placeholder': 'Owner of event center',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of event center',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'custom-select select2',
                'data-placeholder': "Select a category",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'mail': forms.EmailInput(attrs={
                'placeholder': 'Email of event center',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '000-000-000-00000',
                'class': 'form-control input-mask',
                'autocomplete': 'off',
                'data-mask': '000-000-000-00000'
            }
            ),
            'website': forms.TextInput(attrs={
                'placeholder': 'Website link of event center',
                'class': 'form-control'
            }),
            'can_book': forms.CheckboxInput(attrs={
                'class': 'custom-control-input'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Event Center Address',
                'class': 'form-control'
            }),
            'availability': forms.CheckboxInput(attrs={
                'class': 'custom-control-input',
                'rows': "5"
            }),
            'country': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a country",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'state': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a state",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'image_rep': forms.FileInput(attrs={
                'class': 'custom-file-input'
            }),
            'date_history': forms.DateInput(attrs={
                'class': 'form-control date-picker flatpickr-input',
                'placeholder': 'Since when ?',
                'readonly': "readonly"
            })

        }


class AddFoodDrinkForm(forms.ModelForm):
    class Meta:
        model = FoodDrink
        fields = (
            'name', 'category', 'ingredients', 'assoc_country', 'assoc_states', 'image_rep'
        )
        exclude = ['ref_id', 'rating', 'date_registered']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'custom-select select2',
                'data-placeholder': "Select a category",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'List of ingredients',
                'class': 'form-control'
            }),
            'assoc_country': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a country",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'assoc_states': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a state",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'image_rep': forms.FileInput(attrs={
                'class': 'custom-file-input'
            }),
        }


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'owner', 'name', 'category', 'phone', 'mail', 'website', 'has_extras',
            'can_book', 'can_place_order', 'can_make_home_delivery', 'address', 'country',
            'state', 'open_time', 'close_time', 'image_rep', 'date_history'
        )
        exclude = ['ref_id', 'date_registered', 'rating', 'has_extras']
        widgets = {
            'owner': forms.TextInput(attrs={
                'placeholder': 'Owner of restaurant',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of restaurant',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'custom-select select2',
                'data-placeholder': "Select a category",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'mail': forms.EmailInput(attrs={
                'placeholder': 'Email of restaurant',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '000-000-000-00000',
                'class': 'form-control input-mask',
                'autocomplete': 'off',
                'data-mask': '000-000-000-00000'
            }
            ),
            'website': forms.TextInput(attrs={
                'placeholder': 'Website link of restaurant',
                'class': 'form-control'
            }),
            'can_book': forms.CheckboxInput(attrs={
                'class': 'custom-control-input'
            }),
            # 'has_extras': forms.CheckboxInput(attrs={
            #     'class': 'custom-control-input'
            # }),
            'can_place_order': forms.CheckboxInput(attrs={
                'class': 'custom-control-input'
            }),
            'can_make_home_delivery': forms.CheckboxInput(attrs={
                'class': 'custom-control-input'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Event Center Address',
                'class': 'form-control'
            }),
            'country': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a country",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'state': forms.Select(attrs={
                'class': 'select2 select2-hidden-accessible',
                'data-placeholder': "Select a state",
                'tabindex': "-1",
                'aria-hidden': "true"
            }),
            'image_rep': forms.FileInput(attrs={
                'class': 'custom-file-input'
            }),
            'open_time': forms.TimeInput(attrs={
                'class': 'form-control time-picker flatpickr-input',
                'placeholder': 'Opening Time ?',
                'readonly': "readonly"
            }),
            'close_time': forms.TimeInput(attrs={
                'class': 'form-control time-picker flatpickr-input',
                'placeholder': 'Closing Time ?',
                'readonly': "readonly"
            }),
            'date_history': forms.DateInput(attrs={
                'class': 'form-control date-picker flatpickr-input',
                'placeholder': 'Since when ?',
                'readonly': "readonly"
            })
        }
