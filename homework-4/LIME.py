import numpy as np
import torch
from lime import lime_image
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F


# Placeholder CNN model for illustration. Replace this with your actual model.
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(6 * 64 * 64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = x.reshape(-1, 6 * 64 * 64)  # Use view instead of reshape for clarity
        x = self.fc1(x)
        return x


# Function to predict model output given images and the model
def predict_fn(images, model):
    images = torch.from_numpy(images).permute(0, 3, 1, 2).float().to(device)
    logits = model(images)
    probs = F.softmax(logits, dim=1)
    return probs.detach().cpu().numpy()


# Function to rescale image values to be within 0-1 range.
# This is necessary because 'mark_boundaries' function expects image pixel values between 0 and 1.
def rescale_image(image):
    image_min = image.min()
    image_max = image.max()
    image = (image - image_min) / (image_max - image_min + 1e-5)
    return image


if __name__ == '__main__':
    # Initialize the model
    model = SimpleCNN()

    # Load your pre-trained model weights here
    # model.load_state_dict(torch.load('path_to_your_model_weights.pt'))

    # Set the model to evaluation mode.
    model.eval()

    # Define the device for the model
    device = torch.device('cpu')
    model.to(device)

    # Initialize LIME explainer
    explainer = lime_image.LimeImageExplainer()

    # Here, you will need to replace 'YOUR_IMAGE_TENSOR' with your actual image tensor.
    example_image = 'YOUR_IMAGE_TENSOR'

    # Convert image to numpy and make it suitable for LIME
    test_image = example_image.permute(1, 2, 0).numpy()

    # Generate explanations
    explanation = explainer.explain_instance(test_image,
                                             lambda x: predict_fn(x, model),
                                             top_labels=5,
                                             hide_color=0,
                                             num_samples=1000)

    # Get mask for the first prediction
    # positive_only: Only use "positive" features - ones that increase the prediction probability
    # num_features: The number of superpixels to include in the explanation
    # hide_rest: If true, the non-explanation part of the image is greyed out
    temp, mask = explanation.get_image_and_mask(explanation.top_labels[0],
                                                positive_only=True,
                                                num_features=10,
                                                hide_rest=False)

    # Normalize the image for visualization
    normalized_img = rescale_image(temp)

    # Visualize the explanation
    plt.imshow(mark_boundaries(normalized_img, mask))
    plt.show()  # Show the plot
