import numpy as np


def conv_2d(img_input, filt, st=1):
    h_in, w_in = img_input.shape
    h_f, w_f = filt.shape

    h_out = (h_in - h_f) // st + 1
    w_out = (w_in - w_f) // st + 1

    f_map = np.zeros((h_out, w_out))

    for i in range(h_out):
        for j in range(w_out):
            r_start = i * st
            c_start = j * st
            region = img_input[r_start : r_start + h_f, c_start : c_start + w_f]
            f_map[i, j] = np.sum(region * filt)

    return f_map


def pool_2d(f_map, p_size=2, st=2):
    h_map, w_map = f_map.shape
    h_out = (h_map - p_size) // st + 1
    w_out = (w_map - p_size) // st + 1

    downsampled = np.zeros((h_out, w_out))

    for i in range(h_out):
        for j in range(w_out):
            r_start = i * st
            c_start = j * st
            region = f_map[r_start : r_start + p_size, c_start : c_start + p_size]
            downsampled[i, j] = np.max(region)

    return downsampled


def relu_act(x):
    return np.maximum(0, x)


if __name__ == "__main__":
    img_data = np.array(
        [
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
        ]
    )

    v_filter = np.array(
        [
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1],
        ]
    )

    print("--- Original Image ---")
    print(img_data)

    f_map = conv_2d(img_data, v_filter)
    print("\n--- Feature Map after Convolution (edge detection) ---")
    print(f_map)

    act_map = relu_act(f_map)
    print("\n--- After ReLU Activation ---")
    print(act_map)

    downsampled = pool_2d(act_map, p_size=2, st=2)
    print("\n--- After Max Pooling (2x2) ---")
    print(downsampled)

    print("\nOriginal shape:", img_data.shape)
    print("Feature map shape after convolution:", f_map.shape)
    print("Shape after max pooling:", downsampled.shape)
