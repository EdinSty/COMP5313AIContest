def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Input processing
    N = int(data[0])
    haybales = list(map(int, data[1:N+1]))
    Q = int(data[N+1])
    queries = data[N+2:]
    
    # Compute prefix sums
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + haybales[i - 1]
    
    # Precompute Bessie-Elsie difference for each range
    bessie_diff = [0] * (N + 1)
    total_diff = 0
    bessie_hay = 0
    elsie_hay = 0
    
    for i in range(1, N + 1):
        if bessie_hay <= elsie_hay:
            bessie_hay += haybales[i - 1]
        else:
            elsie_hay += haybales[i - 1]
        bessie_diff[i] = bessie_hay - elsie_hay
    
    # Process queries
    result = []
    idx = 0
    for _ in range(Q):
        l = int(queries[idx])
        r = int(queries[idx + 1])
        x = int(queries[idx + 2])
        idx += 3
        
        bessie_start = x
        diff_range = bessie_diff[r] - bessie_diff[l - 1]
        result.append(str(diff_range + bessie_start))
    
    # Output results
    sys.stdout.write("\n".join(result) + "\n")
