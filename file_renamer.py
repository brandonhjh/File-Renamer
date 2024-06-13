import os

def rename_jpeg_files(folder_path):
    # Get a list of all jpeg files in the folder
    jpeg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')]
    
    # Sort the files
    jpeg_files.sort()
    
    # Rename files
    for idx, filename in enumerate(jpeg_files, start=1):
        # Define the new filename
        new_filename = f"{idx}.jpeg"
        
        # Get full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{old_file}' to '{new_file}'")

# Specify the folder path
folder_path = '/Users/brandonhong/Desktop/GII/Wivisites/Task 8 - Marketing Collage/chosen pics'

# Call the function
rename_jpeg_files(folder_path)
