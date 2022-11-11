# 14. Tower of Hanoi problem (obvious content)
# Solution: solution relies on this approach:
# 1) Move "n"-1 disks from 'A' to 'B', using 'C'
# 2) Move "nth disk from 'A' to 'C'
# 3) Move "n"-1 disks from 'B' to 'C' using 'A'

def ex14(n, from_rod, to_rod, aux_rod):
    if n != 0:
        ex14(n-1, from_rod, aux_rod, to_rod)
        print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
        ex14(n-1, aux_rod, to_rod, from_rod)


ex14(4, 'A', 'B', 'C')
