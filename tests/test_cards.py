from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.cards.models import Card
from apps.list.models import List
from apps.comments.models import Comment

class Test_Card(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="User Test",
            last_name="Lastname",
            email="user@test.com",
            password= "1234"
        )
        self.board = Board.objects.create(
            name="Board Test",
            description="Description..."
        )
        self.board.members.add(self.user)
        self.list = List.objects.create(
            name = "List Test",
            board = self.board,
            position = 1
        )
        self.card = Card.objects.create(
            name = "Card Test",
            list = self.list,
            position = 1
        )

    def test_card(self):
        self.assertIsInstance(self.card, Card)
        self.assertIs(self.card.name, "Card Test")
        self.assertEquals(len(Card.objects.all()), 1)
        self.assertEqual(self.card.list, self.list)

class Test_ApiCard(APITestCase):
    def setUp(self):
        users = [
            {
                "name":"Alberto",
                "last_name":"Hernandez",
                "email":"Albert@test.com",
                "password":"1234"
            },
            {
                "name":"Pedro",
                "last_name":"Pelaez",
                "email":"pepe@test.com",
                "password":"1234"
            },
            {
                "name":"Carmen",
                "last_name":"Perez",
                "email":"carmen@test.com",
                "password":"1234"
            }
        ]
        for user in users:
            User.objects.create(
                name=user['name'],
                last_name=user['last_name'],
                email=user['email'],
                password=user['password']
            )
        self.user = User.objects.all().first()
        self.board = Board.objects.create(
            name="Tablero",
            description="Description..."
        )
        self.board.members.add(self.user)
        for i in [1,1,1]:
            Board.objects.create(
                name="Boards Test",
                description="Description Test..."
            ).members.add(self.user)
        self.url = "http://127.0.0.1:8000/"
        self.list = List.objects.create(
            name = "List Test",
            board = self.board,
            position = 1
        )
        self.card = Card.objects.create(
            name = "Card Test",
            list = self.list,
            position = 1
        )
        self.card.members.add(self.user)
        self.comment = Comment.objects.create(
            message="Comentario Test",
            list= self.list,
            members=self.user,
            card=self.card
        )

    def test_Default(self):
        #Default
        action_query = f"{self.url}cards/"

        #GET
        response = self.client.get(f"{action_query}")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], self.card.name)

        #POST
        card_post = self.client.post(
            f"{action_query}",
            {
                "name":"Card Test",
                "description":" Description...",
                "list":self.list.id,
                "members": [self.user.id],
                "position": 1
            }
        )
        self.assertEquals(card_post.status_code, 201)
        self.assertEqual(card_post.data['name'], "Card Test")

        #DELETE
        card_delete = self.client.delete(f"{action_query}{self.card.id}")
        self.assertEquals(card_delete.status_code, 301)
        self.assertEqual(response.data['count'], 1)

    def test_instance(self):
        #Instance
        action_query = f"{self.url}cards/1/"
        
        #GET
        instance = self.client.get(f"{action_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.card.name)

    def test_action_comment(self):
        #Action
        action_query = f"{self.url}cards/1/commentincard/"

        #GET
        comment_get = self.client.get(f"{action_query}")
        self.assertEquals(comment_get.status_code, 200)
        self.assertEquals(len(comment_get.data), 1)

        #POST
        comment_post = self.client.post(
            f"{action_query}",
            {"comments_id": [self.comment.id]}
        )
        self.assertEquals(comment_post.status_code,200)
        comments_get = self.client.get(f"{action_query}")
        self.assertEquals(len(comments_get.data), 1)

        #DELETE
        # PENDIENTE POR ERROR: 
        # File "E:\DOCS\Python\Proyectos\trello\apps\cards\views.py",
        # line 71, in comment card.comments.remove(comment)
        # AttributeError: 'RelatedManager' object has no attribute 'remove'

        # comments_delete = self.client.delete(
        #     f"{action_query}",
        #     {"comments_id": [self.comment.id]}
        # )
        # self.assertEquals(comments_delete.status_code, 200)

    def test_action_user(self):
        #Action
        action_query = f"{self.url}cards/1/userincard/"

        #GET
        user_get = self.client.get(f"{action_query}")
        self.assertEquals(user_get.status_code, 200)
        self.assertEqual(user_get.data[0]['name'], self.user.name )

        #POST
        user_post = self.client.post(
            f"{action_query}",
            {"users_id": [2,3]}
        )
        self.assertEquals(user_post.status_code, 200)
        self.assertEquals(len(self.card.members.all()), 2)

        #DELETE
        user_delete = self.client.delete(
            f"{action_query}",
            {"users_id":[2,3]}
        )
        self.assertEquals(user_delete.status_code, 200)
        self.assertEquals(len(self.card.members.all()), 1)