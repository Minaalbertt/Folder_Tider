import time
import sys
import schedule
import threading
import os
from pathlib import Path
import logging

# Constants
FILE_TYPES = {
    'IMAGES': {'jpg', 'png', 'gif', 'jpeg', 'ico'},
    'AUDIO': {'mp3', 'wav', 'flac'},
    'VIDEOS': {'mp4', 'avi', 'mkv', 'webm'},
    'SHEETS': {'xls', 'xlsx', 'gsheet'},
    'DOCS': {'doc', 'docx', 'gdoc'},
    'BOOKS': {'pdf', 'epub', 'mobi'},
    'ARCHIVES': {'zip', 'tar', 'rar'},
    'DATABASES': {'db', 'sql', 'csv', 'json', 'tsv'},
    'OTHER_DOCS': {'txt', 'md', 'ppt', 'pptx'},
    'PYTHON': {'py', 'pyw', 'ipynb'},
    'JAVASCRIPT': {'js'},
    'HTML': {'html', 'htm'},
    'APPS': {'exe', 'msi', 'bat'},
    'FONTS': {'ttf', 'otf', 'woff', 'woff2'},
}

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_folder_path(folder_path: str) -> Path:
    """Validate the provided folder path."""
    if not folder_path:
        logging.error("Error: Please provide a folder path as an argument.")
        sys.exit(1)
    
    path = Path(folder_path)
    if not path.exists():
        logging.error(f"Error: The folder '{folder_path}' does not exist.")
        sys.exit(1)
    
    return path

def create_folder_if_not_exists(folder_path: Path) -> None:
    """Create a folder if it does not exist."""
    if not folder_path.exists():
        folder_path.mkdir()

def move_file(file: Path, target_folder: Path) -> None:
    """Move a file to the target folder."""
    try:
        os.rename(file, target_folder / file.name)
    except FileExistsError:
        filename = file.stem
        new_filename = f"{filename}(1){file.suffix}"
        os.rename(file, target_folder / new_filename)
    except Exception as e:
        logging.error(f"Error moving file {file.name}: {e}")

def organize_files(folder_path: Path) -> None:
    """Organize files in the specified folder."""
    for file in folder_path.iterdir():
        if file.name == 'desktop.ini':
            continue
        
        if file.is_file():
            file_ext = file.suffix[1:].lower()
            if not file_ext:
                move_file(file, folder_path / 'OTHERS')
                continue
            
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = folder_path / folder_name
                    create_folder_if_not_exists(target_folder)
                    move_file(file, target_folder)
                    moved = True
                    break
            
            if not moved:
                move_file(file, folder_path / 'OTHERS')
        
        elif file.is_dir():
            # Skip if the folder is already a target folder (e.g., 'Folders', 'IMAGES', etc.)
            if file.name in FILE_TYPES.keys() or file.name in ['OTHERS', 'Folders']:
                continue
            
            try:
                # Create the 'Folders' directory if it doesn't exist
                target_folder = folder_path / 'Folders'
                create_folder_if_not_exists(target_folder)
                
                # Move the folder into the 'Folders' directory
                move_file(file, target_folder)
            except Exception as e:
                logging.error(f"Error moving folder {file.name}: {e}")

def organize() -> None:
    """Main function to organize the folder."""
    if len(sys.argv) < 2:
        logging.error("Error: Please provide a folder path as an argument.")
        sys.exit(1)
    
    folder_path = validate_folder_path(sys.argv[1])
    organize_files(folder_path)
    logging.info('Done!')

if __name__ == '__main__':
    organize()
