from django.test import TestCase
from .models import Article, UdvUser, BlockOfText, Source, AlternativeOpinion, Paragraph


from .views.articles import Validator
import json, datetime


class ArticleModelTests(TestCase):

    def test_child_creation(self):
        a = Article()
        a.save()
        self.assertEqual(len(a.children.all()), 0)
        self.assertEqual(a.parent, None)
        for i in range(1, 10):
            a_child = Article(parent=a,title=str(i))
            a_child.save()
            self.assertEqual(len(a.children.all()), i)
            self.assertIs(a_child.parent, a)
            self.assertEqual(len(a_child.children.all()), 0)
        self.assertEqual(a.parent, None)
        for i in range(1, 10):
            a_child_child = Article(parent=a_child, title=a_child.title+str(i))
            a_child_child.save()
            self.assertEqual(len(a_child.children.all()), i)
            self.assertIs(a_child_child.parent, a_child)
            self.assertEqual(len(a_child_child.children.all()), 0)

    def test_child_deletion(self):
        a = Article()
        a.save()
        child_count = 10
        for i in range(child_count):
            a_child = Article(parent=a, title=str(i))
            a_child.save()

        for child in a.children.all():
            child.delete()
            child_count -= 1
            self.assertEqual(len(a.children.all()), child_count)


class ValidationTest(TestCase):
    def test_check_structure(self):
        s = {'hello': 1, 'a': {}, 'z': []}
        self.assertTrue(Validator.check_structure(s, {'hello': int, 'a': dict, 'z': list}))
        self.assertFalse(Validator.check_structure(s, {'hello': int, 'a': dict, 'z': str}))

    def test_article_validation(self):
        data = {
            "parent_id" : 0, "title" : "",
            "paragraphs" : [
            {
               "subtitle" : "",
               "blocks" : [
                   {
                       "text" : "x",
                       "source" : {
                           "author": "",
                           "url": "",
                        }
                    },
               ]
            }
            ]
        }
        self.assertTrue(Validator.article(data))
        data['paragraphs'][0]['blocks'][0]['source']['author'] = 1
        self.assertFalse(Validator.article(data))
        del data['paragraphs'][0]['blocks'][0]['source']['author']
        self.assertFalse(Validator.article(data))


class ProposeArticleTest(TestCase):

    def test_insert(self):
        user = UdvUser.objects.create(email='dummy@dummy.dummy')
        user.set_password('dummy')
        user.save()

        logged = self.client.login(username='dummy@dummy.dummy', password='dummy')
        self.assertTrue(logged)

        parent = Article.objects.create()

        data = {
            "parent_id": parent.id, "title": "dummytitle",
            "paragraphs": [
                {
                    "subtitle": "dummysubtitle",
                    "blocks": [
                        {
                            "text": "dummytext",
                            "source": {
                                "author": "dummyauthor",
                                "url": "dummyurl",
                            }
                        },
                        {
                            "text": "dummytext2",
                            "source": {
                                "author": "dummyauthor2",
                                "url": "dummyurl2",
                            }
                        },
                    ]
                },
                {
                    "subtitle": "dummysubtitle2",
                    "blocks": [
                        {
                            "text": "dummytext3",
                            "source": {
                                "author": "dummyauthor3",
                                "url": "dummyurl3",
                            }
                        },
                        {
                            "text": "dummytext4",
                            "source": {
                                "author": "dummyauthor4",
                                "url": "dummyurl4",
                            }
                        },
                    ]
                }
            ]
        }

        resp = self.client.post('/api/articles/insert/', json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        try:
            int(resp.content)
        except ValueError as err:
            self.fail(str(err) + " is not int")

        try:
            article = Article.objects.get(id = int(resp.content))
        except Article.DoesNotExist:
            self.fail("article is not created")

        self.assertEqual(article.parent, parent)
        self.assertEqual(article.title, data['title'])
        for paragraph_posted, paragraph in zip(data['paragraphs'], article.paragraphs.all()):
            self.assertEqual(paragraph_posted['subtitle'], paragraph.subtitle)
            for block_posted, block in zip(paragraph_posted['blocks'], map(lambda op: op.blocks.first(),paragraph.opinions.all())):
                self.assertEqual(block_posted['text'], block.text)

    def test_invalid_data(self):
        user = UdvUser.objects.create(email='dummy@dummy.dummy')
        user.set_password('dummy')
        user.save()

        logged = self.client.login(username='dummy@dummy.dummy', password='dummy')
        self.assertTrue(logged)
        resp = self.client.post('/api/articles/insert/', '{}', content_type='application/json')
        self.assertNotEqual(resp.status_code,200)


class ProposeChangesTest(TestCase):
    def test_propose_change(self):
        user = UdvUser.objects.create(email='dummy@dummy.dummy')
        user.set_password('dummy')
        user.save()
        self.client.login(username='dummy@dummy.dummy', password='dummy')

        a = Article.objects.create()
        p = Paragraph.objects.create(number=9, article=a)
        o = AlternativeOpinion.objects.create(paragraph=p)
        s = Source.objects.create(author='dummyauthor', link='dummyurl', char_number=0,
                                  date_upload=datetime.datetime.now())
        b = BlockOfText.objects.create(text='dummytext', number=99, source=s, alternative_opinion=o)
        data = {'block_id': b.id, 'new_version':{
                "text": "smarttext",
                "source": {
                    "author": "smartauthor",
                    "url": "smarturl"
                }
        }}
        count = BlockOfText.objects.filter(number=b.number).count()
        resp = self.client.patch('/api/articles/change/', json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(BlockOfText.objects.filter(number=b.number).count(), count + 1)
