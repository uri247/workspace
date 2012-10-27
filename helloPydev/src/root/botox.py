import boto
import os
import itertools


localpath = r'c:/local/media/photos/ufr'
bucket = 'ufr'
limit = 100

s3 = ufr = keys = None
sky_list = list()
sky_fldrs = dict()
local_list = list()

def connect():
    global s3, ufr, keys
    s3 = boto.connect_s3()
    ufr = s3.create_bucket(bucket)
    keys = ufr.list()

def get_sky_list():
    """
    populates the sky_list global
    each item in the list is an tuple with the following format:
    (folder, tail, name, size)
    folder - the root folder (e.g. album name for the photoalbum ufr
    tail - the rest of the path
    name - full path to the item
    size - size in bytes
    """
    for index,k in enumerate(keys):
        if( index == limit ):
            break
        folder, _, tail = k.name.partition('/')
        item = ( folder, tail, k.name, k.size )
        sky_list.append( item )
    sky_list.sort( key = lambda item: item[0] )

def group_sky_by_folders():
    for fldrnm, ls_it in itertools.groupby( sky_list, lambda item: item[0] ):
        ls = list(ls_it)
        total_size = sum( item[3] for item in ls )
        sky_fldrs[fldrnm] = (fldrnm,list(ls),total_size)      

def print_sky_folders():
    for k in sorted(sky_fldrs.keys()):
        fldrnm, ls, total_size = sky_fldrs[k]
        print '{0:<54s}{1:3} files  {2:>12,} bytes'.format( fldrnm, len(ls), total_size )

def get_local_list():
    """
    populate local_list. each record has:
    (rel_path, size)
    """
    for r,_,fs in os.walk(localpath):
        for f in fs:
            full_path = os.path.join(r,f)
            rel_path = os.path.relpath(full_path,localpath).replace('\\','/')
            item = ( rel_path, os.path.getsize(full_path) )
            local_list.append( item )
    
def get_missings():
    skyNames = [skyName for _,_,skyName,_ in sky_list]
    localNames = [localName for localName,_ in local_list]
    
    skyNotInLocal = [skyName for skyName in skyNames if skyName not in localNames]
    localNotInSky = [localName for localName in localNames if localName not in skyNames]
    
    print 'files in sky missing here:'
    for skyName in skyNotInLocal:
        print skyName
    
    print 'files locally missing from sky:'
    for localName in localNotInSky:
        print localName
    
    
    
def xcopy():
    for k in keys:
        folder_name, file_name = k.name.split('/')
        if( not os.path.isdir(folder_name) ):
            print "Making folder: '%s'" % (folder_name)
            os.mkdir( folder_name )
        print "  - %s" % (file_name)
        k.get_contents_to_filename(k.name)
    

def main():
    connect()
    get_sky_list()
    group_sky_by_folders()
    print_sky_folders()
    get_local_list()
    get_missings()


if __name__ == '__main__':
    main()
    