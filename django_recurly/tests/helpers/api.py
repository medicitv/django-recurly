from django.test import TestCase

from django_recurly.helpers import api
from django_recurly.tests.base import BaseTest, RequestFactory
from django_recurly.models import *
from django_recurly import views

rf = RequestFactory()

class GetSubscribeUrlTest(BaseTest):
    
    def ____test_encoding(self):
        html = api.get_change_plan_form(plan_code="myplan",
                                        subscription_id="403bfb8cefa599c6a3af954293b64987")
        
        self.assertTrue('<form action="/change-plan/" method="POST">' in html, html)
        self.assertTrue('input type="hidden" name="plan_code" value="myplan">' in html, html)
    
