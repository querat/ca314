import heapq

import numpy as np


def fast_fill(input_array):
    h_max = np.nanmax(input_array) + 100
    data_mask = np.isfinite(input_array)
    inside_mask = np_binary_erosion(
        data_mask,
        structure=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).astype(np.bool))
    edge_mask = (data_mask & ~inside_mask)
    output_array = np.copy(input_array)
    output_array[inside_mask] = h_max

    put = heapq.heappush
    get = heapq.heappop
    fill_heap = [
        (output_array[t_row, t_col], int(t_row), int(t_col), True)
        for t_row, t_col in np.transpose(np.where(edge_mask))]
    heapq.heapify(fill_heap)

    while True:
        try:
            h_crt, t_row, t_col, edge_flag = get(fill_heap)
        except IndexError:
            break
        for n_row, n_col in neighbors(t_row, t_col):
            if edge_flag:
                try:
                    if not inside_mask[n_row, n_col]:
                        continue
                except IndexError:
                    continue
            if output_array[n_row, n_col] == h_max:
                output_array[n_row, n_col] = max(
                    h_crt, input_array[n_row, n_col])
                put(fill_heap, (output_array[n_row, n_col], n_row, n_col, False))
    return output_array


def neighbors(row, col):
        return [
            (row - 1, col), (row, col + 1),
            (row + 1, col), (row, col - 1)]


def np_binary_erosion(input_array,
                      structure=np.ones((3, 3)).astype(np.bool)):
    rows, cols = input_array.shape
    output_shape = tuple(
        ss + dd - 1 for ss, dd in zip(input_array.shape, structure.shape))
    input_pad_array = np.zeros(output_shape).astype(np.bool)
    input_pad_array[1: rows+1, 1: cols+1] = input_array
    binary_erosion = np.zeros(output_shape).astype(np.bool)

    struc_mask = structure.astype(np.bool)
    for row in range(rows):
        for col in range(cols):
            binary_erosion[row+1, col+1] = np.min(
                input_pad_array[row: row+3, col: col+3][struc_mask])

    return binary_erosion[1: rows+1, 1: cols+1]
