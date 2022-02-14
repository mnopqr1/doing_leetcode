# [Leetcode 1642: Furthest building you can reach](https://leetcode.com/problems/furthest-building-you-can-reach/)

## Description 

You have `B` bricks and `L` ladders that you can use to climb buildings. The heights of the buildings are given in an array `H[0]`, `H[1]`, ...

Whenever you are faced with a building that is higher than the previous one (`H[n+1] > H[n]`), you need to either pay `1` ladder or `H[n+1] - H[n]` bricks.

Following an optimal strategy, what is the furthest building that you can reach?

## Thoughts

* Building `n + 1` is reachable with `B` bricks and `L` ladders means:
    * either `H[n + 1] <= H[n]` and building `n` is reachable with `B` bricks and `L` ladders
    * or `H[n+1] > H[n]` and building `n` is reachable with ...
        * either `B - (H[n+1] - H[n])` bricks and `L` ladders
        * or `B` bricks and `L-1` ladders

Unfortunately, the recursive solution that this suggests seems infeasible because the length of H can be `10^5` and `2^{10^5}` recursive calls seems a bad idea.

* I was thinking for a while about starting from the end of the array but that didn't get me anywhere.

* I'm going to call a step a *jump* if `H[n+1] > H[n]`. We can always at least execute `L` jumps, using the ladders. Every time we encounter a jump after that, it depends:
    * if an earlier jump was *smaller* than the current jump, then it would have been better to use bricks for that old jump, saving the ladder for the current jump.
    * if, on the other hand, all earlier jumps were *at least as big* as the current jump, then we may just as well use bricks for the current jump.

This suggests a strategy that only requires running through the list of heights once! We need to keep track of the `L` largest jumps, and of the number of bricks used. Also notice that in the strategy, whenever we do decide to use bricks at some point, we are *sure* that that's the best option we currently have, because to even get to this point, using bricks at any earlier time would have cost more than using bricks now.

## Implementation

* To execute this plan, we need to maintain a list of the `L` biggest jumps that we had to make so far, and we need to be able to insert jumps and find the least jump. So it seems like a good idea to keep this list of biggest jumps ordered throughout.

* My first implementation used `insort` from the [bisect](https://docs.python.org/3/library/bisect.html) module, which allows you to insert into an array. This gave a successful answer, but looking at others' solutions after that, I noticed that people use [heapq](https://docs.python.org/3/library/heapq.html), and this is significantly faster. I also found [an explanation](https://stackoverflow.com/questions/53005394/is-insertion-of-heapq-is-faster-than-insertion-of-bisect): every time you insert with insort into a list, all the later elements have to be shifted. A priority queue lets you do insertion in logartihmic time. So I wrote a version in [furthestbuilding_heap.py](furthestbuilding_heap.py) using `heapq` instead of `bisect`. I also rewrote the logic a little bit in that version but those changes are cosmetic.

* I had to fix a little bug for the edge case where `L == 0`: then the list of biggest jumps is empty so we can't compare to the least element in it and in Python that gives a runtime error.  

## Learnings 

* The `bisect` module has insertion in order function `insort` but it is relatively slow.

* The standard module for this type of problem is `heapq` (heap priority queue): maintaining the N best or N worst something with efficient inserting and popping the least (greatest) value.

* Test for improbable seeming edge cases, you can be sure that Leetcode will have some of them in the tests.
