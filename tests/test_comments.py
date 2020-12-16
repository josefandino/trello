from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board
from apps.list.models import List
from apps.cards.models import Card
from apps.comments.models import Comment

class Test_Comments(APITestCase):
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

    def test_board(self):
        self.assertIsInstance(self.board, Board)
        self.assertIs(self.board.name, "Board Test" )
        self.assertEquals(len(Board.objects.all()), 1)
        self.assertEqual(self.board.members.all().first(), self.user)
    

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

    def test_Default(self):
        #Default
        response = self.client.get(f"{self.url}boards/")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 4)
        self.assertEqual(response.data['results'][0]['name'], self.board.name)

    def test_instance(self):
        #Instance
        instance = self.client.get(f"{self.url}boards/1/")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.board.name)

    def test_action(self):
        #GET
        user_get = self.client.get(f"{self.url}boards/1/user/")
        self.assertEquals(user_get.status_code, 200)
        self.assertEqual(user_get.data[0]['name'], self.user.name)
        
        #POST
        user_post = self.client.post(
            f"{self.url}boards/1/user/",
            {"users_id":[2,3]}
        )
        self.assertEquals(user_post.status_code, 200)
        
        #DELETE
        user_delete = self.client.delete(
            f"{self.url}boards/1/user/",
            {"users_id":[2,3]}
        )
        self.assertEquals(user_delete.status_code, 200)