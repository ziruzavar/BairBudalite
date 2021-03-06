from django.test import TestCase, Client

from BairBudalite.models import Pohodi, Budali


class IndexViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_pohodi = 4
        number_of_budali = 4

        for pohod_id in range(number_of_pohodi):
            Pohodi.objects.create(
                title=f'Pohod {pohod_id}',
                description=f'Desc {pohod_id},'
            )

        for budali_id in range(number_of_budali):
            Budali.objects.create(
                name=f'Budala {budali_id}',
                pohodi=budali_id,
                image_src='none',
            )

    def setUp(self):
        self.test_client = Client()

    def test_getIndexView_shouldReturnCorrectTemplate(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'index.html')

    def test_IndexView_Pohodi_shouldReturnCorrectContext(self):
        response = self.test_client.get('')
        pohodi = response.context['pohodi']
        self.assertEqual(len(pohodi), 3)
        self.assertEqual(str(pohodi[0]), 'Pohod 3')

    def test_IndexView_Budali_shouldReturnCorrextContext(self):
        response = self.test_client.get('')
        budali = response.context['budali']
        self.assertEqual(len(budali), 4)
        self.assertEqual(str(budali[0]), 'Budala 3')


class PohodiViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getPohodiView_shouldReturnCorrectTemplate(self):
        response = self.test_client.get('/pohodi')
        self.assertTemplateUsed(response, 'generic.html')


class ProjectViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getProjectView_shouldReturnCorrectTemplate(self):
        response = self.test_client.get('/projects')
        self.assertTemplateUsed(response, 'projects.html')

