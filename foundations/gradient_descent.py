class Solution:
    # helper functions    

    # Derivative function: f'(x) = 2x
    def derivative_function(self, x: float) -> float:
        return 2*x

    # Update function rule x = x - learning_rate * f'(x)
    def update_rule(self, x: float, learning_rate: float) -> float:
        return x - learning_rate * self.derivative_function(x)

    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        if iterations == 0:
            return init

        x = init
        count = 0

        for _ in range(iterations):         
            x = self.update_rule(x, learning_rate)            
        
        return round(x, 5)  

