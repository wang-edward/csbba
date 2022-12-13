
def final(current, weight, goal):
    print("=============================================")
    print("FINAL EXAM PREDICTIONS:")
    print("=============================================")
    for i in range(11):
        final = i * 10
        weighted = i * weight / 10
        print("{0}%:\t\t{1}%".format(final, current + weighted))
    req = (goal - current) / weight * 100
    print("=============================================") 
    print("you need {0} on the final to get {1}% overall".format(str(round(req, 2)), goal))
    print("=============================================")

def drop_n (las, n):
    las.sort()
    y = len(las)-1
    return las[n:y]


# final(50, 50, 60)