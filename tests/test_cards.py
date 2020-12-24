from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.cards.models import Card
from apps.list.models import List


class Test_Card(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="User Test",
            last_name="Lastname",
            email="user@test.com",
            password="1234"
        )
        self.board = Board.objects.create(
            name="Board Test",
            description="Description..."
        )
        self.board.members.add(self.user)
        self.list = List.objects.create(
            name="List Test",
            board=self.board,
            position=1
        )
        self.card = Card.objects.create(
            name="Card Test",
            list=self.list,
            position=1
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
                "name": "Alberto",
                "last_name": "Hernandez",
                "email": "Albert@test.com",
                "password": "1234"
            },
            {
                "name": "Pedro",
                "last_name": "Pelaez",
                "email": "pepe@test.com",
                "password": "1234"
            },
            {
                "name": "Carmen",
                "last_name": "Perez",
                "email": "carmen@test.com",
                "password": "1234"
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
        for i in [1, 1, 1]:
            Board.objects.create(
                name="Boards Test",
                description="Description Test..."
            ).members.add(self.user)
        self.url = "http://127.0.0.1:8000/"
        self.list = List.objects.create(
            name="List Test",
            board=self.board,
            position=1
        )
        self.card = Card.objects.create(
            name="Card Test",
            list=self.list,
            position=1
        )
        self.card.members.add(self.user)

    def test_Default(self):
        # Default
        response = self.client.get(f"{self.url}cards/")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], self.card.name)

    def test_instance(self):
        # Instance
        action_query = f"{self.url}cards/1/"

        # GET
        instance = self.client.get(f"{action_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.card.name)

    # FALTA ARREGLAR VIEW ACTION
    # FALTAN LOS FILTROS

    # def test_action_list(self):
    # Action
    # action_query = f"{self.url}cards/1/userincard/"

    # list_get = self.client.get(f"{action_query}")
    # self.assertEquals(list_get.status_code, 200)
    # self.assertEqual(list_get.data[0]['name'], self.list.name)

    def test_action_user(self):
        # Action
        action_query = f"{self.url}cards/1/userincard/"

        # GET
        user_get = self.client.get(f"{action_query}")
        self.assertEquals(user_get.status_code, 200)
        self.assertEqual(user_get.data[0]['name'], self.user.name)

        # POST
        user_post = self.client.post(
            f"{action_query}",
            {"users_id": [2, 3]}
        )
        self.assertEquals(user_post.status_code, 200)
        self.assertEquals(len(self.card.members.all()), 2)

        # DELETE
        user_delete = self.client.delete(
            f"{action_query}",
            {"users_id": [2, 3]}
        )
        self.assertEquals(user_delete.status_code, 200)
        self.assertEquals(len(self.card.members.all()), 1)
