import boto
import os

localpath = r'c:/local/photos/ufr'
bucket = 'ufr'
limit = 100


def connect():
    global s3, ufr, keys
    s3 = boto.connect_s3()
    ufr = s3.create_bucket(bucket)
    keys = ufr.list()
    
def get_sky_list():
    global sky_list
    sky_list = list()
    for index,k in enumerate(keys):
        if( index == limit ):
            break
        folder, _, tail = k.name.partition('/')
        item = ( folder, tail, k.name, k.size )
        sky_list.append( item )

def parse_sky_list():
    global sky_folders
    fldr_set = set( [item[0] for item in sky_list] )
    sky_folders = []
    for fldr in fldr_set:
        print fldr

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
    get_sky_list()
    parse_sky_list()

if __name__ == '__main__':
    main()
    