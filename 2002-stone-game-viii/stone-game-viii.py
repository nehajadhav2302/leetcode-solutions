from itertools import accumulate
from typing import List


class Solution:

  def stoneGameVIII(self, stones: List[int]) -> int:
    # Compute prefix sums array
    pref = list(accumulate(stones))

    # Base case: if forced to pick the maximum allowed stones (index n - 1)
    ans = pref[-1]

    # Iterate backwards from index n - 2 down to 1 (since x > 1)
    for i in range(len(stones) - 2, 0, -1):
      ans = max(ans, pref[i] - ans)

    return ans