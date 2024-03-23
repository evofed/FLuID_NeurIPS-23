femnist_th_incre = 0.01
cifar_th_incre = 0.2

femnist_final_conv = ["cells.1.conv_b.op.2", "cells.1.downsample.1.2.2.2.2.2"]
femnist_final_batch = ["lastact.0"]
femnist_final_fc = ["classifier"]
femnist_model_layers = {
    "stem.0": {
        "ansestors": [],
        "descendants": ["stem.1"]
    },
    "stem.1": {
        "ansestors": ["stem.0"],
        "descendants": ["cells.0.conv_a.op.1", "cells.0.downsample.1.0"]
    },
    "cells.0.conv_a.op.1": {
        "ansestors": ["stem.1"],
        "descendants": ["cells.0.conv_a.op.2"]
    },
    "cells.0.conv_a.op.2": {
        "ansestors": ["cells.0.conv_a.op.1"],
        "descendants": ["cells.0.conv_b.op.1"]
    },
    "cells.0.conv_b.op.1": {
        "ansestors": ["cells.0.conv_a.op.2"],
        "descendants": ["cells.0.conv_b.op.2"]
    },
    "cells.0.conv_b.op.2": {
        "ansestors": ["cells.0.conv_b.op.1"],
        "descendants": ["cells.1.conv_a.op.1", "cells.1.downsample.1.0"]
    },
    "cells.0.downsample.1.0": {
        "ansestors": ["stem.1"],
        "descendants": ["cells.0.downsample.1.1"]
    },
    "cells.0.downsample.1.1": {
        "ansestors": ["cells.0.downsample.1.0"],
        "descendants": ["cells.0.downsample.1.2.0"]
    },
    "cells.0.downsample.1.2.0": {
        "ansestors": ["cells.0.downsample.1.1"],
        "descendants": ["cells.0.downsample.1.2.1"]
    },
    "cells.0.downsample.1.2.1": {
        "ansestors": ["cells.0.downsample.1.2.0"],
        "descendants": ["cells.0.downsample.1.2.2.0"]
    },
    "cells.0.downsample.1.2.2.0": {
        "ansestors": ["cells.0.downsample.1.2.1"],
        "descendants": ["cells.0.downsample.1.2.2.1"]
    },
    "cells.0.downsample.1.2.2.1": {
        "ansestors": ["cells.0.downsample.1.2.2.0"],
        "descendants": ["cells.0.downsample.1.2.2.2.0"]
    },
    "cells.0.downsample.1.2.2.2.0": {
        "ansestors": ["cells.0.downsample.1.2.2.1"],
        "descendants": ["cells.0.downsample.1.2.2.2.1"]
    },
    "cells.0.downsample.1.2.2.2.1": {
        "ansestors": ["cells.0.downsample.1.2.2.2.0"],
        "descendants": ["cells.0.downsample.1.2.2.2.2.0"]
    },
    "cells.0.downsample.1.2.2.2.2.0": {
        "ansestors": ["cells.0.downsample.1.2.2.2.1"],
        "descendants": ["cells.0.downsample.1.2.2.2.2.1"]
    },
    "cells.0.downsample.1.2.2.2.2.1": {
        "ansestors": ["cells.0.downsample.1.2.2.2.2.0"],
        "descendants": ["cells.0.downsample.1.2.2.2.2.2"]
    },
    "cells.0.downsample.1.2.2.2.2.2": {
        "ansestors": ["cells.0.downsample.1.2.2.2.2.1"],
        "descendants": ["cells.1.conv_a.op.1", "cells.1.downsample.1.0"]
    },
    "cells.1.conv_a.op.1": {
        "ansestors": ["cells.0.conv_b.op.2", "cells.0.downsample.1.2.2.2.2.2"],
        "descendants": ["cells.1.conv_a.op.2"]
    },
    "cells.1.conv_a.op.2": {
        "ansestors": ["cells.1.conv_a.op.1"],
        "descendants": ["cells.1.conv_b.op.1"]
    },
    "cells.1.conv_b.op.1": {
        "ansestors": ["cells.1.conv_a.op.2"],
        "descendants": ["cells.1.conv_b.op.2"]
    },
    "cells.1.conv_b.op.2": {
        "ansestors": ["cells.1.conv_b.op.1"],
        "descendants": ["lastact.0"]
    },
    "cells.1.downsample.1.0": {
        "ansestors": ["cells.0.conv_b.op.2", "cells.0.downsample.1.2.2.2.2.2"],
        "descendants": ["cells.1.downsample.1.1"]
    },
    "cells.1.downsample.1.1": {
        "ansestors": ["cells.1.downsample.1.0"],
        "descendants": ["cells.1.downsample.1.2.0"]
    },
    "cells.1.downsample.1.2.0": {
        "ansestors": ["cells.1.downsample.1.1"],
        "descendants": ["cells.1.downsample.1.2.1"]
    },
    "cells.1.downsample.1.2.1": {
        "ansestors": ["cells.1.downsample.1.2.0"],
        "descendants": ["cells.1.downsample.1.2.2.0.0"]
    },
    "cells.1.downsample.1.2.2.0.0": {
        "ansestors": ["cells.1.downsample.1.2.1"],
        "descendants": ["cells.1.downsample.1.2.2.0.1"]
    },
    "cells.1.downsample.1.2.2.0.1": {
        "ansestors": ["cells.1.downsample.1.2.2.0.0"],
        "descendants": ["cells.1.downsample.1.2.2.0.2"]
    },
    "cells.1.downsample.1.2.2.0.2": {
        "ansestors": ["cells.1.downsample.1.2.2.0.1"],
        "descendants": ["cells.1.downsample.1.2.2.1"]
    },
    "cells.1.downsample.1.2.2.1": {
        "ansestors": ["cells.1.downsample.1.2.2.0.2"],
        "descendants": ["cells.1.downsample.1.2.2.2.0"]
    },
    "cells.1.downsample.1.2.2.2.0": {
        "ansestors": ["cells.1.downsample.1.2.2.1"],
        "descendants": ["cells.1.downsample.1.2.2.2.1"]
    },
    "cells.1.downsample.1.2.2.2.1": {
        "ansestors": ["cells.1.downsample.1.2.2.2.0"],
        "descendants": ["cells.1.downsample.1.2.2.2.2.0"]
    },
    "cells.1.downsample.1.2.2.2.2.0": {
        "ansestors": ["cells.1.downsample.1.2.2.2.1"],
        "descendants": ["cells.1.downsample.1.2.2.2.2.1"]
    },
    "cells.1.downsample.1.2.2.2.2.1": {
        "ansestors": ["cells.1.downsample.1.2.2.2.2.0"],
        "descendants": ["cells.1.downsample.1.2.2.2.2.2"]
    },
    "cells.1.downsample.1.2.2.2.2.2": {
        "ansestors": ["cells.1.downsample.1.2.2.2.2.1"],
        "descendants": ["lastact.0"]
    },
    "lastact.0": {
        "ansestors": ["cells.1.conv_b.op.2", "cells.1.downsample.1.2.2.2.2.2"],
        "descendants": ["classifier"]
    },
    "classifier": {
        "ansestors": ["lastact.0"],
        "descendants": []
    }
}

