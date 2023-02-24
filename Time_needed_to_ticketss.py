class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        required_time = 0
        for i in range(tickets[k]):
            for j in range(len(tickets)):
                if tickets[j]!=0:
                    required_time+=1
                    tickets[j]-=1
                if tickets[k]==0:
                    return required_time
        return required_time
