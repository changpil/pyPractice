sunday = [1,2,3,4,5,6]
monday = [4,5,6,7,8]
tuesday = [43,3,45,2,1,3]

daily = [sunday, monday, tuesday]
print(daily)

transpose1 = list(zip(sunday, monday, tuesday))
print(transpose1)

transpose2 = list(zip(*daily))
print(transpose2)
