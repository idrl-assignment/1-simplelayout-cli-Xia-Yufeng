import argparse
import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--board_grid', type=int, help='board_grid')
parser.add_argument('--unit_grid', type=int, help='unit_grid')
parser.add_argument('--unit_n', type=int, help='unit_n')
parser.add_argument('--positions', type=int, help='positions')
parser.add_argument('--outdir', type=str, help='outdir')
parser.add_argument('--file_name', type=str, help='file_name')
args = parser.parse_args()


def main():
    data = {'f': np.random.randint(0, 2, (args.board_grid, args.board_grid))}
    # data = {'f': np.random.randint(0, 2, (100, 100))}
    path = args.outdir + '/' + args.file_name
    # path = 'example'
    scio.savemat(path + '.mat', data)
    plt.imshow(data['f'])
    plt.savefig(path + '.jpg')


if __name__ == "__main__":
    main()
