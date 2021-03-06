import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--board_grid', type=int, help='board_grid')
    parser.add_argument('--unit_grid', type=int, help='unit_grid')
    parser.add_argument('--unit_n', type=int, help='unit_n')
    parser.add_argument('--positions', type=int, nargs='+', help='positions')
    parser.add_argument('--outdir', type=str, help='outdir')
    parser.add_argument('--file_name', type=str, help='file_name')
    args = parser.parse_args()

    if args.board_grid % args.unit_grid != 0:
        sys.exit('User exit')
    if args.unit_n != len(args.positions):
        sys.exit('User exit')
    if min(args.positions) < 1:
        sys.exit('User exit')
    if max(args.positions) > (args.board_grid / args.unit_grid)**2:
        sys.exit('User exit')
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    filename = args.outdir + '/' + args.file_name
    with open(filename + '.mat', 'w') as _:
        pass
    with open(filename + '.jpg', 'w') as _:
        pass


if __name__ == "__main__":
    main()
