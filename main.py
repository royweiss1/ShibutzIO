import matplotlib.pyplot as plt

def plot_shape_outline(outline):
    # Extract x and y coordinates from the outline
    x_coords = [point[0] for point in outline]
    y_coords = [point[1] for point in outline]

    # Plot the shape outline
    plt.plot(x_coords, y_coords, 'b-')
    plt.scatter(x_coords, y_coords, color='r')

    # Set the axis labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Shape Outline')

    # Show the plot
    plt.show()
from scipy.spatial import ConvexHull

def get_shape_outline(positions):
    # Compute the Convex Hull
    hull = ConvexHull(positions)

    # Get the vertices and edges of the Convex Hull
    vertices = hull.points[hull.vertices]
    edges = []
    for simplex in hull.simplices:
        edges.extend([(hull.points[simplex[i]], hull.points[simplex[(i+1) % len(simplex)]]) for i in range(len(simplex))])

    # Create the shape outline using the vertices and edges
    outline = []
    for vertex in vertices:
        outline.append(vertex)
    for edge in edges:
        outline.extend([point for point in edge])

    return outline

# Example usage
positions = [(1, 1), (3, 5), (6, 3), (8, 7), (4, 9), (2, 6)]
outline = get_shape_outline(positions)
plot_shape_outline(outline)
print(outline)