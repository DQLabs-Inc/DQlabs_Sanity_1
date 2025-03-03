import os
import zipfile

# Set project folder path (Update as needed)
project_folder = "/Users/saivamsi/Downloads/DQlabs_Sanity_QA-main"

# Ensure the ZIP file is stored outside the project folder
zip_file_name = "DQlabs_Sanity3.zip"
zip_file_path = os.path.join(os.path.dirname(project_folder), zip_file_name)

# List of folders & extensions to exclude
EXCLUDE_FOLDERS = {"__pycache__", ".git", ".venv", "node_modules", "logs", "dist", ".idea"}
EXCLUDE_EXTENSIONS = {".zip", ".log", ".mp4", ".png", ".jpg", ".DS_Store"}


def should_exclude(file_path):
    """Returns True if the file should be excluded based on folder or extension."""
    for folder in EXCLUDE_FOLDERS:
        if folder in file_path:
            return True
    if os.path.splitext(file_path)[1] in EXCLUDE_EXTENSIONS:
        return True
    return False


# Remove old ZIP file if it exists (to prevent recursive size increase)
if os.path.exists(zip_file_path):
    os.remove(zip_file_path)
    print(f"🗑️ Removed old ZIP: {zip_file_path}")

# Create a new ZIP file with compression
with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_folder):
        # Remove excluded folders from search
        dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]

        for file in files:
            file_path = os.path.join(root, file)
            if not should_exclude(file_path):  # Only add allowed files
                zipf.write(file_path, os.path.relpath(file_path, project_folder))

print(f"✅ Compressed project saved as: {zip_file_path}")

#python zip_project.py
