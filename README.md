1. **Dataset prep**
    1. Download the MNIST dataset
    2. Normalize the data : Scale pixel values from the range [0, 255] to [0, 1].
    3. Reshape the data : Each 28x28 image should be reshaped with an additional depth channel (28x28x1) to simulate the input structure for CNNs.
2. **Initialise Network Architecture**
    1. Design the architecture : Let’s do 2 or 3 conv layers and 1 or 2 fully connected layers. 
        1. Need to implement the conv layer before, I don’t want to use Torch or anything else.
        2. Same for the fully connected layer. Have to understand how everything work.
        3. Also do Pool layer and Dropout.
    2. Set up fully connected layers: Initialize weights for the dense layers at the end of the network.
3. **Forward pass implementation**
    1. Convolution operation
        1. Manually perform the convolution operation between the input image and each filter, calculating the dot product over patches of the image.
    2. Apply activation func (reLU)
        1. Apply the ReLU function to the feature maps to introduce non-linearity.
    3. Pooling (Max Pooling)
    4. Flatten the output of the final Conv layer to FCL.
4. **Classification with Fully Connected Layers**
    1. Pass the flattened output through fully connected layers.
    2. Apply Softmax activation in the output layer for multi-class classification (since MNIST has 10 classes).
5. Loss Calculation
    1. Define the loss func (cross entropy loss)
    2. calculate the difference between the predicted value and the real one.
6. Backprop
    1. Compute the gradients of the loss with respect to the network weights (for each convolutional and fully connected layer).
    2. Implement gradient descent to update the weights of the network based on the calculated gradients.
7. Training loop
    1. Feed forward training batch.
    2. Calculate loss.
    3. Perform backpropagation.
    4. Update weights.
8. Validation and Testing
