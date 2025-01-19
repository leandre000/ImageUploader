
# Image Monitor and Uploader

This Python script automates the process of monitoring a folder, uploading images to a server, and organizing the uploaded images in a separate folder.

## Features
- **Folder Monitoring**: Watches a specified folder for new images.
- **Automated Upload**: Uploads images to a specified server URL every 30 seconds using the `curl` command.
- **File Organization**: Moves successfully uploaded images to a separate folder to avoid redundancy.

---

## Prerequisites
- Python 3.6 or higher
- `curl` installed on your system

---

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/image-monitor-uploader.git
   cd embedded
   ```

2. **Install Required Libraries**:
   This script uses built-in Python libraries, so no additional installations are required.

3. **Verify `curl` Installation**:
   Ensure `curl` is installed and available in your system's PATH. To check:
   ```bash
   curl --version
   ```

---

## Configuration

1. Update the following variables in the `imagesUploader.py` file:

   - `monitor_folder`: Path to the folder where your camera saves images.
   - `uploaded_folder`: Path to the folder where successfully uploaded images will be moved.
   - `upload_url`: The server URL to upload the images (provided in the assignment).

   Example:
   ```python
   monitor_folder = r"C:\Users\YourUsername\Pictures\CameraImages"
   uploaded_folder = r"C:\Users\YourUsername\Pictures\UploadedImages"
   upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
   ```

---

## Usage

1. Run the script:
   ```bash
   python imagesUploader.py
   ```

2. The script will:
   - Continuously monitor the `monitor_folder`.
   - Upload each image found to the specified server URL.
   - Move successfully uploaded images to the `uploadedImages`.

3. Check the console output for upload status messages.

---

## Example Output
```plaintext
Starting to monitor the folder...
Successfully uploaded: C:\Users\YourUsername\Pictures\CameraImages\image1.jpg
Successfully uploaded: C:\Users\YourUsername\Pictures\CameraImages\image2.jpg
Failed to upload C:\Users\YourUsername\Pictures\CameraImages\image3.jpg: Server error
```

---

## Folder Structure
```
embedded/
│
├── imagesUploader.py               # The main Python script
├── uploadedImages          # This stores the uploaded images
```

---

## Troubleshooting

- **Folder Not Found**: Ensure the `monitor_folder` exists and contains the images to upload.
- **Failed Uploads**: Check your internet connection and ensure the `upload_url` is correct.
- **curl Errors**: Verify that `curl` is installed and properly configured on your system.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
