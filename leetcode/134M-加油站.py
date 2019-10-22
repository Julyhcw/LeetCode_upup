class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):return -1
        n = 0
        cur_gas,total_gas = 0, 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i] 
            if cur_gas < 0:
                n = i + 1
                cur_gas = 0
        return n if total_gas >= 0 else -1