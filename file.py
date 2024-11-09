def file_add_end(file: str, what='', mode: str = 'a+', encode: str = 'utf-8'):
    with open(file, mode, encoding=encode) as f:
        f.write(what)
        try:
            return f.read()
        except Exception as e:
            pass
    
def kill_file(kills: list[str] | str):
    import os
    
    if type(kills) == str:
       os.remove(kills)
       return
    for file in kill_list:
        os.remove(file)
