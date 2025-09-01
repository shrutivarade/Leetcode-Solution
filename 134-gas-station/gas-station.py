class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            netGas = gas[i] - cost[i]
            totalGas += netGas
            tank += netGas
            if tank < 0:
                start = i+1
                tank = 0
        
        return start if totalGas >= 0 and start < len(gas) else -1