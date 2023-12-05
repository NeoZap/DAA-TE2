import random


def generate_random_tree(num_vertices):
    cur_vertex = 1
    N = num_vertices[1]
    adj_list = [[] for _ in range(N)]

    for i in range(1, N + 1):
        vertices_left = N - cur_vertex
        lower_bound, upper_bound = 1, 15
        num_child = min(vertices_left, random.randrange(lower_bound, upper_bound + 1))
        adj_list[i - 1] = [
            child for child in range(cur_vertex + 1, cur_vertex + num_child + 1)
        ]
        cur_vertex += num_child

    output_bnb = f"{num_vertices[0]} {num_vertices[0] - 1} 0\n"
    for i in range(num_vertices[0]):
        nodes = [node for node in adj_list[i] if node <= num_vertices[0]]
        output_bnb += " ".join(map(str, nodes)) + "\n"

    output_dp = f"{num_vertices[1]} {num_vertices[1] - 1} 0\n"
    for nodes in adj_list:
        output_dp += " ".join(map(str, nodes)) + "\n"

    return output_bnb, output_dp


NUM_VERTICES = [
    (100, 10**4),
    (300, 10**5),
    (900, 10**6),
]
random.seed(42)

for num_vertices in NUM_VERTICES:
    output_bnb, output_dp = generate_random_tree(num_vertices)

    bnb_filename = f"Data/truncated_random_{num_vertices[0]}.tree"
    with open(bnb_filename, "w") as file:
        file.write(output_bnb)
        print(
            f"Random tree with {num_vertices[0]} vertices generated and saved to '{bnb_filename}'"
        )

    dp_filename = f"Data/raw_random_{num_vertices[1]}.tree"
    with open(dp_filename, "w") as file:
        file.write(output_dp)
        print(
            f"Random tree with {num_vertices[1]} vertices generated and saved to '{dp_filename}'"
        )
