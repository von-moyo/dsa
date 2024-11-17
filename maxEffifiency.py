def maximizeEfficiencyProduct(efficiencyScores):
    efficiencyScores.sort()
    
    max1 = efficiencyScores[-1] * efficiencyScores[-2] * efficiencyScores[-3] * efficiencyScores[-4] * efficiencyScores[-5]
    
    max2 = efficiencyScores[0] * efficiencyScores[1] * efficiencyScores[-1] * efficiencyScores[-2] * efficiencyScores[-3]
    
    return max(max1, max2)

