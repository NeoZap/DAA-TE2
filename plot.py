import matplotlib.pyplot as plt


def plot_performance(ax, x_values, y_values, function_name, y_label, title, color=None):
    ax.plot(x_values, y_values, label=function_name, color=color)
    ax.set_xlabel("Size of N")
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()


def generate_plots(input_sizes, times, memory_usages, function):
    _, axes = plt.subplots(2, 2, figsize=(12, 8))

    plot_performance(
        axes[0, 0],
        input_sizes[0],
        times[0],
        function[0],
        "Running Time (s)",
        "Dynamic Programming MVC",
    )
    plot_performance(
        axes[0, 1],
        input_sizes[1],
        times[1],
        function[1],
        "Running Time (s)",
        "Branch and Bound MVC",
        color="red",
    )
    plot_performance(
        axes[1, 0],
        input_sizes[0],
        memory_usages[0],
        function[0],
        "Memory Usage (bytes)",
        "Dynamic Programming MVC",
    )
    plot_performance(
        axes[1, 1],
        input_sizes[1],
        memory_usages[1],
        function[1],
        "Memory Usage (bytes)",
        "Branch and Bound MVC",
        color="red",
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    function = ["DP", "BnB"]
    input_sizes = [[10**4, 10**5, 10**6], [100, 300, 900]]
    memory_usages = [[969202, 9607124, 96464526], [101472, 274237, 1610242]]
    times = [[0.03, 0.31, 3.23], [0.004, 0.02, 153.31]]

    generate_plots(input_sizes, times, memory_usages, function)
