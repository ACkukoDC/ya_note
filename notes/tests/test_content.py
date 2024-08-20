from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from notes.models import Note

User = get_user_model()


class TestStatic(TestCase):

    @classmethod
    def setUpTestData(cls):  # noqa
        cls.author = User.objects.create(username='Лев Толстой')
        cls.reader = User.objects.create(username='Читатель простой')
        cls.note = Note.objects.create(title='Заголовок', text='Текст', slug='Dima', author=cls.author)


class TestlistPage(TestStatic):
    LIST_URL = reverse('notes:list')

    def test_new_note_on_list_for_author_and_not_for_reader(self):
        user = (self.author, self.reader)
        for name in user:
            with self.subTest(name=name):
                self.client.force_login(name)
                response = self.client.get(self.LIST_URL)
                object_list = response.context['object_list']
                if name == self.author:
                    self.assertIn(self.note, object_list)
                else:
                    self.assertNotIn(self.note, object_list)


class TestNoteData(TestStatic):

    def test_create_note_page_contains_form(self):
        urls = (
            ('notes:add', None),
            ('notes:edit', (self.note.slug,)),
        )
        self.client.force_login(self.author)
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertIn('form', response.context)
