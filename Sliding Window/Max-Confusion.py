# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/


def max_confusion(answerKey, k):
    t_count = f_count = 0
    i = 0
    while min(t_count, f_count) <= k and i < len(answerKey):
        if answerKey[i] == "T":
            t_count += 1
        else:
            f_count += 1
        i += 1
        print(f"t: {t_count} and f: {f_count}")
    return i


print(max_confusion("TTFF", 2))
# 4
print(max_confusion("TFFT", 1))
# 3
