class Solution:
    def sigmoid_one(self, z: float) -> float:
        # Formula: 1 / (1 + e^(-z))   
        return float(1 / (1+np.exp(-z)))    
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        length_z = len(z)
        x: NDArray[np.float64] = np.array([0] * length_z, dtype=np.float64)

        for index in range(length_z):
            x[index] = np.round(self.sigmoid_one(z[index]), 5)       

        return  x
        # one-line code 
        # return np.round(1 / (1 + np.exp(-z)), 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return np.array(np.maximum(0, z), dtype = np.float64)
