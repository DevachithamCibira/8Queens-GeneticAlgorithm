import unittest
import Queen_challenge

class TestEightQueens(unittest.TestCase):


    def test_initial_population(self):
        queen = Queen_challenge.EightQueens()
        value = queen.initial_population()
        self.assertAlmostEqual(len(value), 8)


    def test_selected_population(self):
        queen = Queen_challenge.EightQueens()
        value = queen.initial_population()
        score = queen.large_population(value)
        population = queen.selection(score)
        parent1 = population[0]
        parent2 = population[1]
        self.assertIn(parent1,population)
        self.assertIn(parent2,population)



    def test_parents(self):
        queen = Queen_challenge.EightQueens()
        value = queen.initial_population()
        score = queen.large_population(value)
        parent = queen.selection(score)
        parent1 = parent[0]
        parent2  = parent[1]
        offspring1, offspring2 = queen.cross_over(parent1, parent2)
        self.assertAlmostEqual(len(offspring1), len(offspring2))

    def test_result(self):
        queen = Queen_challenge.EightQueens()
        queen.start()
        result = queen.final_result
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()