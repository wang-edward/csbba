from util import * 
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
final_weight = 40 
overall_goal = 60

assignments = [24.5,
27,
19.5,
0,
21.5,
20,
15] # missed some assignments cuz transfer from 145, should have a0 - a9

test1 = 41/45 * 100
test2 = 33/40 * 100

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

asgns = drop_n(assignments, 1)

c_asgn = sum(asgns) / len(asgns) / 30 * 100

curr = c_asgn * 0.2 + test1 * 0.2 + test2 * 0.2  

if __name__ == "__main__":
    final(curr, final_weight, overall_goal)