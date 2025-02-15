# Folder_Tider
Tide your folder and make it tidy
- If your folder have many and random files and looks bad
- My app tide your folder to folder for (APPS, VIDEOS, ARCHIVES , IMAGES, DATABASES , BOOKS , FOLDERS, Others , ...)
#### How to run:
- Firstly you should installed python in your device (Soon. I will convert this python file to real app)
- After that you should download this files to your local device and extarct zip file
- After that you should write in bash (cmd , powershell) <code>python "FolderTiderPath\Folder_Tider_CMD.py" "FolderPathThatYouWantToTideIt"</code>
- Example command: <code>python "C:\FolderTider\Folder_Tider_CMD.py" "D:\Downloads"</code>
#### Note:
> If you want to make this file shedule to any file you can uncomment:
> 
> <code># schedule.every(1).minutes.do(organize_files,dic)
        # here ↑
        # if __name__ == '__main__':
        #     schedule.run_pending()
        #     time.sleep(1)</code>
> From line 76 to line 80
>
> After that you should also in line 7 <code>dic = sys.argv[1]</code> replace <code>sys.argv[1]</code> to your folder path for example <code>dic = 'D:\Downloads' #my folder path</code>
