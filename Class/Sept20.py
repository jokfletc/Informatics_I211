#write program looks and finds total size
#of all the file in directory but don't look atfiles
#directory but look at directory in directory and look at
#files within these many step of directory
#use recurrsive to find directroy
#start at zero if file is file find size and add to
#zero but if directory recursive


def file_space(user_file):
    file_bytes = 0
    for content in os.listdir(user_file):
        if os.path.isfile(content)
        file_bytes += os.path.getsize(content)
        elif os.path.isdir(content):
            
                
        
