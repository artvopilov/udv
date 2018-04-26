from django.test import TestCase
from .models import Article


class ArticleModelTests(TestCase):

    def test_child_creation(self):
        a = Article()
        a.save()
        self.assertEqual(len(a.children.all()), 0)
        self.assertEqual(a.parent, None)
        for i in range(1, 10):
            a_child = Article(parent=a)
            a_child.save()
            self.assertEqual(len(a.children.all()), i)
            self.assertIs(a_child.parent, a)
            self.assertEqual(len(a_child.children.all()), 0)
        self.assertEqual(a.parent, None)
        for i in range(1, 10):
            a_child_child = Article(parent=a_child)
            a_child_child.save()
            self.assertEqual(len(a_child.children.all()), i)
            self.assertIs(a_child_child.parent, a_child)
            self.assertEqual(len(a_child_child.children.all()), 0)

    def test_child_deletion(self):
        a = Article()
        a.save()
        child_count = 10
        for i in range(child_count):
            a_child = Article(parent=a)
            a_child.save()

        for child in a.children.all():
            child.delete()
            child_count -= 1
            self.assertEqual(len(a.children.all()), child_count)
