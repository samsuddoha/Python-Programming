
#problem set 1: counting students categories based on their score

scores = [95, 87, 72, 68, 91]
goldMedal=silverMedal=bronzeMedal=participationAward=0
for score in scores:
    if score>90:
        goldMedal+=1
    elif score<=90 and score>80:
        silverMedal+=1
    elif score<=80 and score>70:
        bronzeMedal+=1
    else:
        participationAward+=1
print(f"Gold Medal: {goldMedal} students")
print(f"Silver Medal: {silverMedal} students")
print(f"Bronze Medal: {bronzeMedal} students")
print(f"Participation Award: {participationAward} students")