import os
import random

def draw_random_files(folder, nb_sample, seed = 42):
    rng   = random.seed(seed)
    files = []
    # Start exploration of the directory structure and files
    for root, dirs, in_files in os.walk(folder):
        for f in in_files:
            files.append(os.path.join(root, f))

    if nb_sample > len(files):
        print("Not enough files")
        return None

    return random.sample(files, nb_sample)


