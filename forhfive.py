import h5py

# Replace 'your_file.h5' with the actual filename
with h5py.File('lstm-model-first.h5', 'r') as hdf_file:
    # Your code to access data in the file goes here
    # For example, get information about the file contents
    print("List of keys (dataset names):", list(hdf_file.keys()), hdf_file['optimizer_weights'])