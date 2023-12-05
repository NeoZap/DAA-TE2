import os

NUM_VERTICES = [
    (100, 10**4),
    (300, 10**5),
    (900, 10**6),
]

for num_vertices in NUM_VERTICES:
    bnb_filename = f"Data/truncated_random_{num_vertices[0]}.tree"
    os.system(f"py BnB_Edited.py -inst {bnb_filename}")

    dp_filename = f"Data/raw_random_{num_vertices[1]}.tree"
    os.system(f"py dp.py {dp_filename}")
