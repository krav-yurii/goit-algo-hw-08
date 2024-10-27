import heapq

def min_total_cost_with_steps(cables):
    heapq.heapify(cables)
    total_cost = 0
    steps = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
        steps.append(f"З'єднати кабелі довжиною {first} і {second}, вартість: {cost}")

    return total_cost, steps

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    result, steps = min_total_cost_with_steps(cables)
    for step in steps:
        print(step)
    print(f"Мінімальні загальні витрати на з'єднання кабелів: {result}")
