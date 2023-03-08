import os

inputDir = os.listdir('.')
powerpoints = []
for x in inputDir: 
    if x.endswith(".ppt"):
        powerpoints.append(x)

print(powerpoints)