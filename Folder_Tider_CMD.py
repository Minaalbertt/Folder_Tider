#start of import functions ↓↓
import time,sys,schedule,threading,os
from pathlib import Path

def organize():
    # to get the directly from the entry 
        dic = sys.argv[1]
    
        

    # try:
        # dic to store the correct files in them correct folders 
        file_type = {
        'IMAGES': 'jpg, png, gif, jpeg, ico',
        'AUDIO': 'mp3, wav, flac',
        'VIDEOS': 'mp4, avi, mkv, webm',
        'SHEETS': 'xls, xlsx, gsheet',
        'DOCS': 'doc, docx, gdoc',
        'BOOKS': 'pdf, epub, mobi',
        'ARCHIVES': 'zip, tar, rar',
        'DATABASES': 'db, sql, csv, json, tsv',
        'OTHER_DOCS': 'txt, md, ppt, pptx',
        'PYTHON': 'py, pyw, ipynb',
        'JAVASCRIPT': 'js',
        'HTML': 'html, htm',
        'APPS': 'exe, msi ,bat',
        }
        # to organize files and move it to them folders 
        def organize_files(dic):
            # convert dic to path 
            path = Path(dic)
            # to move files in them folders
            def move(folder):
                try:
                    folder_dic = path / folder
                       
                    if not folder_dic.exists():
                        folder_dic.mkdir()
                    
                    os.rename(file,os.path.join(folder_dic,file.name))
                except:
                    filename = file.stem
                    os.rename(file,os.path.join(folder_dic,filename+'(1)'+file_ext))

            # to list the files and store it to them folders 
            for file in path.iterdir():
                # to check files if it files or folders 
                if file.name == 'desktop.ini':
                    continue
                if file.is_file():
                    # to store file ext
                    file_ext = file.suffix[1:]
                    if file_ext == '' or file_ext == ' ':
                        move('OTHERS')
                        break
                    # to store the items of file_type dic in key and value 
                    for key, value in file_type.items():
                        # to move files in them correct folders 
                        if file_ext in value:
                            move(key)
                            break
                    # If the ext of the files not in value of keys it will move it to "OTHERS" folder 
                    else:
                        move('OTHERS')
            
                if file.is_dir() and file.name not in list(file_type.keys()) and file.name not in ['OTHERS'] :
                        try:
                            move('Folders')
                        except:
                            pass                      
        # to run the function 
        organize_files(dic)
        # to know the users the program has organized the folder 
        print('Done!')
        # to organize the folder every one minute 
        # schedule.every(1).minutes.do(organize_files,dic)
        # here ↑
        # if __name__ == '__main__':
        #     schedule.run_pending()
        #     time.sleep(1)
organize()
