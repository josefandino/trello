from rest_framework.test import APITestCase
from apps.users.models import User
from apps.boards.models import Board

class Test_board(APITestCase):
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
        self.user = User.objects.get(id=1)
        self.board = Board.objects.create(
            name="Tablero",
            description="Description..."
        )
        self.board.members.add(self.user)
        self.url = "http://127.0.0.1:8000/"

    def test_Default(self):
        #Default
        action_query = f"{self.url}boards/"
        
        #GET
        response = self.client.get(f"{action_query}")
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], self.board.name)
        
        #POST
        board_post = self.client.post(
            f"{action_query}",
            {
                "name" : "Test 2",
                "description": "Description...",
                "members": [self.user.id]
            }
        )
        self.assertEquals(board_post.status_code, 201)
        self.assertEqual(board_post.data['name'], "Test 2")

        #DELETE
        board_delete = self.client.delete(f"{action_query}{self.board.id}")
        self.assertEquals(board_delete.status_code, 301)
        self.assertEqual(response.data['count'], 1)

    def test_instance(self):
        #Instance
        instance_query = f"{self.url}boards/1/"

        #GET
        instance = self.client.get(f"{instance_query}")
        self.assertEquals(instance.status_code, 200)
        self.assertEquals(instance.data['name'], self.board.name)

        #PATCH
        board_patch = self.client.patch(
            f"{instance_query}",
            { "name": "PATCH TEST" }
        )
        self.assertEquals(board_patch.status_code, 200)
        self.assertEquals(board_patch.data['name'], "PATCH TEST")

        #DELETE
        board_delete = self.client.delete(f"{instance_query}")
        self.assertEquals(board_delete.status_code, 204)
        boards_get = self.client.get(f"{self.url}boards/")
        self.assertEquals(boards_get.data['count'], 0)

    def test_action_user(self):
        #GET
        user_get = self.client.get(f"{self.url}boards/1/user/")
        self.assertEquals(user_get.status_code, 200)
        self.assertEqual(user_get.data[0]['name'], self.user.name)
        self.assertEquals(self.board.members.get(id=1), self.user)
        self.assertEquals(self.board.id, 1)
        
        #POST
        user_post = self.client.post(
            f"{self.url}boards/1/user/",
            {"users_id":[2]}
        )
        self.assertEquals(user_post.status_code, 200)
        self.assertEquals(len(self.board.members.all()), 2)

        #DELETE
        user_delete = self.client.delete(
            f"{self.url}boards/1/user/",
            {"users_id":[1]}
        )
        self.assertEquals(user_delete.status_code, 200)
        self.assertEquals(self.board.members.get(id=2).name, "Pedro")

    def test_action_lis(self):
        #Action
        action_query = f"{self.url}boards/1/lis/"

        #GET
        board_get = self.client.get(f"{action_query}")
        self.assertEquals(board_get.status_code, 200)
        self.assertEquals(len(board_get.data), 1)

        #POST (PENDIENTE)
        # board_post = self.client.post(
        #     f"{action_query}",
        #     {""}
        # )