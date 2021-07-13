from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Review, Shop


class TestAPI(APITestCase):
    def setUp(self) -> None:
        pass

    def test_review_CRUD(self):
        url = reverse('api:review-list')
        data_first_review = {
            "rating": 1,
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user": "lana@gmail.com",
            "title": "worst shop",
            "description": "some text"
        }
        data_second_review = {
            "rating": 5,
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user": "gleb@gmail.com",
            "title": "best shop",
            "description": "some text"
        }
        data_third_review = {
            "rating": 5,
            "shop_link": "https://kufar.by/tovary-dlia-sobak/",
            "user": "lana@gmail.com",
            "title": "best shop",
            "description": "some text"
        }
        """Creation of reviews"""
        response = self.client.post(url, data_first_review, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.filter(user='lana@gmail.com').count(), 1)
        self.assertEqual(Shop.objects.count(), 1)
        self.assertEqual(Shop.objects.filter(domain='rozetka.com.ua').values('avg_rate')[0]['avg_rate'], 1)
        response = self.client.post(url, data_second_review, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)
        self.assertEqual(Review.objects.filter(user='lana@gmail.com').count(), 1)
        self.assertEqual(Review.objects.filter(user='gleb@gmail.com').count(), 1)
        self.assertEqual(Shop.objects.filter(domain='rozetka.com.ua').values('avg_rate')[0]['avg_rate'], 3)
        self.assertEqual(Shop.objects.filter(domain='rozetka.com.ua').values('reviews')[0]['reviews'], 2)
        response = self.client.post(url, data_third_review, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 3)
        self.assertEqual(Review.objects.filter(user='lana@gmail.com').count(), 2)
        self.assertEqual(Shop.objects.count(), 2)
        """Update of a review"""
        url_detail = reverse('api:review-detail', kwargs={'pk': Review.objects.get(title=data_first_review['title']).pk})
        data_part_upd = {
            'rating': 5
        }
        response = self.client.patch(url_detail, data_part_upd, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Review.objects.get(title=data_first_review['title']).rating, 5)
        self.assertEqual(Shop.objects.filter(domain='rozetka.com.ua').values('avg_rate')[0]['avg_rate'], 5)
        data_upd = {
            "rating": 1,
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user": "lana@gmail.com",
            "title": "not so worst shop",
            "description": "some text and some text"
        }
        response = self.client.put(url_detail, data_upd, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Review.objects.get(title=data_upd['title']).rating, 1)
        self.assertEqual(Shop.objects.filter(domain='rozetka.com.ua').values('avg_rate')[0]['avg_rate'], 3)
        """Delete of a review"""
        response = self.client.delete(url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(Review.objects.count(), 2)