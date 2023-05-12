import os
import time
from tqdm.notebook import tqdm

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision.transforms import Normalize

import numpy as np
from sklearn.model_selection import train_test_split

from data_loader import load_data


# Define a normalization function
def normalize(data):
    data = data.to(dtype=torch.float32)
    img_mean = data.mean(dim=(0, 2, 3))
    img_std = data.std(dim=(0, 2, 3))
    normalize = Normalize(img_mean, img_std)
    preprocessed_data = normalize(data)
    return preprocessed_data


# Define the architecture of your Linear Model. You will need to fill in the blanks!
# input_size: This is the number of input features for the linear model. If you are dealing with flattened images, this will be the total number of pixels in each image.
# output_size: This is the number of output features for the linear model. In a classification task, this is typically equal to the number of classes.

class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(in_features='FILL_IN_THIS_VALUE', out_features='FILL_IN_THIS_VALUE')

    def forward(self, x):
        x = x.reshape(x.size(0), -1)  # Flatten the input
        return self.linear(x)


# Define the architecture of your CNN. You will need to fill in the blanks!
# Think about what the input and output of each layer should be
class VanillaCNN(nn.Module):
    def __init__(self):
        super(VanillaCNN, self).__init__()

        # Define the layers of your CNN here. You will need to choose appropriate values for the parameters.
        # For example, you might have a convolutional layer like this:
        # self.conv = nn.Conv2d(in_channels='FILL_IN_THIS_VALUE', out_channels='FILL_IN_THIS_VALUE', kernel_size='FILL_IN_THIS_VALUE', padding='FILL_IN_THIS_VALUE')

        # And a fully connected layer like this:
        # self.fc = nn.Linear(in_features='FILL_IN_THIS_VALUE', out_features='FILL_IN_THIS_VALUE')

        # Continue to define your network here...

    def forward(self, x):
        # Define the forward pass of your network here.
        # Remember to connect the layers as you have defined them.
        # Make sure the output of one layer matches the input of the next.
        pass


