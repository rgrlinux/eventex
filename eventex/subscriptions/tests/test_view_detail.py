import unittest

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/1/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    @unittest.skip('averiguar')
    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

#    def test_context(self):
#        subscription = self.resp.context['subscription']
#        self.assertIsInstance(subscription, Subscription)
    @unittest.skip('averiguar')
    def test_html(self):
        self.assertContains(self.resp, 'Rogerio de Oliveira')
        self.assertContains(self.resp, '31095929836')
        self.assertContains(self.resp, 'rgrlinux@gmail.com')
        self.assertContains(self.resp, '11-980887373')
