from random import seed, random
import argparse, sys
import time


parser = argparse.ArgumentParser()
parser.add_argument('-seed', help=' : Set seed of random(or numpy.random) Module, default=42', default=42)
parser.add_argument('-Q_0', help=' : Set initial asset Q_0, default=10', default=10)
args=parser.parse_args()


def get_N_end_using_random(my_seed=42, Q_0=10):
    import random as rd
    rd.seed(my_seed)
    N_end = 0
    
    while (Q_0 > 0):
        r = rd.random()
        if (r < 1/3):
            Q_0 += -1
        elif (r > 2/3):
            Q_0 += 1

        N_end += 1
    
    return N_end

def main(argv, args):
    start_time = time.time()
    N_end = get_N_end_using_random(int(args.seed), int(args.Q_0))
    end_time = time.time()
    duration = end_time - start_time
    print(f"{int(args.Q_0)}, {N_end}, {duration}")


if __name__ == '__main__':
    argv = sys.argv
    main(argv ,args)