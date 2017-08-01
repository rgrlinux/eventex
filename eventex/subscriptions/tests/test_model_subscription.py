from datetime import datetime

from django.test import TestCase
from  eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rogerio Oliveira',
            cpf='31095929836',
            email='rgrlinux@gmail.com',
            phone='11-980887373'
        )
        self.obj.save()

    def teste_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
