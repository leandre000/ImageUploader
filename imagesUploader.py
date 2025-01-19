import os
import time
import shutil
import subprocess

# Configuration
monitor_folder = r"C:\Users\Shema Leandre\Pictures\coffeee"  # Use raw string to handle Windows paths
uploaded_folder = r"C:\Users\Shema Leandre\Downloads\embedded\uploadedImages"  # Use raw string for the target folder
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

def upload_image(file_path):
    try:
        # Use the curl command to upload the image
        result = subprocess.run(
            ["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", upload_url],
            capture_output=True, text=True
        )
        if result.returncode == 0 and "success" in result.stdout.lower():
            print(f"Successfully uploaded: {file_path}")
            return True
        else:
            print(f"Failed to upload {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
        return False

def monitor_and_upload():
    while True:
        # List all files in the folder
        files = [f for f in os.listdir(monitor_folder) if os.path.isfile(os.path.join(monitor_folder, f))]
        for file in files:
            file_path = os.path.join(monitor_folder, file)
            
            # Upload the image
            if upload_image(file_path):
                # Move the uploaded file to another folder
                shutil.move(file_path, os.path.join(uploaded_folder, file))
        
        # Wait 30 seconds before checking again
        time.sleep(30)

if __name__ == "__main__":
    # Ensure the folders exist
    if not os.path.exists(monitor_folder):
        print(f"Error: Monitoring folder does not exist: {monitor_folder}")
        exit(1)
    if not os.path.exists(uploaded_folder):
        os.makedirs(uploaded_folder)

    # Start monitoring and uploading
    print("Starting to monitor the folder...")
    monitor_and_upload()
