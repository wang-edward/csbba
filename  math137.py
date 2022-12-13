from util import * 
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
final_weight = 50
pass_req = 60
quiz_drops = 2
quiz = [
    63,
    7,
    46,
    81,
    61,
    68,
    77]

academic_integrity = 0
latex_quiz = 0
latex_assign = 0
mt = 47/58 * 100

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

x = drop_n(quiz, quiz_drops)
quiz = sum(x) / (len(x))

curr = academic_integrity * 0.01 + latex_quiz * 0.01 + latex_assign * 0.01 + quiz * 0.19 + mt * 0.3

if __name__ == "__main__":
    final(curr, final_weight, pass_req)