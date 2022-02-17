# [Leetcode 1657: Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)

## Description 

You can transform a string of lowercase characters `w` by permuting its letters
or by swapping character names out: `aabbb` can be transformed into `bbaaa` by
swapping the names `a` and `b`. If you can reach `w2` from `w` in this way,
call `w2` *close* to `w`.

## Thoughts

* We want to somehow find an *invariant* for these transformations. My first
  thought was to look at the *letter profile* of a string `w`: the letter
profile of aabbbbc would be the list `[1,2,4]` (ordered upward). If two strings
have the same letter profile, then you can transform one into the other?

* Not quite, as Gargi (who I paired with) remarked: you also need to know that
  the exact same letters occur in both `w` and `w2`.

* So: the words should have the same content (letters occurring in them) *and*
  the same letter profile. 

## Implementation

* For the letter profile, I used Python Counter from collections, which creates
  a dictionary counting how many occurrences of each item you have in a list
(or a string, which is more or less the same thing as a list of characters in
Python).

* For the content, I got it from the letter profile by doing
  `set(profile.keys())`, but I later realized I could have just done that
directly with `set(w)`, which is a little clearer.

## Learnings 

* This was a fun problem, shows the usefulness of the idea of an invariant; it
  felt very math-y and reminded me of times when I was doing [semigroup theory](https://en.wikipedia.org/wiki/Semigroup). I believe this problem could
be formulated in a way that it is about commutative semigroups.

* You can be optimistic about what is possible with Python strings, usually the
  same as lists (like `set(w)` for a string `w`).

