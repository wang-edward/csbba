from util import * 
# 20% - minor assessments
# 20% - review quizzes
# 25% - midterm
# 35% - final

final_weight = 35
overall_goal = 60

minor = [
    4,
    4,
    4,
    0,
    1.2345] # out of 4 like on myLS

review = [
    4,
    4,
    5,
    1.231] # out of 5 like on myLS

mt = 80.91

curr = sum(minor) + sum(review) + mt * 0.25

if __name__ == "__main__":
    final(curr, final_weight, overall_goal)