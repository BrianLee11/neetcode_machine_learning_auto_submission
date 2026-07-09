import numpy as np
from numpy.typing import NDArray


"""
https://neetcode.io/problems/softmax/question
Input: z = [1, 2, 3]
Output: [0.09, 0.2447, 0.6652]
"""
import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)

        z = np.array(z, dtype = np.float64)
        max_z = np.max(z)
        
        z = z - max_z
        lenghth_z = len(z)

        exp_z = np.array([0] * lenghth_z, dtype = np.float64)

        for index in range(lenghth_z):
            exp_z[index] = np.exp(z[index])

        exp_sum = sum(exp_z)

        for index in range(lenghth_z):
            exp_z[index] = round(exp_z[index]/exp_sum, 4)

        return exp_z

