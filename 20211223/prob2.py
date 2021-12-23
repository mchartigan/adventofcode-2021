'''
--- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

  #D#C#B#A#
  #D#B#A#C#

So, the above example now becomes:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

The amphipods still want to be organized into rooms similar to before:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

In this updated example, the least energy required to organize these amphipods is 44169:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?
'''

'''
#############   A:0
#...........#   B:0
###B#A#A#D###   C:0
  #D#C#B#A#     D:0
  #D#B#A#C#
  #B#C#D#C#
  #########

#############   A:10
#A.........A#   B:0
###B#.#.#D###   C:0
  #D#C#B#A#     D:0
  #D#B#A#C#
  #B#C#D#C#
  #########

#############   A:18
#AA.D.....BA#   B:5
###B#.#.#D###   C:0
  #D#C#.#A#     D:7
  #D#B#.#C#
  #B#C#.#C#
  #########

#############   A:18
#AA.D...B.BA#   B:11
###B#.#.#D###   C:17
  #D#.#.#A#     D:7
  #D#.#C#C#
  #B#.#C#C#
  #########

#############   A:18
#AA.D......A#   B:26
###B#.#.#D###   C:17
  #D#.#.#A#     D:7
  #D#B#C#C#
  #B#B#C#C#
  #########

#############   A:21
#AA.D.D...AA#   B:26
###B#.#.#.###   C:17
  #D#.#.#.#     D:11
  #D#B#C#C#
  #B#B#C#C#
  #########

#############   A:21
#AA.D.D...AA#   B:26
###B#.#C#.###   C:31
  #D#.#C#.#     D:11
  #D#B#C#.#
  #B#B#C#.#
  #########

#############   A:21
#AA.......AA#   B:26
###B#.#C#.###   C:31
  #D#.#C#.#     D:26
  #D#B#C#D#
  #B#B#C#D#
  #########

#############   A:21
#AA.......AA#   B:31
###.#.#C#D###   C:31
  #.#B#C#D#     D:46
  #.#B#C#D#
  #B#B#C#D#
  #########

#############   A:21
#AA.......AA#   B:38
###.#B#C#D###   C:31
  #.#B#C#D#     D:46
  #.#B#C#D#
  #.#B#C#D#
  #########

#############   A:49
#...........#   B:38
###A#B#C#D###   C:31
  #A#B#C#D#     D:46
  #A#B#C#D#
  #A#B#C#D#
  #########
'''

print(49*1 + 38*10 + 33*100 + 46*1000)