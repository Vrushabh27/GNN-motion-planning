import numpy as np
from scipy.io import loadmat
from collections import defaultdict

# Function to load the data and convert it
def load_and_convert(filename):
    # Load the MATLAB file
    data = loadmat(filename)
    # Assuming 'all_k_nearest_neighbors' is the variable name in the MATLAB file
    neighbors_matrix = data['all_k_nearest_neighbors']
    
    # Convert to Python 0-based indexing if MATLAB indexing is 1-based
    neighbors_matrix = neighbors_matrix - 1
    
    # Initialize defaultdict
    neighbors_dict = defaultdict(list)
    
    # Populate the defaultdict with the data
    for idx, neighbors in enumerate(neighbors_matrix):
        neighbors_dict[idx] = neighbors.tolist()
    
    return neighbors_dict

def format_node_gnn(node_gnn):
    # Convert node_gnn to a NumPy array if it's not already one
    node_gnn_array = np.array(node_gnn)
    
    # Check if the conversion was successful and the shape is as expected (1200 nodes, 6 dimensions)
    if node_gnn_array.ndim == 2 and node_gnn_array.shape[1] == 6:
        print(f"Element 0: Type = {type(node_gnn_array)}")
        print(f"  Shape: {node_gnn_array.shape}")
        print("  Contents:")
        print(node_gnn_array)
    else:
        print("The input does not match the expected format of 1200 nodes with 6 dimensions each.")

# Load the .mat file
data = loadmat('nodes.mat', squeeze_me=True, struct_as_record=False)

# Access the 'node_gnn' variable, ensuring it's correctly indexed
node_gnn = data['node_gnn']

# Preallocate a NumPy array to hold the 6-dimensional values for 1200 nodes
node_values = np.zeros((1200, 6))

# Loop through each node to extract its 'v' value
for j in range(1200):
    # Assuming 'v' is directly accessible and properly structured
    node_values[j, :] = node_gnn[j].v  # Adjust if 'v' needs specific indexing
node_numpy=format_node_gnn(node_values)

# Load the data and convert it
filename = 'neighbors.mat'
neighbors_dict = load_and_convert(filename)

# Display the required information
print(f"Type = {type(neighbors_dict)}")
print(f"Number of keys: {len(neighbors_dict)}")
print("First few key-value pairs:")
for i, (key, value) in enumerate(neighbors_dict.items()):
    if i < 50:  # Adjust this number to display more or fewer key-value pairs
        print(f"  Key: {key}, Value: {value}")
    else:
        break


# Calculate the total number of edges
total_edges = sum(len(neighbors) for neighbors in neighbors_dict.values())

# Initialize the edge_index array
edge_index = np.zeros((total_edges, 2), dtype=int)

# Populate the edge_index array
edge_counter = 0
for node, neighbors in neighbors_dict.items():
    for neighbor in neighbors:
        edge_index[edge_counter] = [node, neighbor]
        edge_counter += 1

# Displaying the requested information
print(f"Element 3: Type = {type(edge_index)}")
print(f"  Shape: {edge_index.shape}")
print("  Contents:")
print(edge_index[:5], "\n ...")  # Display first 5 for brevity
print(edge_index[-3:], "\n")  # Display last 3 to show the structure continues as described
