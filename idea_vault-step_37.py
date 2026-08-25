# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: IdeaVault
import unittest


class TestIdea(unittest.TestCase):
    def test_idea_creation(self):
        idea = Idea("Build MVP", "2024-01-01", "2024-06-01")
        self.assertEqual(idea.title, "Build MVP")
        self.assertEqual(idea.start_date, "2024-01-01")
        self.assertEqual(idea.end_date, "2024-06-01")


class TestIdeaVault(unittest.TestCase):
    def test_add_and_get_idea(self):
        vault = IdeaVault()
        idea = Idea("Test Idea", "2024-01-01", "2024-12-31")
        vault.add_idea(idea)
        self.assertEqual(len(vault.ideas), 1)
        self.assertIs(vault.get_idea(idea.id), idea)


class TestIdeaStatus(unittest.TestCase):
    def test_status_values(self):
        self.assertEqual(IdeaStatus.NOT_STARTED, "Not Started")
        self.assertEqual(IdeaStatus.IN_PROGRESS, "In Progress")
        self.assertEqual(IdeaStatus.COMPLETED, "Completed")


class TestCategory(unittest.TestCase):
    def test_category_creation(self):
        cat = Category("Tech", "Technology")
        self.assertEqual(cat.name, "Tech")
        self.assertEqual(cat.description, "Technology")


class TestPriority(unittest.TestCase):
    def test_priority_values(self):
        self.assertEqual(Priority.LOW, 1)
        self.assertEqual(Priority.MEDIUM, 2)
        self.assertEqual(Priority.HIGH, 3)


class TestIdeaConnection(unittest.TestCase):
    def test_connection_creation(self):
        conn = IdeaConnection(Idea(0), Idea(1), "depends_on")
        self.assertEqual(conn.type, "depends_on")
        self.assertEqual(conn.target_idea.id, 1)
