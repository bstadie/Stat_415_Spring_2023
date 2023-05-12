import torch
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def load_data(file_path, id_bytes, label_bytes, num_images, height, width, depth):
    """
    Function to load image data from a binary file.

    Parameters:
    file_path (str): Path to the binary file.
    id_bytes (int): Number of bytes used for the image ID.
    label_bytes (int): Number of bytes used for the image label.
    num_images (int): Number of images in the binary file.
    height (int): Height of the images.
    width (int): Width of the images.
    depth (int): Depth of the images (number of color channels).

    Returns:
    images (torch.Tensor): Tensor of image data.
    labels (torch.Tensor): Tensor of image labels.
    """

    # Define the record size in bytes
    record_size = id_bytes + label_bytes + height * width * depth

    # Initialize tensors to store the image IDs, labels, and data
    ids = torch.empty((num_images, id_bytes), dtype=torch.uint8)
    labels = torch.empty((num_images, label_bytes), dtype=torch.uint8)
    images = torch.empty((num_images, depth, height, width), dtype=torch.uint8)

    # Open the binary file and read the contents
    with open(file_path, 'rb') as file:
        for i in range(num_images):
            byte_record = file.read(record_size)

            # Convert the byte string to a tensor
            byte_tensor = torch.tensor(list(byte_record), dtype=torch.uint8)

            # Extract the image ID
            ids[i] = byte_tensor[:id_bytes].view(1, -1)

            # Extract the image label
            labels[i] = byte_tensor[id_bytes:id_bytes + label_bytes].view(1, -1)

            # Extract the image data
            array_image = byte_tensor[id_bytes + label_bytes:record_size].view(depth, height, width)
            images[i] = array_image

    # Ensure labels is a 1-D tensor
    labels = labels[:, -1]

    return images, labels


if __name__ == '__main__':
    # Specify parameters (information can be found in the readme file)
    id_bytes = 4
    label_bytes = 4
    num_train_files = 1
    num_train_images = 'FILL_IN_THIS_VALUE'
    num_test_image = 'FILL_IN_THIS_VALUE'
    width = 'FILL_IN_THIS_VALUE'
    height = 'FILL_IN_THIS_VALUE'
    depth = 'FILL_IN_THIS_VALUE'
    num_classes = 'FILL_IN_THIS_VALUE'

    # Load training and test data
    train_images, train_labels = load_data('binary_ver/data_batch_1.bin', id_bytes, label_bytes, num_train_images, height, width, depth)
    test_images, test_labels = load_data('binary_ver/test_batch.bin', id_bytes, label_bytes, num_test_image, height, width, depth)

    # Split training data into training and validation sets
    train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.1, random_state=42)

    # Print shapes of datasets
    print(train_images.shape)
    print(train_labels.shape)
    print(val_images.shape)
    print(val_labels.shape)
    print(test_images.shape)
    print(test_labels.shape)

    # Show the second training image
    plt.imshow(train_images[1].permute(1, 2, 0))
    plt.show()