speech_final_conv = ["layer4.0.conv2", "layer4.0.downsample.0"]
speech_final_batch = ["layer4.0.bn2", "layer4.0.downsample.1"]
speech_final_fc = ["fc"]
speech_model_layers = {
    "conv1": {
        "ansestors": [],
        "descendants": ["bn1"]
    },
    "bn1": {
        "ansestors": ["conv1"],
        "descendants": ["layer1.0.conv1", "layer2.0.conv1.0", "layer2.0.downsample.0"]
    },
    "layer1.0.conv1": {
        "ansestors": ["bn1"],
        "descendants": ["layer1.0.bn1"]
    },
    "layer1.0.bn1": {
        "ansestors": ["layer1.0.conv1"],
        "descendants": ["layer1.0.conv2"]
    },
    "layer1.0.conv2": {
        "ansestors": ["layer1.0.bn1"],
        "descendants": ["layer1.0.bn2"]
    },
    "layer1.0.bn2": {
        "ansestors": ["layer1.0.conv2"],
        "descendants": ["layer2.0.conv1.0", "layer2.0.downsample.0"]
    },
    "layer2.0.conv1.0": {
        "ansestors": ["bn1", "layer1.0.bn2"],
        "descendants": ["layer2.0.conv1.1"]
    },
    "layer2.0.conv1.1": {
        "ansestors": ["layer2.0.conv1.0"],
        "descendants": ["layer2.0.conv1.2"]
    },
    "layer2.0.conv1.2": {
        "ansestors": ["layer2.0.conv1.1"],
        "descendants": ["layer2.0.bn1"]
    },
    "layer2.0.bn1": {
        "ansestors": ["layer2.0.conv1.2"],
        "descendants": ["layer2.0.conv2"]
    },
    "layer2.0.conv2.0": {
        "ansestors": ["layer2.0.bn1"],
        "descendants": ["layer2.0.conv2.1"]
    },
    "layer2.0.conv2.1": {
        "ansestors": ["layer2.0.conv2.0"],
        "descendants": ["layer2.0.conv2.2"]
    },
    "layer2.0.conv2.2": {
        "ansestors": ["layer2.0.conv2.1"],
        "descendants": ["layer2.0.bn2"]
    },
    "layer2.0.bn2": {
        "ansestors": ["layer2.0.conv2.2"],
        "descendants": ["layer3.0.conv1.0", "layer3.0.downsample.0"]
    },
    "layer2.0.downsample.0": {
        "ansestors": ["bn1", "layer1.0.bn2"],
        "descendants": ["layer2.0.downsample.1"]
    },
    "layer2.0.downsample.1": {
        "ansestors": ["layer2.0.downsample.0"],
        "descendants": ["layer3.0.conv1.0", "layer3.0.downsample.0"]
    },
    "layer3.0.conv1.0": {
        "ansestors": ["layer2.0.bn2", "layer2.0.downsample.1"],
        "descendants": ["layer3.0.conv1.1"]
    },
    "layer3.0.conv1.1": {
        "ansestors": ["layer3.0.conv1.0"],
        "descendants": ["layer3.0.conv1.2"]
    },
    "layer3.0.conv1.2": {
        "ansestors": ["layer3.0.conv1.1"],
        "descendants": ["layer3.0.bn1"]
    },

    "layer3.0.bn1": {
        "ansestors": ["layer3.0.conv1.2"],
        "descendants": ["layer3.0.conv2"]
    },
    "layer.3.conv2": {
        "ansestors": ["layer3.0.bn1"],
        "descendants": ["layer3.0.bn2"]
    },
    "layer3.0.bn2": {
        "ansestors": ["layer3.0.conv2"],
        "descendants": ["layer4.0.conv1", "layer4.0.downsample.0"]
    },
    "layer3.0.downsample.0": {
        "ansestors": ["layer2.0.downsample.1", "layer2.0.bn2"],
        "descendants": ["layer3.0.downsample.1"]
    },
    "layer3.0.downsample.1": {
        "ansestors": ["layer3.0.downsample.0"],
        "descendants": ["layer4.0.conv1", "layer4.0.downsample.0"]
    },
    "layer4.0.conv1": {
        "ansestors": ["layer3.0.bn2", "layer3.0.downsample.1"],
        "descendants": ["layer4.0.bn1"]
    },
    "layer4.0.bn1": {
        "ansestors": ["layer4.0.conv1"],
        "descendants": ["layer4.0.conv2"]
    },
    "layer4.0.conv2": {
        "ansestors": ["layer4.0.bn1"],
        "descendants": ["layer4.0.bn2"]
    },
    "layer4.0.bn2": {
        "ansestors": ["layer4.0.conv2"],
        "descendants": ["fc"]
    },
    "layer4.0.downsample.0": {
        "ansestors": ["layer3.0.bn2", "layer3.0.downsample.1"],
        "descendants": ["layer4.0.downsample.1"]
    },
    "layer4.0.downsample.1": {
        "ansestors": ["layer4.0.downsample.0"],
        "descendants": ["fc"]
    },
    "fc": {
        "ansestors": ["layer4.0.bn2", "layer4.0.downsample.1"],
        "descendants": []
    }
}

cifar_final_conv = []
cifar_final_batch = []
cifar_final_fc = []
cifar_model_layers = {}

openimage_final_conv = []
openimage_final_batch = []
openimage_final_fc = []
openimage_model_layers = {}
