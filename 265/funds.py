IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    size = len(village)
    st, en, poi = 0, 0, 0

    curr_sum = 0
    max_so_far = village[0]

    for i in range(0, size):
       curr_sum = curr_sum + a[i]

        if max_so_far < curr_sum:
            max_so_far = curr_sum
            st = poi
            en = i

       if (curr_sum < 0):
          curr_sum = 0
          poi=i+1

    if max_so_far < 0:
       return 0, 0, 0

    return max_so_far, st+1, en+1
	
