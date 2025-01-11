import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def simulate_random_walk(num_steps, num_simulations, plot_every):
    """
    Simulates multiple random walks and plots them
    Parameters:
        num_steps: number of steps for each walk
        num_simulations: number of walks to simulate
        plot_every: plot every nth simulation
    Returns:
        List of final positions for each walk
    """
    paths = []
    max_distances = []
    avg_step_sizes = []

    for sim in range(num_simulations):
        x, y = [0], [0]
        step_sizes = []
        max_dist = 0

        for _ in range(num_steps):
            dx = np.random.normal(0, 1)
            dy = np.random.normal(0, 1)
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)

            step_size = np.sqrt(dx ** 2 + dy ** 2)
            step_sizes.append(step_size)

            current_dist = np.sqrt(x[-1] ** 2 + y[-1] ** 2)
            max_dist = max(max_dist, current_dist)

        paths.append((x, y))
        if sim % plot_every == 0:
            plt.plot(x, y, '-', alpha=0.5)

        avg_step = np.mean(step_sizes)
        max_distances.append(max_dist)
        avg_step_sizes.append(avg_step)

    final_x = sum(paths[i][0][-1] for i in range(num_simulations))
    final_y = sum(paths[i][1][-1] for i in range(num_simulations))

    center_x = final_x / num_simulations
    center_y = final_y / num_simulations

    center_distance = np.sqrt(center_x ** 2 + center_y ** 2)

    final_distances = [np.sqrt(paths[i][0][-1] ** 2 + paths[i][1][-1] ** 2)
                       for i in range(num_simulations)]

    print("\nStatistici pentru Random Walk:")
    print(f"Poziția medie finală: ({center_x:.2f}, {center_y:.2f})")
    print(f"Distanța centrului de masă față de origine: {center_distance:.2f}")
    print(f"Distanța maximă medie: {np.mean(max_distances):.2f}")
    print(f"Mărimea medie a pasului: {np.mean(avg_step_sizes):.2f}")
    print(f"Deviația standard a distanțelor finale: {np.std(final_distances):.2f}")

    plt.grid(True)
    plt.title(f'Random Walks (n={num_simulations})')

    final_positions_x = [paths[i][0][-1] for i in range(num_simulations)]
    final_positions_y = [paths[i][1][-1] for i in range(num_simulations)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.hist(final_positions_x, bins=30, alpha=0.7)
    ax1.set_title('Final X values')
    ax1.set_xlabel('X value')
    ax1.set_ylabel('Frequency')

    ax2.hist(final_positions_y, bins=30, alpha=0.7)
    ax2.set_title('Final Y values')
    ax2.set_xlabel('Y value')
    ax2.set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()

    return paths


# Example usage:
simulate_random_walk(100, 10000, 100)
