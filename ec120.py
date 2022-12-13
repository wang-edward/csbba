from util import * 
# 20% - minor assessments
# 20% - review quizzes
# 25% - midterm
# 35% - final

final_weight = 35
overall_goal = 60

minor = [
    4,
    2.24,
    1.78,
    0.44,
    2.17]

review = [
    4,
    4.33,
    4.17,
    4.33]

mt = 80.91

curr = sum(minor) + sum(review) + mt * 0.25

if __name__ == "__main__":
    final(curr, final_weight, overall_goal)