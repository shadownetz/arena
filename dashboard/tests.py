from django.test import TestCase
from django.shortcuts import reverse
from index.models import UserProfile


class ArenaDashboardTest(TestCase):

    def setUp(self):
        self.user = UserProfile.objects.create(
            first_name='new',
            last_name='user',
            username='newuser',
            email='user@mail.com',
        )
        self.user.set_password(123456)
        self.user.save()

    def test_dashboard_pages_status_code_when_user_is_unauthenticated(self):
        response = self.client.get(reverse('arena:arena_dashboard:index'))  # test dashboard page
        response01 = self.client.get(reverse('arena:arena_dashboard:addEventCenter'))   # test addNewEvent Page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response01.status_code, 302)

    def test_dashboard_pages_status_code_when_user_is_authenticated(self):
        new_client = self.client
        page_status = new_client.login(username='newuser', password=123456)
        response = new_client.get(reverse('arena:arena_dashboard:index'))   # test dashboard page
        response01 = new_client.get(reverse('arena:arena_dashboard:addEventCenter'))     # test addNewEvent Page

        self.assertTrue(page_status)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response01.status_code, 200)


class ArenaAddNewEventTest(TestCase):

    pass
