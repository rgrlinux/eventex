from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rogerio Oliveira', cpf='31095929836',
                    email='rgrlinux@gmail.com', phone='11-98088-7373')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]                             

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'rgrlinux@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Rogerio Oliveira',
            '31095929836',
            'rgrlinux@gmail.com',
            '11-98088-7373'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

