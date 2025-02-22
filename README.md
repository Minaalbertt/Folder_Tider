### Folder Tider:
- If your folder have many and random files and looks bad
- My app tide your folder to folder for (APPS, VIDEOS, ARCHIVES , IMAGES, DATABASES , BOOKS , FOLDERS, Others , ...)
---
#### How to run:
- Firstly you should installed python in your device (Soon. I will convert this python file to real app) and install requirements  <code>pip install -r requirements.txt</code>
- After that you should download this files to your local device and extarct zip file
- After that you should write in bash (cmd , powershell)
  ```batch
  python "FolderTiderPath\Folder_Tider_CMD.py" "FolderPathThatYouWantToTideIt"
  ```
- Example command:
  ```batch
  python "C:\FolderTider\Folder_Tider_CMD.py" "D:\Downloads"
   ```
---
#### Note:
> If you want to make this file shedule to any file you can uncomment:
> 
> <code batch># schedule.every(1).minutes.do(organize_files,dic)
        # here ↑
        # if __name__ == '__main__':
        #     schedule.run_pending()
        #     time.sleep(1)</code>
> From line 76 to line 80
>
> After that you should also in line 7 <code>dic = sys.argv[1]</code> replace <code>sys.argv[1]</code> to your folder path for example <code>dic = 'D:\Downloads' #my folder path</code>


---

### Setting Up a Python Script as a System-Wide Command via Batch File

To make your Python script accessible as a system-wide command, you can create a batch (`.bat`) file and add it to your system's `PATH`. Follow these steps:

---

### Step 1: Create a Batch File

1. Open a text editor (e.g., Notepad) and paste the following script:

   ```batch
   @echo off
   python "pyfilePath" %*
   ```

   Replace `"pyfilePath"` with the full path to your Python script (e.g., `C:\path\to\your_script.py`).

2. Save the file with a `.bat` extension, for example, `run_script.bat`.

---

### Step 2: Add the Batch File to the System `PATH`

1. Move the `.bat` file to a dedicated folder, for example:
   ```
   C:\Scripts
   ```

2. Add the folder containing the `.bat` file to your system's `PATH` environment variable:
   - Press `Win + R`, type `sysdm.cpl`, and press Enter.
   - Go to the **Advanced** tab and click **Environment Variables**.
   - Under **System Variables**, find the `Path` variable and click **Edit**.
   - Add the folder path (e.g., `C:\Scripts`) to the list.
   - Click **OK** to save the changes.

---

### Step 3: Verify the Setup

1. Open a new Command Prompt window.
2. Type the name of your batch file (without the `.bat` extension) and press Enter. For example:
   ```
   run_script
   ```
   If everything is set up correctly, your Python script should execute.

---

### Notes
- Ensure Python is installed and added to your system `PATH` for this to work.
- You can now run your Python script from any directory in the Command Prompt by simply typing the batch file name.

---
