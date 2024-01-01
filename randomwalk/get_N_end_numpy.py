import numpy as np
import argparse, sys
import time


parser = argparse.ArgumentParser()
parser.add_argument('-seed', help=' : Set seed of random(or numpy.random) Module, default=42', default=42)
parser.add_argument('-Q_0', help=' : Set initial asset Q_0, default=10', default=10)
parser.add_argument('-step_n', help=' : Set initial step number, default=1024', default=1024)
args=parser.parse_args()


def get_N_end_using_numpy(my_seed=42, Q_0=10, step_n=1024*16):
    np.random.seed(my_seed)
    steps = np.random.choice(a=[-1, 0, 1], size=step_n)
    path = Q_0 + np.cumsum(steps)

    if (np.where(path==0)[0].size != 0):
        return np.where(path==0)[0][0]

    return get_N_end_using_numpy(my_seed, Q_0, step_n*4)



def main(argv, args):
    start_time = time.time()
    N_end = get_N_end_using_numpy(int(args.seed), int(args.Q_0), int(args.step_n))
    end_time = time.time()
    duration = end_time - start_time
    print(f"{int(args.Q_0)}, {N_end}, {duration}")


if __name__ == '__main__':
    argv = sys.argv
    main(argv ,args)