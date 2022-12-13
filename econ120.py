# 20% - minor assessments
# 20% - review quizzes
# 25% - midterm
# 35% - final

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

mt = 80.91 * 0.25

curr = sum(minor) + sum(review) + mt

for i in range(11):
    x = i * 10 
    weighted = x* 0.35
    print("{0}%: {1}".format(x, curr + weighted))
