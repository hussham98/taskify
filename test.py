
import unittest
from app import app, tasks

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Todo List', response.data)

    def test_edit_task(self):
        response = self.app.post('/edit/0', data={'task': 'New Task', 'due_date': '2024-05-15'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks[0]['task'], 'New Task')
        self.assertEqual(tasks[0]['due_date'], '2024-05-15')

    def test_complete_task(self):
        response = self.app.get('/complete/0')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(tasks[0]['completed'])

if __name__ == '__main__':
    unittest.main()
