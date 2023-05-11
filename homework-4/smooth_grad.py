import numpy as np
import torch
from nn_models import ExampleCNN
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F

class VanillaGrad:
    """ Class for computing gradients of the output w.r.t an input image for a pretrained model """

    def __init__(self, pretrained_model, cuda=False):
        self.pretrained_model = pretrained_model
        self.cuda = cuda

    def __call__(self, x, index=None):
        x.requires_grad_(True)
        output = self.pretrained_model(x)

        # If no index is provided, select the class with the highest probability
        if index is None:
            index = output.argmax(dim=1).item()

        one_hot = torch.zeros_like(output)
        one_hot[:, index] = 1
        one_hot = one_hot.to(x.device) if self.cuda else one_hot

        # Zero gradients
        self.pretrained_model.zero_grad()
        output.backward(gradient=one_hot)
        grad = x.grad.data

        return grad


class SmoothGrad(VanillaGrad):
    """ Class for computing SmoothGrad, which averages gradients of the output w.r.t input image over
        multiple noisy versions of the input """

    def __init__(self, pretrained_model, cuda=False, stdev_spread=0.15, n_samples=25, magnitude=True):
        super(SmoothGrad, self).__init__(pretrained_model, cuda)
        self.stdev_spread = stdev_spread
        self.n_samples = n_samples
        self.magnitude = magnitude

    def __call__(self, x, index=None):
        stdev = self.stdev_spread * (x.max() - x.min())
        total_gradients = torch.zeros_like(x)

        for _ in range(self.n_samples):
            noise = torch.normal(0, stdev, size=x.shape).to(x.device) if self.cuda else torch.normal(0, stdev, size=x.shape)
            x_plus_noise = x + noise

            grad = super(SmoothGrad, self).__call__(x_plus_noise, index=index)

            if self.magnitude:
                total_gradients += (grad * grad)
            else:
                total_gradients += grad

        avg_gradients = total_gradients / self.n_samples
        return avg_gradients


# Note: This is an overly simplified model and is meant for demonstration purposes only.
# It is used here as a placeholder. You should use what you've built for the previous questions.

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(6 * 64 * 64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = x.view(-1, 6 * 64 * 64)
        x = self.fc1(x)
        return x


if __name__ == '__main__':
    # Initialize your model by calling the class that defines your model architecture.
    # Here, 'ExampleCNN' is a placeholder for your model choice.
    model = ExampleCNN()

    # The weights from your pretrained model should be saved in a .pt file.
    model_weights = 'Load in your pretrained model weights.pt file here'

    # Uncomment the following line to load the weights into the model.
    # 'torch.load' will load the weights, and 'model.load_state_dict' will apply these weights to your model.
    # Make sure that the architecture of 'model' matches the architecture of the model that the weights came from.
    # model.load_state_dict(torch.load(model_weights))

    # Set the model to evaluation mode.
    # This step is necessary because it tells your model that it will be used for inference, not training.
    # In evaluation mode, certain layers like dropout are disabled.
    model.eval()

    # Initialize SmoothGrad. It will average the gradients over 25 noisy versions of the input. Each noisy version is
    # obtained by adding Gaussian noise to the input with a standard deviation of 15% of the input's range.
    # You can change these numbers to vary noise levels and number of images for averaging.
    smooth_grad = SmoothGrad(pretrained_model=model, cuda=False, stdev_spread=0.15, n_samples=25, magnitude=True)

    # Load saved example image (normalized) and label for demonstration purposes.
    # You can replace these with the image tensor you want to visualize
    example_image = torch.load('train_image.pth')
    example_label = torch.load('train_label.pth')

    # Compute the SmoothGrad saliency map
    # The image tensor is unsqueezed to add an extra dimension because the model expects a batch of images.
    # The dtype is set to float32, as the model expects input data in this format.
    smooth_saliency = smooth_grad(example_image.to(dtype=torch.float32).unsqueeze(0), example_label)

    # Convert the saliency map to absolute values, because we are interested in the magnitude of the gradients,
    # regardless of their direction.
    abs_saliency = np.abs(smooth_saliency.numpy())

    # Sum the absolute gradients across all color channels to get a single saliency map.
    # 'squeeze' is used to remove the extra dimension that was added earlier.
    saliency_map = np.sum(abs_saliency, axis=1).squeeze()

    # Display the final saliency map. The brighter a pixel in the saliency map, the more important it is for the model's decision.
    plt.imshow(saliency_map, cmap='gray')
    plt.show()


