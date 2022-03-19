from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())

    def test_done_field_not_required(self):
        form = ItemForm({"name": "name"})
        self.assertTrue(form.is_valid())
