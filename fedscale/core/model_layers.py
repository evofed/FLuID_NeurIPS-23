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
    "layer3.0.conv2": {
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

cifar_final_conv = ["features.12.0"]
cifar_final_batch = ["features.12.1"]
cifar_final_fc = ["classifier.0", "classifier.3"]
cifar_model_layers = {
    "features.0.0": {
        "ansestors": [],
        "descendants": ["features.0.1"]
    },
    "features.0.1": {
        "ansestors": ["features.0.0"],
        "descendants": ["features.1.block.0.0"]
    },
    "features.1.block.0.0": {
        "ansestors": ["features.0.1"],
        "descendants": ["features.1.block.0.1"]
    },
    "features.1.block.0.1": {
        "ansestors": ["features.1.block.0.0"],
        "descendants": ["features.1.block.1.fc1", "features.1.block.2.0"]
    },
    "features.1.block.1.fc1": {
        "ansestors": ["features.0.1"],
        "descendants": ["features.1.block.1.fc2"]
    },
    "features.1.block.1.fc2": {
        "ansestors": ["features.1.block.1.fc1"],
        "descendants": ["features.1.block.2.0"]
    },
    "features.1.block.2.0": {
        "ansestors": ["features.1.block.1.fc2", "features.1.block.0.1"],
        "descendants": ["features.1.block.2.1"]
    },
    "features.1.block.2.1": {
        "ansestors": ["features.1.block.2.0"],
        "descendants": ["features.2.block.0.0"]
    },
    "features.2.block.0.0": {
        "ansestors": ["features.1.block.2.1"],
        "descendants": ["features.2.block.0.1"]
    },
    "features.2.block.0.1": {
        "ansestors": ["features.2.block.0.0"],
        "descendants": ["features.2.block.1.0.0"]
    },
    "features.2.block.1.0.0": {
        "ansestors": ["features.2.block.0.1"],
        "descendants": ["features.2.block.1.0.1"]
    },
    "features.2.block.1.0.1": {
        "ansestors": ["features.2.block.1.0.0"],
        "descendants": ["features.2.block.1.0.2.0"]
    },
    "features.2.block.1.0.2.0": {
        "ansestors": ["features.2.block.1.0.1"],
        "descendants": ["features.2.block.1.0.2.1"]
    },
    "features.2.block.1.0.2.1": {
        "ansestors": ["features.2.block.1.0.2.0"],
        "descendants": ["features.2.block.1.0.2.2"]
    },
    "features.2.block.1.0.2.2": {
        "ansestors": ["features.2.block.1.0.2.1"],
        "descendants": ["features.2.block.1.1"]
    },
    "features.2.block.1.1": {
        "ansestors": ["features.2.block.1.0.2.2"],
        "descendants": ["features.2.block.2.0"]
    },
    "features.2.block.2.0": {
        "ansestors": ["features.2.block.1.1"],
        "descendants": ["features.2.block.2.1"]
    },
    "features.2.block.2.1": {
        "ansestors": ["features.2.block.2.0"],
        "descendants": ["features.3.block.0.0.0", "features.4.block.0.0"]
    },
    "features.3.block.0.0.0": {
        "ansestors": ["features.2.block.2.1"],
        "descendants": ["features.3.block.0.0.1"]
    },
    "features.3.block.0.0.1": {
        "ansestors": ["features.3.block.0.0.0"],
        "descendants": ["features.3.block.0.0.2"]
    },
    "features.3.block.0.0.2": {
        "ansestors": ["features.3.block.0.0.1"],
        "descendants": ["features.3.block.0.1"]
    },
    "features.3.block.0.1": {
        "ansestors": ["features.3.block.0.0.2"],
        "descendants": ["features.3.block.1.0"]
    },
    "features.3.block.1.0": {
        "ansestors": ["features.3.block.0.1"],
        "descendants": ["features.3.block.1.1"]
    },
    "features.3.block.1.1": {
        "ansestors": ["features.3.block.1.0"],
        "descendants": ["features.3.block.2.0"]
    },
    "features.3.block.2.0": {
        "ansestors": ["features.3.block.1.1"],
        "descendants": ["features.3.block.2.1"]
    },
    "features.3.block.2.1": {
        "ansestors": ["features.3.block.2.0"],
        "descendants": ["features.4.block.0.0"]
    },
    "features.4.block.0.0": {
        "ansestors": ["features.3.block.2.1", "features.2.block.2.1"],
        "descendants": ["features.4.block.0.1"]
    },
    "features.4.block.0.1": {
        "ansestors": ["features.4.block.0.0"],
        "descendants": ["features.4.block.1.0"]
    },
    "features.4.block.1.0": {
        "ansestors": ["features.4.block.0.1"],
        "descendants": ["features.4.block.1.1"]
    },
    "features.4.block.1.1": {
        "ansestors": ["features.4.block.1.0"],
        "descendants": ["features.4.block.2.fc1", "features.4.block.3.0"]
    },
    "features.4.block.2.fc1": {
        "ansestors": ["features.4.block.1.1"],
        "descendants": ["features.4.block.2.fc2"]
    },
    "features.4.block.2.fc2": {
        "ansestors": ["features.4.block.2.fc1"],
        "descendants": ["features.4.block.3.0"]
    },
    "features.4.block.3.0": {
        "ansestors": ["features.4.block.2.fc2", "features.4.block.1.1"],
        "descendants": ["features.4.block.3.1"]
    },
    "features.4.block.3.1": {
        "ansestors": ["features.4.block.3.0"],
        "descendants": ["features.5.block.0.0", "features.6.block.0.0", "features.7.block.0.0"]
    },
    "features.5.block.0.0": {
        "ansestors": ["features.4.block.3.1"],
        "descendants": ["features.5.block.0.1"]
    },
    "features.5.block.0.1": {
        "ansestors": ["features.5.block.0.0"],
        "descendants": ["features.5.block.1.0"]
    },
    "features.5.block.1.0": {
        "ansestors": ["features.5.block.0.1"],
        "descendants": ["features.5.block.1.1"]
    },
    "features.5.block.1.1": {
        "ansestors": ["features.5.block.1.0"],
        "descendants": ["features.5.block.2.fc1", "features.5.block.3.0"]
    },
    "features.5.block.2.fc1": {
        "ansestors": ["features.5.block.1.1"],
        "descendants": ["features.5.block.2.fc2"]
    },
    "features.5.block.2.fc2": {
        "ansestors": ["features.5.block.2.fc1"],
        "descendants": ["features.5.block.3.0"]
    },
    "features.5.block.3.0": {
        "ansestors": ["features.5.block.2.fc2", "features.5.block.1.1"],
        "descendants": ["features.5.block.3.1"]
    },
    "features.5.block.3.1": {
        "ansestors": ["features.5.block.3.0"],
        "descendants": ["features.6.block.0.0", "features.7.block.0.0"]
    },
    "features.6.block.0.0": {
        "ansestors": ["features.5.block.3.1"],
        "descendants": ["features.6.block.0.1"]
    },
    "features.6.block.0.1": {
        "ansestors": ["features.6.block.0.0"],
        "descendants": ["features.6.block.1.0"]
    },
    "features.6.block.1.0": {
        "ansestors": ["features.6.block.0.1"],
        "descendants": ["features.6.block.1.1"]
    },
    "features.6.block.1.1": {
        "ansestors": ["features.6.block.1.0"],
        "descendants": ["features.6.block.2.fc1", "features.6.block.3.0"]
    },
    "features.6.block.2.fc1": {
        "ansestors": ["features.6.block.1.1"],
        "descendants": ["features.6.block.2.fc2"]
    },
    "features.6.block.2.fc2": {
        "ansestors": ["features.6.block.2.fc1"],
        "descendants": ["features.6.block.3.0"]
    },
    "features.6.block.3.0": {
        "ansestors": ["features.6.block.2.fc2", "features.6.block.1.1"],
        "descendants": ["features.6.block.3.1"]
    },
    "features.6.block.3.1": {
        "ansestors": ["features.6.block.3.0"],
        "descendants": ["features.7.block.0.0"]
    },
    "features.7.block.0.0": {
        "ansestors": ["features.6.block.3.1", "features.5.block.3.1", "features.4.block.3.1"],
        "descendants": ["features.7.block.0.1"]
    },
    "features.7.block.0.1": {
        "ansestors": ["features.7.block.0.0"],
        "descendants": ["features.7.block.1.0"]
    },
    "features.7.block.1.0": {
        "ansestors": ["features.7.block.0.1"],
        "descendants": ["features.7.block.1.1"]
    },
    "features.7.block.1.1": {
        "ansestors": ["features.7.block.1.0"],
        "descendants": ["features.7.block.2.fc1", "features.7.block.3.0"]
    },
    "features.7.block.2.fc1": {
        "ansestors": ["features.7.block.1.1"],
        "descendants": ["features.7.block.2.fc2"]
    },
    "features.7.block.2.fc2": {
        "ansestors": ["features.7.block.2.fc1"],
        "descendants": ["features.7.block.3.0"]
    },
    "features.7.block.3.0": {
        "ansestors": ["features.7.block.2.fc2", "features.7.block.1.1"],
        "descendants": ["features.7.block.3.1"]
    },
    "features.7.block.3.1": {
        "ansestors": ["features.7.block.3.0"],
        "descendants": ["features.8.block.0.0", "features.9.block.0.0"]
    },
    "features.8.block.0.0": {
        "ansestors": ["features.7.block.3.1"],
        "descendants": ["features.8.block.0.1"]
    },
    "features.8.block.0.1": {
        "ansestors": ["features.8.block.0.0"],
        "descendants": ["features.8.block.1.0"]
    },
    "features.8.block.1.0": {
        "ansestors": ["features.8.block.0.1"],
        "descendants": ["features.8.block.1.1"]
    },
    "features.8.block.1.1": {
        "ansestors": ["features.8.block.1.0"],
        "descendants": ["features.8.block.2.fc1", "features.8.block.3.0"]
    },
    "features.8.block.2.fc1": {
        "ansestors": ["features.8.block.1.1"],
        "descendants": ["features.8.block.2.fc2"]
    },
    "features.8.block.2.fc2": {
        "ansestors": ["features.8.block.2.fc1"],
        "descendants": ["features.8.block.3.0"]
    },
    "features.8.block.3.0": {
        "ansestors": ["features.8.block.2.fc2", "features.8.block.1.1"],
        "descendants": ["features.8.block.3.1"]
    },
    "features.8.block.3.1": {
        "ansestors": ["features.8.block.3.0"],
        "descendants": ["features.9.block.0.0"]
    },
    "features.9.block.0.0": {
        "ansestors": ["features.8.block.3.1"],
        "descendants": ["features.9.block.0.1"]
    },
    "features.9.block.0.1": {
        "ansestors": ["features.9.block.0.0"],
        "descendants": ["features.9.block.1.0"]
    },
    "features.9.block.1.0": {
        "ansestors": ["features.9.block.0.1"],
        "descendants": ["features.9.block.1.1"]
    },
    "features.9.block.1.1": {
        "ansestors": ["features.9.block.1.0"],
        "descendants": ["features.9.block.2.fc1", "features.9.block.3.0"]
    },
    "features.9.block.2.fc1": {
        "ansestors": ["features.9.block.1.1"],
        "descendants": ["features.9.block.2.fc2"]
    },
    "features.9.block.2.fc2": {
        "ansestors": ["features.9.block.2.fc1"],
        "descendants": ["features.9.block.3.0"]
    },
    "features.9.block.3.0": {
        "ansestors": ["features.9.block.2.fc2", "features.9.block.1.1"],
        "descendants": ["features.9.block.3.1"]
    },
    "features.9.block.3.1": {
        "ansestors": ["features.9.block.3.0"],
        "descendants": ["features.10.block.0.0", "features.11.block.0.0", "features.12.0"]
    },
    "features.10.block.0.0": {
        "ansestors": ["features.9.block.3.1"],
        "descendants": ["features.10.block.0.1"]
    },
    "features.10.block.0.1": {
        "ansestors": ["features.10.block.0.0"],
        "descendants": ["features.10.block.1.0"]
    },
    "features.10.block.1.0": {
        "ansestors": ["features.10.block.0.1"],
        "descendants": ["features.10.block.1.1"]
    },
    "features.10.block.1.1": {
        "ansestors": ["features.10.block.1.0"],
        "descendants": ["features.10.block.2.fc1", "features.10.block.3.0"]
    },
    "features.10.block.2.fc1": {
        "ansestors": ["features.10.block.1.1"],
        "descendants": ["features.10.block.2.fc2"]
    },
    "features.10.block.2.fc2": {
        "ansestors": ["features.10.block.2.fc1"],
        "descendants": ["features.10.block.3.0"]
    },
    "features.10.block.3.0": {
        "ansestors": ["features.10.block.2.fc2", "features.10.block.1.1"],
        "descendants": ["features.10.block.3.1"]
    },
    "features.10.block.3.1": {
        "ansestors": ["features.10.block.3.0"],
        "descendants": ["features.11.block.0.0", "features.12.0"]
    },
    "features.11.block.0.0": {
        "ansestors": ["features.10.block.3.1"],
        "descendants": ["features.11.block.0.1"]
    },
    "features.11.block.0.1": {
        "ansestors": ["features.11.block.0.0"],
        "descendants": ["features.11.block.1.0"]
    },
    "features.11.block.1.0": {
        "ansestors": ["features.11.block.0.1"],
        "descendants": ["features.11.block.1.1"]
    },
    "features.11.block.1.1": {
        "ansestors": ["features.11.block.1.0"],
        "descendants": ["features.11.block.2.fc1", "features.11.block.3.0"]
    },
    "features.11.block.2.fc1": {
        "ansestors": ["features.11.block.1.1"],
        "descendants": ["features.11.block.2.fc2"]
    },
    "features.11.block.2.fc2": {
        "ansestors": ["features.11.block.2.fc1"],
        "descendants": ["features.11.block.3.0"]
    },
    "features.11.block.3.0": {
        "ansestors": ["features.11.block.2.fc2", "features.11.block.1.1"],
        "descendants": ["features.11.block.3.1"]
    },
    "features.11.block.3.1": {
        "ansestors": ["features.11.block.3.0"],
        "descendants": ["features.12.0"]
    },
    "features.12.0": {
        "ansestors": ["features.11.block.3.1"],
        "descendants": ["features.12.1"]
    },
    "features.12.1": {
        "ansestors": ["features.12.0"],
        "descendants": ["classifier.0"]
    },
    "classifier.0": {
        "ansestors": ["features.12.1"],
        "descendants": ["classifier.3"]
    },
    "classifier.3": {
        "ansestors": ["classifier.0"],
        "descendants": []
    }
}

openimage_final_conv = ["layer4.conv2.2", "layer4.0.downsample.0"]
openimage_final_batch = ["layer4.0.downsample.1"]
openimage_final_fc = ["fc"]
openimage_model_layers = {
    "conv1": {
        "ansestors": [],
        "descendants": ["bn1"]
    },
    "bn1": {
        "ansestors": ["conv1"],
        "descendants": ["layer1.0.conv1", "layer1.0.downsample.0"]
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
        "descendants": ["layer2.0.conv1", "layer2.0.downsample.0"]
    },
    "layer1.0.downsample.0": {
        "ansestors": ["bn1"],
        "descendants": ["layer1.0.downsample.1"]
    },
    "layer1.0.downsample.1": {
        "ansestors": ["layer1.0.downsample.0"],
        "descendants": ["layer2.0.conv1", "layer2.0.downsample.0"]
    },
    "layer2.0.conv1": {
        "ansestors": ["layer1.0.bn2", "layer1.0.downsample.1"],
        "descendants": ["layer2.0.bn1"]
    },
    "layer2.0.bn1": {
        "ansestors": ["layer2.0.conv1"],
        "descendants": ["layer2.0.conv2"]
    },
    "layer2.0.conv2": {
        "ansestors": ["layer2.0.bn1"],
        "descendants": ["layer2.0.bn2"]
    },
    "layer2.0.bn2": {
        "ansestors": ["layer2.0.conv2"],
        "descendants": ["layer3.0.conv1", "layer3.0.downsample.0"]
    },
    "layer2.0.downsample.0": {
        "ansestors": ["layer1.0.downsample.1"],
        "descendants": ["layer2.0.downsample.1"]
    },
    "layer2.0.downsample.1": {
        "ansestors": ["layer2.0.downsample.0"],
        "descendants": ["layer3.0.conv1", "layer3.0.downsample.0"]
    },
    "layer3.0.conv1": {
        "ansestors": ["layer2.0.bn2", "layer2.0.downsample.1"],
        "descendants": ["layer3.0.bn1"]
    },
    "layer3.0.bn1": {
        "ansestors": ["layer3.0.conv1"],
        "descendants": ["layer3.0.conv2"]
    },
    "layer3.0.conv2": {
        "ansestors": ["layer3.0.bn1"],
        "descendants": ["layer3.0.bn2"]
    },
    "layer3.0.bn2": {
        "ansestors": ["layer3.0.conv2"],
        "descendants": ["layer4.0.conv1", "layer4.0.downsample.0"]
    },
    "layer3.0.downsample.0": {
        "ansestors": ["layer2.0.downsample.1"],
        "descendants": ["layer3.0.downsample.1"]
    },
    "layer3.0.downsample.1": {
        "ansestors": ["layer3.0.downsample.0"],
        "descendants": ["layer4.0.conv1.0", "layer4.0.downsample.0"]
    },
    "layer4.0.conv1.0": {
        "ansestors": ["layer3.0.bn2", "layer3.0.downsample.1"],
        "descendants": ["layer4.0.conv1.1"]
    },
    "layer4.0.conv1.1": {
        "ansestors": ["layer4.0.conv1.0"],
        "descendants": ["layer4.0.conv1.2"]
    },
    "layer4.0.conv1.2": {
        "ansestors": ["layer4.0.conv1.1"],
        "descendants": ["layer4.0.bn1"]
    },
    "layer4.0.bn1": {
        "ansestors": ["layer4.0.conv1.2"],
        "descendants": ["layer4.0.conv2.0"]
    },
    "layer4.0.conv2.0": {
        "ansestors": ["layer4.0.bn1"],
        "descendants": ["layer4.0.conv2.1"]
    },
    "layer4.0.conv2.1": {
        "ansestors": ["layer4.0.conv2.0"],
        "descendants": ["layer4.0.conv2.2"]
    },
    "layer4.0.conv2.2": {
        "ansestors": ["layer4.0.conv2.1"],
        "descendants": ["layer4.0.bn2"]
    },
    "layer4.0.bn2": {
        "ansestors": ["layer4.0.conv2.2"],
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
