import os

def split_file(filepath, chunk_size=15 * 1024 * 1024):  # 15MB chunks
    if not os.path.exists(filepath):
        print(f"ERROR: File '{filepath}' not found.")
        return
    
    filename = os.path.basename(filepath)
    file_size = os.path.getsize(filepath)
    print(f"Splitting '{filename}' ({file_size / (1024*1024):.2f} MB)...")
    
    with open(filepath, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            # This creates the .part files in the same folder as the original
            output_name = f"{filepath}.part{part_num}"
            with open(output_name, 'wb') as output_file:
                output_file.write(chunk)
            
            print(f"   Created: {os.path.basename(output_name)}")
            part_num += 1
    print(f"Done: {filename} -> {part_num - 1} parts.\n")

if __name__ == "__main__":
    # The exact path you provided
    build_folder = r"C:\Users\MSI\Downloads\pet world\Build"
    
    # Filenames from your Pet World screenshot
    files_to_split = [
        "pet-world[16]-mirraSDK[4.3.39].data",
        "pet-world[16]-mirraSDK[4.3.39].wasm"
    ]
    
    for file_name in files_to_split:
        full_path = os.path.join(build_folder, file_name)
        split_file(full_path)
        
    print("All tasks complete. Check your 'Build' folder for the .part files.")