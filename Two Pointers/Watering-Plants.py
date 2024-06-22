# https://leetcode.com/problems/watering-plants-ii/description/
def minimum_refill(plants, capacityA, capacityB):
    i = count = 0
    j = len(plants) - 1
    tempA, tempB = capacityA, capacityB

    while i < j:
        if tempA < plants[i]:
            tempA = capacityA
            count += 1
            print(f"count + 1 {i} : {j}")
        tempA -= plants[i]
        i += 1

        if tempB < plants[j]:
            tempB = capacityB
            count += 1
            print(f"count + 1 {i} : {j}")
        tempB -= plants[j]
        j -= 1

    if i == j and max(tempA, tempB) < plants[i]:
        count += 1
        print(f"count + 1 {i} : {j}")

    return count
