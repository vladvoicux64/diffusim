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


def animate_single_particle():
    """
    Animates a single particle's random walk in real-time
    """
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot([], [], 'b-')
    point, = ax.plot([], [], 'ro')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)

    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point

    def update(frame):
        dx = np.random.normal(0, 0.5)
        dy = np.random.normal(0, 0.5)

        if x_data:
            x_data.append(x_data[-1] + dx)
            y_data.append(y_data[-1] + dy)
        else:
            x_data.append(0)
            y_data.append(0)

        line.set_data(x_data, y_data)
        point.set_data([x_data[-1]], [y_data[-1]])
        return line, point

    anim = FuncAnimation(fig, update, init_func=init, frames=200,
                         interval=50, blit=True)
    plt.show()


def simulate_particle_collisions(num_particles=20, max_collisions=10):
    """
    Simulates multiple particles with collisions and tracks one particle
    """

    class Particle:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dx = np.random.normal(0, 0.5)
            self.dy = np.random.normal(0, 0.5)

    def elastic_collision(p1, p2):
        nx = p2.x - p1.x
        ny = p2.y - p1.y
        dist = np.sqrt(nx * nx + ny * ny)
        if dist == 0: return
        nx /= dist
        ny /= dist

        v1n = p1.dx * nx + p1.dy * ny
        v2n = p2.dx * nx + p2.dy * ny

        p1.dx += (v2n - v1n) * nx
        p1.dy += (v2n - v1n) * ny
        p2.dx += (v1n - v2n) * nx
        p2.dy += (v1n - v2n) * ny

    particles = [Particle(np.random.uniform(-10, 10), np.random.uniform(-10, 10))
                 for _ in range(num_particles)]
    tracked_particle = particles[0]
    collision_count = 0

    fig, ax = plt.subplots()
    tracked_path_x, tracked_path_y = [], []
    tracked_line, = ax.plot([], [], 'b-', alpha=0.5)
    particles_scatter = ax.scatter([], [], c='blue')
    tracked_point = ax.scatter([], [], c='red', s=100)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)

    def init():
        tracked_line.set_data([], [])
        particles_scatter.set_offsets(np.empty((0, 2)))
        tracked_point.set_offsets(np.empty((0, 2)))
        return tracked_line, particles_scatter, tracked_point

    def update(frame):
        nonlocal collision_count
        if collision_count >= max_collisions:
            return tracked_line, particles_scatter, tracked_point

        for p in particles:
            p.x += p.dx
            p.y += p.dy

            if abs(p.x) > 10:
                p.dx *= -1
                p.x = np.sign(p.x) * 10
            if abs(p.y) > 10:
                p.dy *= -1
                p.y = np.sign(p.y) * 10

        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                p1, p2 = particles[i], particles[j]
                dist = np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
                if dist < 0.5:
                    elastic_collision(p1, p2)
                    if p1 is tracked_particle or p2 is tracked_particle:
                        collision_count += 1

        tracked_path_x.append(tracked_particle.x)
        tracked_path_y.append(tracked_particle.y)

        tracked_line.set_data(tracked_path_x, tracked_path_y)

        all_positions = np.array([[p.x, p.y] for p in particles])
        particles_scatter.set_offsets(all_positions)
        tracked_point.set_offsets([[tracked_particle.x, tracked_particle.y]])

        return tracked_line, particles_scatter, tracked_point

    anim = FuncAnimation(fig, update, init_func=init, frames=1000,
                         interval=50, blit=True)
    plt.show()


# Example usage:
simulate_random_walk(100, 10000, 100)
# simulate_random_walk(100, 10000, 100)
animate_single_particle()
# animate_single_particle()
simulate_particle_collisions(100, 100)
