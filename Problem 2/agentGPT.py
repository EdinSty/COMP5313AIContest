def fair_split_haybales(N, haybales, Q, queries):
    prefix_sum = [0]
    for i in range(N):
        prefix_sum.append(prefix_sum[-1] + haybales[i])

    result = []
    for query in queries:
        l, r, x = query
        total_hay_units = prefix_sum[r] - prefix_sum[l-1]
        starting_difference = x
        remaining_hay_units = total_hay_units + starting_difference

        bessie_hay_units = remaining_hay_units // 2
        elsie_hay_units = remaining_hay_units - bessie_hay_units

        difference = bessie_hay_units - elsie_hay_units
        result.append(difference)

    return result


# Read input
N = int(input())
haybales = list(map(int, input().split()))
Q = int(input())

queries = []
for _ in range(Q):
    l, r, x = map(int, input().split())
    queries.append((l, r, x))

# Solve the problem
output = fair_split_haybales(N, haybales, Q, queries)

# Print the output
for o in output:
    print(o)
