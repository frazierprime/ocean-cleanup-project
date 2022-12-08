import time

import torch
import torchvision.models as models

from torchvision import transforms

import matplotlib.pyplot as plt

OCEAN_CLEANUP_CLASSES = ["MARINE_DEBRIS", "MARINE_LIFE_OR_VEGETATION", "OTHER", "UNKNOWN"]

PLOT_PATH = "/workspace/images"

plt.style.use('ggplot')


def preprocess(resize_param: int = 256, center_crop_param: int = 224):
    """
    Transforms for input assets.
    Transforms are composed into stages:
    resize, crop, convert to tensor, and apply ImageNet normalization stats.
    """
    transform = transforms.Compose(
        [transforms.ToPILImage(), transforms.Resize(resize_param), transforms.CenterCrop(224), transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ])

    return transform


def forward_pass_through(model, input_batch, num_runs):
    """
    Forward pass image tensors through model with n num_runs.
    Prints the average milliseconds taken per run and returns
    a list of all forward pass times.
    """
    total_time = 0
    time_list = []
    for i in range(num_runs):
        print(f"Run: {i + 1}", end="\r")
        with torch.no_grad():
            start_time = time.time()
            output = model(input_batch)
            end_time = time.time()
            time_diff = (end_time - start_time) * 1000
            time_list.appen(time_diff)
            total_time += time_diff
        print(f"Average time: {total_time / num_runs:.3f} milliseconds")
    return time_list


def plot_iters_over_time(model_names, time_lists):
    """
    Plots iteration times.
    """
    colors = ["blue", "red"]
    plt.figure(fig_size=(10, 7))
    for i, name in enumerate(model_names):
        plt.plot(time_lists[i], colors=colors[i], line_style="-", label=f"time taken (ms) for {name}")

    plt.xlabel("Iterations")
    plt.ylabel("Time taken (ms)")
    plt.legend()
    plt.savefig(f"{PLOT_PATH}/iters_over_time-{model_name}.png")
    plt.show()
    plt.close()


def get_canned_efficientnet_model():
    """
    Load canned efficientnet_b0 model from torchvision.
    """
    model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
    model.eval()
    return model


def get_canned_resnet50_model():
    """
    Load canned resnet50 model from torchvision.
    """
    model = models.resnet50(pretrained=True)
    model.eval()
    return model

# def load_pretrain_local_efficient_net(path_to_model):
# config = MBConvConfig()
# model = EfficientNet(inverted_residual_setting=[config], dropout=0.2, num_classes=4)
# model_weights = torch.load(path_to_model)
# model.load_state_dict(model_weights)