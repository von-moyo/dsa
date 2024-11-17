// function maximizeEfficiencyProduct(efficiencyScores) {
//   efficiencyScores.sort((a, b) => a - b);

//   let n = efficiencyScores.length;
//   let max1 = efficiencyScores[n - 1] * efficiencyScores[n - 2] * efficiencyScores[n - 3] * efficiencyScores[n - 4] * efficiencyScores[n - 5];

//   let max2 = efficiencyScores[0] * efficiencyScores[1] * efficiencyScores[n - 1] * efficiencyScores[n - 2] * efficiencyScores[n - 3];

//   return Math.max(max1, max2);
// }

function maximizeEfficiencyProduct(efficiencyScores) {
  let max1 = -Infinity, max2 = -Infinity, max3 = -Infinity, max4 = -Infinity, max5 = -Infinity;
  let min1 = Infinity, min2 = Infinity;
  
  for (let num of efficiencyScores) {
      if (num > max1) {
          [max5, max4, max3, max2, max1] = [max4, max3, max2, max1, num];
      } else if (num > max2) {
          [max5, max4, max3, max2] = [max4, max3, max2, num];
      } else if (num > max3) {
          [max5, max4, max3] = [max4, max3, num];
      } else if (num > max4) {
          [max5, max4] = [max4, num];
      } else if (num > max5) {
          max5 = num;
      }
      
      if (num < min1) {
          [min2, min1] = [min1, num];
      } else if (num < min2) {
          min2 = num;
      }
  }
  
  let product1 = max1 * max2 * max3 * max4 * max5;
  let product2 = max1 * max2 * max3 * min1 * min2;
  
  return Math.max(product1, product2);
}

let efficiencyScores = [6, 1, 2, 8, 1];
console.log(maximizeEfficiencyProduct(efficiencyScores)); // Output should be 96
