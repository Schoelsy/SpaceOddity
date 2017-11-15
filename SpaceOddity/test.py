from django.test import TestCase
from main_app.models import ReservationForm

class MailTestCase(TestCase):
    def setUp(self):
        ReservationForm.objects.create(name = "Józio", lastName = "borysewicz", mail = "Kinga.Gulewska@gmail.com", message = "witaj")

    def test_send_mail(self):
        borysewicz= ReservationForm.objects.get(lastName="borysewicz")
        self.assertEqual(borysewicz.returname(),"Józio")
