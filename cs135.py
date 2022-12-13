from util import * 
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
final_weight = 30
overall_goal = 60

assignments = [
100,
92.65,
97.5,
79.60,
96.55,
65.90,
77,
70.13,
72.90] # one assignment got exempted

mt1 = 87
mt2 = 73
iclick = 58.2 * 4/3 # top 75% (might be wrong)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

asgn_mark = (sum(assignments)/len(assignments)) 


# no_iclick = asgn_mark * 0.45 + mt1 * 0.07 + mt2 * 0.13 
curr = asgn_mark * 0.45 + mt1 * 0.07 + mt2 * 0.13 + iclick * 0.05

if __name__ == "__main__":
    final(curr, final_weight, overall_goal)