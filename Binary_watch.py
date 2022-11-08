class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hourCombination = defaultdict(list)
        minuteCombination = defaultdict(list)

        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        for i in range(4):
            for comb in combinations(hours, i):
                summ = sum(comb)
                if summ<12:
                    hourCombination[i].append(summ)
        for j in range(6):
            for comb in combinations(minutes, j):
                summ = sum(comb)
                if summ<60:
                    minuteCombination[j].append(summ)
        result = []
        finder = []
        for i in range(turnedOn+1):
            for j in range(turnedOn+1):
                if i+j == turnedOn:
                    finder.append([i,j])
        for comb in finder:
            
            first, second = comb
            
            if first in hourCombination and second in minuteCombination:
                for hour in hourCombination[first]:
                    for minute in minuteCombination[second]:
                        result.append("%d:%02d" % (hour, minute))
                
        return result


    
    


    
        
