from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.list.models import List
from apps.cards.models import Card
from apps.comments.models import Comment

class Test_Comments(APITestCase):
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
            message="Comment Test",
            list= self.list,
            members=self.user,
            card=self.card
        )

    def test_comment(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertIs(self.comment.message, "Comment Test" )
        self.assertEquals(len(Comment.objects.all()), 1)

class Test_ApiBoard(APITestCase):
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
        action_query = f"{self.url}comments/"
        
        #GET
        response = self.client.get(f"{action_query}")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['message'], self.comment.message)
        
        #POST
        comment_post = self.client.post(
            f"{action_query}",
            {
                "message" : "Test 2",
                "members": self.user.id,
                "card": self.user.id,
                "position": 1,
                "list": self.list.id
            }
        )
        self.assertEquals(comment_post.status_code, 201)
        self.assertEqual(comment_post.data['message'], "Test 2")

        #DELETE
        comment_delete = self.client.delete(f"{action_query}{self.comment.id}")
        self.assertEquals(comment_delete.status_code, 301)
        self.assertEqual(response.data['count'], 1)

    def test_instance(self):
        #Instance
        instance_query = f"{self.url}comments/1/"

        #GET
        instance = self.client.get(f"{instance_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['message'], self.comment.message)

        #PATCH
        comment_patch = self.client.patch(
            f"{instance_query}",
            { "message": "PATCH TEST" }
        )
        self.assertEquals(comment_patch.status_code, 200)
        self.assertEquals(comment_patch.data['message'], "PATCH TEST")

        #DELETE
        board_delete = self.client.delete(f"{instance_query}")
        self.assertEquals(board_delete.status_code, 204)
        boards_get = self.client.get(f"{self.url}comments/")
        self.assertEquals(boards_get.data['count'], 0)

    def test_action(self):
        #Action
        action_query = f"{self.url}comments/1/comentariodeusuario/"

        #GET
        user_get = self.client.get(f"{action_query}")
        self.assertEquals(user_get.status_code, 200)
        self.assertEqual(user_get.data['name'], self.user.name)