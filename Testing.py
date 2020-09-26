import os
os.system('cls')
#---------------
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

#Add your code here!

total_damage = 0
modifier = STAB * Type * Critical * Other 
d1=(2*Level+10)/250
d2=Attack/Defense
total_damage=(d1*d2*Base+2)*modifier   

print(total_damage)
