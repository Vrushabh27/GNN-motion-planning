
'''
Analyzing pickle data located in "data/pkl/snake_prm_3000.pkl"

Author: Shrenik Zinage
Date: 2024-02-25
'''
import pickle
import numpy as np

# Path to the pickle file
data_path = 'data/pkl/snake_prm_3000.pkl'

# Function to print the contents of a specific tuple by index, limiting dictionary output
def print_tuple_contents(lst, index, num_keys=5):
    if index < 0 or index >= len(lst):
        print("Index out of range.")
        return
    
    tuple_element = lst[index]
    print(f"Details of tuple at index {index}:")
    for i, element in enumerate(tuple_element):
        element_type = type(element)
        print(f"\nElement {i}: Type = {element_type}")
        
        if isinstance(element, np.ndarray):
            print(f"  Shape: {element.shape}")
            print("  Contents:", element)
        elif isinstance(element, dict):
            print(f"  Number of keys: {len(element)}")
            print("  First few key-value pairs:")
            for j, (key, value) in enumerate(element.items()):
                if j >= num_keys: break  # Limit the number of printed keys
                print(f"    Key: {key}, Value: {value}")
        elif isinstance(element, list):
            print(f"  Length: {len(element)}")
            print("  Contents:", element[:num_keys])  # Limit the list content shown
        # Add handling for other types if necessary

# Load the data
with open(data_path, 'rb') as file:
    loaded_data = pickle.load(file)

# Ensure the loaded data is a list and proceed with printing contents of a specific tuple
if isinstance(loaded_data, list):
    # Example: Print contents for the tuple at index 0, showing only the first few keys in dictionaries
    print_tuple_contents(loaded_data, 0)
else:
    print("Loaded data is not a list of tuples.")