# Define the training function
def training_loop(model, dataset_train, dataset_val, epochs, batch_size, lr, save_path, model_name_str, device="cpu"):
    """
    Train a neural network model for digit recognition on the MNIST dataset.

    Parameters
    ----------
    model (nn.Module): PyTorch model to be trained

    dataset_train (Dataset): PyTorch datasets for training

    dataset_val (Dataset): PyTorch datasets for validation

    epochs (int):     number of iterations through the whole dataset for training

    batch_size (int): size of a single batch of inputs

    save_path (str):  path/filename for model checkpoint, e.g. 'my_model.pt'

    model_name_str (str):  name of the model, e.g. 'VanillaCNN'

    device (str):     device on which tensors are placed; should be 'cpu' or 'cuda'.

    Returns
    -------
    model (nn.Module): final trained model

    best_moded_save_path (str):   path/filename for model checkpoint with the best validation accuracy

    device (str):      the device on which we carried out training, so we can match it
                       when we test the final model on unseen data later

    train_acc_lst, val_acc_lst, train_loss_lst, val_loss_lst (list): lists of training and validation accuracy and loss
    """

    # initialize model and move it to the device
    model.to(device)

    # initialize an optimizer to update our model's parameters during training
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    # initialize a DataLoader object for each dataset
    train_dataloader = torch.utils.data.DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
    val_dataloader = torch.utils.data.DataLoader(dataset_val, batch_size=batch_size, shuffle=False)

    # a PyTorch categorical cross-entropy loss object
    loss_fn = nn.CrossEntropyLoss()

    # keep track of training and validation accuracy and loss
    train_acc_lst = []
    val_acc_lst = []
    train_loss_lst = []
    val_loss_lst = []

    # time training process
    start_time = time.time()

    print("Training model: ", model_name_str)

    # run our training loop
    for epoch_idx in tqdm(range(epochs)):

        print(f"-------------------- Begin Epoch {epoch_idx} --------------------")
        epoch_start_time = time.time()

        # keep track of the best validation accuracy; if improved upon, save checkpoint
        best_acc = 0.0

        # loop through the entire dataset once per epoch
        train_loss = 0.0
        train_acc = 0.0
        train_total = 0

        epoch_val_acc_lst = []
        epoch_val_loss_lst = []

        for batch_idx, batch in enumerate(tqdm(train_dataloader)):

            model.train()

            # clear gradients
            optimizer.zero_grad()

            # unpack data and labels
            x, y = batch
            x = x.to(device)
            y = y.to(device)

            # generate predictions and compute loss
            output = model(x.float())  # (batch_size, 10)
            loss = loss_fn(output, y)

            # compute accuracy
            preds = output.argmax(dim=1)
            acc = preds.eq(y).sum().item() / len(y)

            # compute gradients and update model parameters
            loss.backward()
            optimizer.step()

            # update batch training statistics
            train_loss += (loss * len(x))
            train_acc += (acc * len(x))
            train_total += len(x)

            ##########################
            # perform validation every 20 batch
            if batch_idx > 0 and batch_idx % 20 == 0:
                batch_val_loss = 0.0
                batch_val_acc = 0.0
                batch_val_total = 0

                model.eval()
                for val_batch_idx, batch in enumerate(val_dataloader):
                    # don't compute gradients during validation
                    with torch.no_grad():
                        # unpack data and labels
                        x, y = batch
                        x = x.to(device)
                        y = y.to(device)

                        # generate predictions and compute loss
                        output = model(x.float())
                        loss = loss_fn(output, y)

                        # compute accuracy
                        preds = output.argmax(dim=1)
                        acc = preds.eq(y).sum().item() / len(y)

                        # update batch validation statistics
                        batch_val_loss += (loss * len(x))
                        batch_val_acc += (acc * len(x))
                        batch_val_total += len(x)

                batch_val_loss /= batch_val_total
                batch_val_acc /= batch_val_total
                epoch_val_acc_lst.append(batch_val_acc)
                epoch_val_loss_lst.append(batch_val_loss.detach().cpu().numpy().item())

                if batch_val_acc > best_acc:
                    best_acc = batch_val_acc
                    best_model_save_path = save_path + "E" + str(epoch_idx) + "B" + str(
                        batch_idx) + "_" + model_name_str + ".pt"
                    print(
                        f"Epoch {epoch_idx}, Batch {batch_idx}: New best val acc {batch_val_acc :0.3f}, model weights saved to {best_model_save_path}")
                    torch.save(model.state_dict(), best_model_save_path)

        # update epoch training statistics
        train_loss /= train_total
        train_acc /= train_total
        train_acc_lst.append(train_acc)
        train_loss_lst.append(train_loss.detach().cpu().numpy().item())

        # update epoch validation statistics
        val_acc = np.mean(epoch_val_acc_lst)
        val_loss = np.mean(epoch_val_loss_lst)
        val_acc_lst.append(val_acc)
        val_loss_lst.append(val_loss)

        print(
            f"End of Epoch {epoch_idx}: train loss {train_loss :0.3f}, val loss {val_loss :0.3f}; train acc {train_acc :0.3f}, val acc {val_acc :0.3f}")
        print(
            f"Current total training time: {time.time() - start_time :0.3f} seconds; time for this epoch: {time.time() - epoch_start_time :0.3f} seconds")
        print(f"-------------------------------------------------------")

    return model, best_model_save_path, device, train_acc_lst, val_acc_lst, train_loss_lst, val_loss_lst


if __name__ == '__main__':

    # Define the saving path for trained models
    save_path = "./saved_models/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Check device availability
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Specify parameters (information can be found in the readme file)
    id_bytes = 4
    label_bytes = 4
    num_train_files = 1
    num_train_images = 'FILL_IN_THIS_VALUE'
    width = 'FILL_IN_THIS_VALUE'
    height = 'FILL_IN_THIS_VALUE'
    depth = 'FILL_IN_THIS_VALUE'
    num_classes = 'FILL_IN_THIS_VALUE'

    # Load training and test data
    train_images, train_labels = load_data('binary_ver/data_batch_1.bin', id_bytes, label_bytes, num_train_images,
                                           height, width, depth)

    # Split training data into training and validation sets
    train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.1, random_state=42)

    norm_train_images = normalize(train_images)
    norm_val_images = normalize(val_images)

    # initialize a Dataset object for each dataset
    dataset_train = TensorDataset(norm_train_images, train_labels)
    dataset_val = TensorDataset(norm_val_images, val_labels)

    # initialize a model
    model = 'FILL_IN_THIS_VALUE'
    epochs = 'FILL_IN_THIS_VALUE'
    batch_size = 'FILL_IN_THIS_VALUE'
    learning_rate = 'FILL_IN_THIS_VALUE'

    # train the model
    model, best_model_save_path, device, train_acc, val_acc, train_loss, val_loss = training_loop(
        model=model,
        dataset_train=dataset_train,
        dataset_val=dataset_val,
        epochs=epochs,
        batch_size=batch_size,
        lr=learning_rate,
        save_path="saved_models/",
        model_name_str='model',  # you should change this to the specific model name you are training
        device=device)
