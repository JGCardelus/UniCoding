import os
import subprocess
import pyscreenshot as ImageGrab

loc = os.path.join(os.getcwd(), "programs")
photos = os.path.join(os.getcwd(), "photos")

def is_c_program(name):
    name_chunks = name.split(".")
    extension = name_chunks[len(name_chunks)- 1]

    if extension == "c":
        return True

    return False

def hacer_practica(location):
    os.chdir(location)

    for root, folder, files in os.walk("."):
        for i, file_ in enumerate(files):
            print(file_)
            if is_c_program(file_):
                hacer_ejercicio(file_, i)

def remove_extension(name):
    name_chunks = name.split(".")
    name_chunks.pop()
    no_ext_name = "".join(name_chunks)

    return no_ext_name

def execute(sentence):
    p = subprocess.Popen(sentence.split(),
                     stdout=subprocess.PIPE)
    preprocessed, _ = p.communicate()
    return preprocessed.decode('utf-8')

def hacer_ejercicio(file_, i):
    # Compilar
    no_ext_file = remove_extension(file_)
    execute("gcc -I /usr/include/mysql %s -L /usr/lib/mysql -lmysqlclient -o %s" % (file_, no_ext_file))
    execute("gcc -o %s $(mysql_config --cflags) %s $(mysql_config --libs)" % (no_ext_file, file_))

    resp = execute("./%s" % (no_ext_file))
    print(resp)

    # grab fullscreen
    os.chdir(photos)
    im = ImageGrab.grab()
    im.save('%s.png' % (no_ext_file))
    os.chdir(loc)

hacer_practica(loc)

