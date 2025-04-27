from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from core.models import CourseModel, LevelModel


class CourseAPITestCase(TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = None
        self.course = None
        self.create_url = None
        self.detail_url = None
        self.course_data = None
        self.level = None
    def setUp(self):
        self.client = APIClient()
        
        
        self.level =LevelModel.objects.create(name='Beginner', description='Beginner Level', order=1)
        self.course_data = {
            'name': 'Python 101',
            'level_id': self.level.id,  # Assuming level with ID 1 exists
            'description': 'Introduction to Python'
        }
        self.course = CourseModel.objects.create(**self.course_data)
        self.create_url = '/courses/'
        self.detail_url = f'/courses/{self.course.id}/'

    def test_create_course(self):
        response = self.client.post(self.create_url, {
            'name': 'Django REST',
            'description': 'Introduction to Django REST Framework',
            'level_id': self.level.id
        }, format='json')
        print('response', response.data)
        print('response', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Django REST')

    def test_list_courses(self):
        response = self.client.get(self.create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_course(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.course.name)

    def test_update_course(self):
        update_data = {'title': 'Updated Python 101',
                       'description': 'Updated', 'price': 39.99}
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Python 101')

    def test_delete_course(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CourseModel.objects.filter(id=self.course.id).exists())
