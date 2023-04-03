from importer import reader
import grasp_algorithm
import sys

if __name__ == '__main__':

    if len(sys.argv[1]) <= 3:
        print('Verifique os argumentos', file=sys.stderr)

    # Print the command-line arguments
    file = sys.argv[1]
    print(file)

    sequence = reader.read_dat_file(file)
    print(sequence)
    k = 3
    max_iter = 1000000
    resolution = grasp_algorithm.grasp(sequence, max_iter, k)
    print(resolution)
