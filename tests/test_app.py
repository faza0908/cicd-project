"""
Unit Tests for Counter Service
"""
import unittest
from app import app, COUNTERS


class TestCounterService(unittest.TestCase):
    """Test cases for the Counter Service"""

    def setUp(self):
        """Set up test fixtures"""
        self.app = app.test_client()
        self.app.testing = True
        COUNTERS.clear()

    def tearDown(self):
        """Tear down test fixtures"""
        COUNTERS.clear()

    # ----------------------------------------------------------
    # Health Check Tests
    # ----------------------------------------------------------
    def test_health_endpoint(self):
        """It should return health status OK"""
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "OK")

    def test_index_endpoint(self):
        """It should return SERVICE RUNNING"""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("SERVICE RUNNING", data["status"])

    # ----------------------------------------------------------
    # Counter CRUD Tests
    # ----------------------------------------------------------
    def test_create_counter(self):
        """It should create a counter successfully"""
        response = self.app.post("/counters/foo")
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["foo"], 0)

    def test_create_duplicate_counter(self):
        """It should return 409 for duplicate counter"""
        self.app.post("/counters/foo")
        response = self.app.post("/counters/foo")
        self.assertEqual(response.status_code, 409)

    def test_read_counter(self):
        """It should read a counter"""
        self.app.post("/counters/bar")
        response = self.app.get("/counters/bar")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["bar"], 0)

    def test_read_missing_counter(self):
        """It should return 404 for missing counter"""
        response = self.app.get("/counters/missing")
        self.assertEqual(response.status_code, 404)

    def test_update_counter(self):
        """It should increment a counter"""
        self.app.post("/counters/baz")
        response = self.app.put("/counters/baz")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["baz"], 1)

    def test_update_missing_counter(self):
        """It should return 404 when updating missing counter"""
        response = self.app.put("/counters/missing")
        self.assertEqual(response.status_code, 404)

    def test_delete_counter(self):
        """It should delete a counter"""
        self.app.post("/counters/del")
        response = self.app.delete("/counters/del")
        self.assertEqual(response.status_code, 204)

    def test_delete_missing_counter(self):
        """It should return 404 when deleting missing counter"""
        response = self.app.delete("/counters/missing")
        self.assertEqual(response.status_code, 404)

    def test_list_counters(self):
        """It should list all counters"""
        self.app.post("/counters/a")
        self.app.post("/counters/b")
        response = self.app.get("/counters")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("a", data)
        self.assertIn("b", data)


if __name__ == "__main__":
    unittest.main()
