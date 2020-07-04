import random

class EightQueens():

    def populate(self, CB_list):
        moves_possible, queen_moves, coin_position = [], [], []
        hit_moves = {}
        [[moves_possible.append((row, col)) for col in range(1, 9)] for row in range(1, 9)]
        for i in range(8):
            if CB_list[i] != 0:
                coin_position.append((CB_list[i], i + 1))
        for queen_position in coin_position:
            coin_blocked = []
            for i in range(1, 9):
                queen_moves.append((queen_position[0], i))
                queen_moves.append((i, queen_position[1]))
                coin_blocked.append((queen_position[0], i))
                coin_blocked.append((i, queen_position[1]))
                if queen_position[0] + i < 9 and queen_position[1] + i < 9:
                    queen_moves.append((queen_position[0] + i, queen_position[1] + i))
                    coin_blocked.append((queen_position[0] + i, queen_position[1] + i))
                if queen_position[0] - i > 0 and queen_position[1] - i > 0:
                    queen_moves.append((queen_position[0] - i, queen_position[1] - i))
                    coin_blocked.append((queen_position[0] - i, queen_position[1] - i))
                if queen_position[0] + i < 9 and queen_position[1] - i > 0:
                    queen_moves.append((queen_position[0] + i, queen_position[1] - i))
                    coin_blocked.append((queen_position[0] + i, queen_position[1] - i))
                if queen_position[0] - i > 0 and queen_position[1] + i < 9:
                    queen_moves.append((queen_position[0] - i, queen_position[1] + i))
                    coin_blocked.append((queen_position[0] - i, queen_position[1] + i))
            queen_moves = list(dict.fromkeys(queen_moves))
            hit_moves[queen_position[0] * 10 + queen_position[1]] = coin_blocked
        [moves_possible.remove(move) for move in queen_moves if move in moves_possible]
        attack = self.fitness(coin_position, hit_moves)
        return (attack, CB_list)


    def fitness(self,coins_pos, hit_moves):
        attack = 0
        for n, coin in enumerate(coins_pos):
            if n is not 0:
                for key in hit_moves.keys():
                    if coin[0] * 10 + coin[1] != key and key % 10 < coin[1]:
                        if coin in hit_moves[key]:
                            attack = attack + 1
        return attack


    def initial_population(self):
        population = []
        for _ in range(8):
            n = random.randint(1, 8)
            population.append(n)
        return population


    def large_population(self,value):
        total_population = []
        score = []
        while len(total_population) < 150:
            val = self.initial_population()
            total_population.append(val)
        for people in total_population:
            attack, people = self.populate(people)
            score.append((attack, people))
        return score


    def selection(self,score):
        selected_population = []
        val = sorted(score, key=lambda x:x[0])
        for _, b in val:
            selected_population.append((b))
        return selected_population


    def cross_over(self,parent1, parent2):
        for n, val in enumerate(parent1):
            if len(parent1) != len(list(dict.fromkeys(parent1))):
                for k, pval in enumerate(parent1):
                    if val == pval and n != k:
                        parent1[n] = parent2[n]
        for n, val in enumerate(parent2):
            if len(parent2) != len(list(dict.fromkeys(parent2))):
                for k, pval in enumerate(parent2):
                    if val == pval and n != k:
                        parent2[n] = parent1[n]
        rand_length = random.randrange(8)
        parent1 = parent1[:rand_length] + parent2[rand_length:]
        rand_length = random.randrange(8)
        parent2 = parent2[:rand_length] + parent1[rand_length:]
        return parent1, parent2


    def mutation(self,offspring1, offspring2):
        rand_length = random.randrange(8)
        offspring1_left = offspring1[: rand_length]
        offspring1_right = offspring1[rand_length:]
        mutated_child1 = offspring1_right + offspring1_left
        rand_length = random.randrange(8)
        offspring2_left = offspring2[: rand_length]
        offspring2_right = offspring2[rand_length:]
        mutated_child2 = offspring2_right + offspring2_left
        temp = []
        for child in [mutated_child1, mutated_child2]:
            if len(child) != len(list(dict.fromkeys(child))):
                replacement = []
                [replacement.append(val) for val in range(1, 9) if val not in child]
                for n in range(len(child)):
                    for k in range(len(child)):
                        if n != k and child[n] == child[k]:
                            child[n] = replacement.pop(0)
            temp.append(child)
        return temp[0],temp[1]


    def start(self):
        value = self.initial_population()
        score = self.large_population(value)
        population = self.selection(score)
        parent1 = population[0]
        parent2 = population[1]
        while True:
            offspring1, offspring2 = self.cross_over(parent1, parent2)
            mutated_child1, mutated_child2 = self.mutation(offspring1, offspring2)
            score1, mutated_child1 = self.populate(mutated_child1)
            score2, mutated_child2 = self.populate(mutated_child2)
            parent1, parent2 = mutated_child1, mutated_child2
            result = []
            parent, score = (parent1, score1)  if score1 is 0 else (parent2, score2) if score2 is 0 else ('', 5)
            if score is 0:
                final_result = ''
                for val in parent:
                    val = val - 1
                    result.append(val)
                    final_result = final_result + " " + str(val)
                self.final_list = result
                self.final_result = final_result[1:]
                break


if __name__=="__main__":
    queen = EightQueens()
    queen.start()
    result = queen.final_result
    print(result)
