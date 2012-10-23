import boto
import os

localpath = r'c:/local/photos/ufr'
bucket = 'ufr'


def connect():
    global s3, ufr, keys
    s3 = boto.connect_s3()
    ufr = s3.create_bucket(bucket)
    keys = ufr.list()
    
def xcopy():
    for k in keys:
        folder_name, file_name = k.name.split('/')
        if( not os.path.isdir(folder_name) ):
            print "Making folder: '%s'" % (folder_name)
            os.mkdir( folder_name )
        print "  - %s" % (file_name)
        k.get_contents_to_filename(k.name)
    

def iterate_local():
    for fldr in os.listdir( localpath ):
        if os.path.isdir(fldr):
            #fldr is a folder. verify we have a bucket for it            
            for file in os.listdir(fldr):
                if os.path.isfile( file ):
                    pass
    
def iterate_sky():
    global sky_folders
    sky_folders = dict()
    for index,k in enumerate(keys):
        if( index == 100 ):
            break
        folder, _, fl = k.name.partition('/')
        if folder in sky_folders:
            rec = sky_folders[folder]
        else:
            rec = (folder, [])
            sky_folders[folder] = rec    
        _, ls = rec
        #if not '/' in fl:
        if True:
            ls.append( (fl,k.size) )
        
def print_sky():
    for rec in sorted(sky_folders.keys()):
        nm, ls = sky_folders[rec]
        total = sum( size for _,size in ls )
        print '{0:<54s}{1:3} files  {2:>12,} bytes'.format( nm, len(ls), total )

def there_not_here():
    for fldr in sorted(sky_folders.keys()):
        nm, ls = sky_folders[fldr]
        for f,_ in ls:
            loc_file = localpath + '/' + nm + '/' + f
            if os.path.isfile(loc_file):
                pass
            else:
                print "{0}/{1} there but not here".format( nm, f )


def main():
    connect()
    iterate_sky()
    print_sky()
    there_not_here()


if __name__ == '__main__':
    main()
    