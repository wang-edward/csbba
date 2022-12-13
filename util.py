
def final(current, weight, goal):
    print("=============================================")
    print("FINAL\t|||\tOVERALL:")
    print("=============================================")
    for i in range(11):
        final = i * 10
        weighted = i * weight / 10
        print("{0}%:\t|||\t{1}%".format(final, str(round(current + weighted, 2))))
    req = (goal - current) / weight * 100
    print("=============================================") 
    print("you need {0}% on the final to get {1}% overall".format(str(round(req, 2)), goal))
    print("=============================================")

def drop_n (las, n):
    las.sort()
    y = len(las)-1
    return las[n:y]

if __name__ == "__main__":
    print("""============================================= 
    this is util file, update your marks in the files then run
    \tpython3 <course_code>.py
    example: Math 135 - Algebra
    \tpython3 ma135.py
=============================================""")

# final(50, 50, 60)