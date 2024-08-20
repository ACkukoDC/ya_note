# # news/tests/test_trial.py
# from unittest import skip
#
# from django.contrib.auth import get_user_model
# from django.test import Client, TestCase
# from notes.models import Note
#
# User = get_user_model()
#
#
# @skip(reason='не надо')
# class TestNews(TestCase):
#     # Все нужные переменные сохраняем в атрибуты класса.
#     TITLE = 'Заголовок новости'
#     TEXT = 'Тестовый текст'
#
#     @classmethod
#     def setUpTestData(cls):  # noqa
#         cls.user = User.objects.create(username='testUser')
#         # Создаём объект клиента.
#         cls.user_client = Client()
#         # "Логинимся" в клиенте при помощи метода force_login().
#         cls.user_client.force_login(cls.user)
#         cls.news = Note.objects.create(
#             # При создании объекта обращаемся к константам класса через cls.
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )
#
#     def test_successful_creation(self):
#         news_count = Note.objects.count()
#         self.assertEqual(news_count, 1)
#
#     def test_title(self):
#         # Чтобы проверить равенство с константой -
#         # обращаемся к ней через self, а не через cls:
#         self.assertEqual(self.news.title, self.TITLE)
