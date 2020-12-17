from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.cards.models import Card
from apps.list.models import List
from apps.comments.models import Comment

class Test_List(APITestCase):
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

    def test_list(self):
        self.assertIsInstance(self.list, List)
        self.assertIs(self.list.name, "List Test")
        self.assertEquals(len(List.objects.all()), 1)
        self.assertEqual(self.list.board, self.board)

class Test_ApiList(APITestCase):
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
        default_query = f"{self.url}list/"

        #GET
        response = self.client.get(f"{default_query}")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], self.list.name)

        #POST
        comment_post = self.client.post(
            f"{default_query}",
            {
                "name":"List Test",
                "position":1,
                "board": self.board.id
            }
        )
        self.assertEquals(comment_post.status_code, 201)
        self.assertEqual(comment_post.data['name'], "List Test")

    def test_instance(self):
        #Instance
        instance_query = f"{self.url}list/1/"
        
        #GET
        instance = self.client.get(f"{instance_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.list.name)

        #PATCH
        comment_patch = self.client.patch(
            f"{instance_query}",
            { "name": "PATCH TEST" }
        )
        self.assertEquals(comment_patch.status_code, 200)
        self.assertEquals(comment_patch.data['name'], "PATCH TEST")

        #DELETE
        card_delete = self.client.delete(f"{instance_query}")
        self.assertEquals(card_delete.status_code, 204)
        cards_get = self.client.get(f"{self.url}list/")
        self.assertEquals(cards_get.data['count'], 0)

    def test_action_card(self):
        #Action
        action_query = f"{self.url}list/1/card/"

        #GET
        card_get = self.client.get(f"{action_query}")
        self.assertEquals(card_get.status_code, 200)
        self.assertEqual(card_get.data[0]['name'], self.card.name )

        #DELETE
        card_delete = self.client.delete(
            f"{action_query}",
            {"card_id":[1]}
        )
        self.assertEquals(card_delete.status_code, 200)
        # self.assertEquals(len(self.card.members.all()), 1)