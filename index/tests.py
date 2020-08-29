from django.test import TestCase
from django.urls import reverse
from .models import UserProfile
# from dashboard.models import Profile
# from django.utils import timezone
# from .forms import UserSignUp


class ArenaHomeTest(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200, msg='HomePage Not Available')

    def test_view_url_by_name(self):
        response = self.client.get(reverse('arena:index'))
        self.assertEquals(response.status_code, 200, msg='HomePage View not Available')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('arena:index'))
        self.assertTemplateUsed(response, 'arena/index.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="#">arena</a>')

    def test_unauthenticated_user_is_redirected(self):
        response = self.client.get(reverse('arena:arena_dashboard:index'))
        self.assertRedirects(response, '/?next=/dashboard/')


class ArenaSignUpTest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(
            first_name='first',
            last_name='user',
            username='firstuser',
            email='first_user123@mail.com',
        )
        self.user.set_password(123456)
        self.user.save()

    def test_user_profile_is_created(self):
        """
        Profile Table is automatically created when user model is created
        so check if the user profile table is created
        :return: Nil
        """
        response = self.user.profile
        user_profile_phone = response.phone_number
        user_nick_name = response.nick_name
        user_about = response.about
        self.assertNotEquals(response, '')
        self.assertEquals(user_profile_phone, None)
        self.assertEquals(user_about, None)
        self.assertEquals(user_nick_name, None)

    def test_user_can_login_after_signup(self):
        response = self.client.login(username='firstuser', password=123456)
        self.assertTrue(response)


class ArenaLoginTest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(
            first_name='new',
            last_name='user',
            username='newuser',
            email='user@mail.com',
        )
        self.user.set_password(123456)
        self.user.save()

    def test_valid_user_can_login(self):
        response = self.client.login(username='newuser', password=123456)
        self.assertTrue(response)

    def test_reject_invalid_login_credentials(self):
        response = self.client.login(username='', password='')
        self.assertFalse(response)

    def test_unauthenticated_user_does_not_have_access_to_dashboard(self):
        response = self.client.get(reverse('arena:arena_dashboard:index'))
        self.assertEquals(response.status_code, 302)

    def test_authenticated_user_has_access_to_dashboard(self):
        self.client.login(username='newuser', password=123456)
        response = self.client.get(reverse('arena:arena_dashboard:index'))
        self.assertEquals(response.status_code, 200)

    def test_authenticated_user_cannot_have_access_to_superuser_page(self):
        response = self.client.get(reverse('arena:arena_dashboard:su'))
        self.assertEquals(response.status_code, 302)
