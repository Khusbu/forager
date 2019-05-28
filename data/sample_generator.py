import random
import sys


def get_datapoints(filename):
    fr = open(filename, 'r', encoding="ISO-8859-1")
    datapoints = fr.read().split('\n\n')
    fr.close()

    return datapoints


def generate_sample_file(filepath, sample_size=10**4):
    datapoints = get_datapoints(filepath)
    # name should be finefoods.txt as it is being used in app for creating indexes
    sample_filename = 'finefoods.txt'
    fw = open(sample_filename, 'w')

    for _ in range(sample_size):
        # possibility of sampling a review more than once.
        index = random.randint(0, len(datapoints))
        fw.write(datapoints[index])
        fw.write('\n\n')
    fw.close()

    return sample_filename


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python sample_generator.py <filepath> <sample_size>")
        exit(1)

    filepath, sample_size = sys.argv[1], int(sys.argv[2])
    sample_filename = generate_sample_file(filepath, sample_size)
    print('Sample file stored in', sample_filename)