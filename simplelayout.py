import argparse
import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--board_grid', help='board_grid')
parser.add_argument('--unit_grid', help='unit_grid')
parser.add_argument('--unit_n', help='unit_n')
parser.add_argument('--positions', help='learning rate decay')
parser.add_argument('--outdir', help='outdir')
parser.add_argument('--file_name', help='training epochs')
args = parser.parse_args()

def main():
    data = {'f': np.random.randint(0, 2, (args.board_grid, args.board_grid))}
    path = args.outdir + '/' + args.file_name
    scio.savemat(path + '.mat', data)
    plt.imshow(data['f'])
    plt.savefig(path + '.jpg')


if __name__ == "__main__":
    main()
