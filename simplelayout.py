import argparse
import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--board_grid', type=int, help='board_grid')
    parser.add_argument('--unit_grid', type=int, help='unit_grid')
    parser.add_argument('--unit_n', type=int, help='unit_n')
    parser.add_argument('--positions', type=int, help='positions')
    parser.add_argument('--outdir', type=str, help='outdir')
    parser.add_argument('--file_name', type=str, help='file_name')
    args = parser.parse_args()

    matrix = np.random.randint(0, 2, (args.board_grid, args.board_grid))
    data = {'f': matrix}
    path = args.outdir + '/' + args.file_name
    scio.savemat(path + '.mat', data)
    plt.imshow(data['f'])
    plt.savefig(path + '.jpg')
    return()


if __name__ == "__main__":
    main()
