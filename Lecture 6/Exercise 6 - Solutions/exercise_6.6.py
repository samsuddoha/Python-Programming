#counting individuls based on age group

ages= [5, 17, 24, 13, 45, 67, 89, 15, 33, 12, 18, 64, 65, 70]

child=0
teen=0
adult=0
senior=0
for a in ages:
    if 0<=a<=12:
        child+=1
    elif 13<=a<=19:
        teen+=1
    elif 20<=a<=64:
        adult+=1
    elif a>=65:
        senior+=1
print(f"Child: {child}")
print(f"Teen: {teen}")
print(f"Adult: {adult}")
print(f"Senior: {senior}")