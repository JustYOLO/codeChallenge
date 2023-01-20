# Recap
import sys
def draw_star(n):
    if n == 3: return ['***', '* *', '***']
    stars = []
    small = draw_star(n//3)
    for star in small:
        stars.append(star*3)
    for star in small:
        stars.append(star + ' '*(n//3) + star)
    for star in small:
        stars.append(star*3)
    
    return stars
n = int(sys.stdin.readline())
print("\n".join(draw_star(n)))