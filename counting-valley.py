def countingValleys(steps, path):
    steps=0
    valley=0
    for i in path:
        if i=='U':
            steps+=1
        else:
            steps-=1
        if steps==0 and i=='U':
            valley+=1
    return valley
