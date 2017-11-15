from django.test import TestCase

# Create your tests here.
from main_app.models import ReservationForm

class MailTestCase(TestCase):
    def test_printtest(self):
        print("DONNNE")
    def setUp(self):
        ReservationForm.objects.create(name = "Józio", lastName = "borysewicz", email = "Kinga.Gulewska@gmail.com", message = "witaj")
'''
    def test_send_mail(self):
        borysewicz= ReservationForm.objects.get(lastName="borysewicz")
        self.assertEqual(borysewicz.returname(),"Józio")
'''