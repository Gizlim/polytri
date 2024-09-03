import matplotlib.pyplot as plt
import csv

# Lists to store the coordinates of the triangles
triangles = []

# Read the triangle data from the CSV file
with open('triangles.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        v0_x, v0_y = float(row[0]), float(row[1])
        v1_x, v1_y = float(row[2]), float(row[3])
        v2_x, v2_y = float(row[4]), float(row[5])
        triangles.append([(v0_x, v0_y), (v1_x, v1_y), (v2_x, v2_y)])

# Plot the triangles
plt.figure()
for triangle in triangles:
    # Extracting x and y coordinates
    xs = [v[0] for v in triangle] + [triangle[0][0]]  # Close the triangle
    ys = [v[1] for v in triangle] + [triangle[0][1]]  # Close the triangle
    plt.plot(xs, ys)  # 'b-' is blue solid line

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Polygon Triangulation")
plt.grid(True)
plt.axis('equal')  # To maintain aspect ratio
plt.show()
