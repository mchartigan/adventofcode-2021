'''
--- Part Two ---

Now that you're warmed up, it's time to play the real game.

A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.

Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.

Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?
'''

sides = [1, 2, 3]
outcomes = {3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
mut = 0
for d1 in sides:
    for d2 in sides:
        for d3 in sides:
            outcomes[d1+d2+d3] += 1
            mut += 1


class Die:
    def __init__(self, det=True):
        self.last = 0
        self.det = det
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        if self.det:
            self.last += 1
            return self.last
        else:
            return 0

class Player:
    def __init__(self, num, start):
        self.num = num
        self.pos = start
        self.score = 0

    def move(self, x):
        temp = self.pos
        self.pos = (temp + x) % 10 if (temp + x) % 10 != 0 else 10
        self.score += self.pos
        return self.score


def quantum(s1, p1, s2, p2):
    if s1 > 19:
        return mut, 0

    v1 = 0
    v2 = 0
    for o1 in outcomes.keys():   # all possible ending positions
        n1 = (p1 + o1) % 10 if (p1 + o1) % 10 != 0 else 10
        if s1+n1 > 20:
            v1 += outcomes[o1]   # number of paths causing match to end here * wins
        else:
            for o2 in outcomes.keys():
                n2 = (p2 + o2) % 10 if (p2 + o2) % 10 != 0 else 10
                if s2+n2 > 20:
                    v2 += outcomes[o1]*outcomes[o2] # number of paths causing match to end here * wins
                else:
                    t1, t2 = quantum(s1+n1, n1, s2+n2, n2)
                    v1 += outcomes[o1]*outcomes[o2]*t1
                    v2 += outcomes[o1]*outcomes[o2]*t2

    return v1, v2


with open("input.txt") as file:
    data = [[int(y) for y in x.strip().replace('Player ','').replace('starting position: ','').split(' ')] for x in file.readlines()]
    
players = []
for player, pos in data:
    players.append(Player(player, pos))



v1, v2 = quantum(0, players[0].pos, 0, players[1].pos)
print(max([v1,v2]))
pass