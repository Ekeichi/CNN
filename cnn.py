import numpy as np

class cnn:
    def __init__(self, input_shape, num_classes):
        return None
    
    def conv2d(self,input, kernel):
        """
        Conv 2D layer
        imput : must be a 2D input.
        kernel : must be a 2D filter.

        Returns : 2D output of the convolutional layer.
        """
        # Calculate the output size
        output_height = input.shape[0] - kernel.shape[0] + 1
        output_width = input.shape[1] - kernel.shape[1] + 1
        result = np.zeros((output_height, output_width))

        # Perform the convolution
        for i in range(output_height):
            for j in range(output_width):
                # Extract the current patch from the input
                patch = input[i:i+kernel.shape[0], j:j+kernel.shape[1]]
                
                # Compute the dot product (element-wise multiplication and sum)
                result[i, j] = np.sum(patch * kernel)
        
        return result
    
    def max_pooling(self, input, kernel_size):
        """
        Max Pooling layer
        input : must be a 2D input.
        kernel_size : must be a 2D filter.

        Returns : 2D output of the max pooling layer.
        """
        

input = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel = np.array([[1, 1], [1, 1]])

print(conv2d(input, kernel))
        