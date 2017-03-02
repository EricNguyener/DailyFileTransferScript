import os, shutil
from os import path
import datetime
from datetime import date, time, timedelta

# Source and destination

src = "C:\Users\Thien Nguyen\Desktop\A"
dst = "C:\Users\Thien Nguyen\Desktop\B"

def file_modified(fname):
    print str(path.getmtime(fname))
    
# Modification time
    file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))

    print datetime.datetime.now()
    print file_m_time

# Different between today and file modification time

    tdelta = datetime.datetime.now() - file_m_time

    print tdelta
    print 'days : %d' % tdelta.days

# File will be archived/logged if modded within the last 24hrs

    if tdelta.days == 0:
        global ready_to_archive
        ready_to_archive = ready_to_archive + 1
        return True
    else: return False

# Archive function

def main():
    global ready_to_archive
    global archived
    ready_to_archive, archived = 0, 0


    for fname in os.listdir('C:\Users\Thien Nguyen\Desktop\A'):

        src_fname = 'C:\Users\Thien Nguyen\Desktop\A\%s' % fname

        if file_modified(src_fname):
            dst_fname = 'C:\Users\Thien Nguyen\Desktop\B\%s' % fname
            dst_folder = 'C:\Users\Thien Nguyen\Desktop\B'


            try:
                shutil.copy2(src_fname, dst_folder)
                global archived;
                archived = archived + 1

                print 'Copying file : %s ' % (src_fname)
                print '      To loc : %s ' % (dst_fname)

            except IOError as e:
                    print 'could not open the file: %s ' % e

if __name__ == "__main__":
    
    main()

    print '*   Log Report for %s   *' % datetime.datetime.now()
    print '%d files ready to be logged ' % ready_to_archive
    print '%d files logged' % archived

   
