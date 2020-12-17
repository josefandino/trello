from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.cards.models import Card
from apps.list.models import List
from apps.comments.models import Comment

class Test_User(APITestCase):
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
        self.assertIsInstance(self.user, User)
        self.assertIs(self.user.name, "User Test")
        self.assertEquals(len(User.objects.all()), 1)

class Test_ApiUser(APITestCase):
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
        default_query = f"{self.url}users/"

        #GET
        response = self.client.get(f"{default_query}")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 3)
        self.assertEqual(response.data['results'][0]['name'], self.user.name)

        #POST
        user_post = self.client.post(
            f"{default_query}",
            {
                "name":"User Test",
                "last_name":"Test",
                "email": "test@gmail.com",
                "password": "1234"
            }
        )
        self.assertEquals(user_post.status_code, 201)
        self.assertEqual(user_post.data['id'], 4)

    def test_instance(self):
        #Instance
        instance_query = f"{self.url}users/1/"
        
        #GET
        instance = self.client.get(f"{instance_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.user.name)

        #PATCH
        user_patch = self.client.patch(
            f"{instance_query}",
            { "name": "PATCH TEST" }
        )
        self.assertEquals(user_patch.status_code, 200)
        self.assertEquals(user_patch.data['name'], "PATCH TEST")

        #DELETE
        user_delete = self.client.delete(f"{instance_query}")
        self.assertEquals(user_delete.status_code, 204)
        users_get = self.client.get(f"{self.url}users/")
        self.assertEquals(users_get.data['count'], 2)

    def test_action_board(self):
        #Action
        action_query = f"{self.url}users/1/boards/"

        #GET
        boards_get = self.client.get(f"{action_query}")
        self.assertEquals(boards_get.status_code, 200)
        self.assertEqual(boards_get.data[0]['name'], self.board.name )