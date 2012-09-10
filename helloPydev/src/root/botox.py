import boto
import os


def xcopy():
    s3 = boto.connect_s3()
    #rs = conn.get_all_buckets()
    ufr = s3.create_bucket('ufr')
    keys = ufr.list()
    for k in keys:
        folder_name, file_name = k.name.split('/')
        if( not os.path.isdir(folder_name) ):
            print "Making folder: '%s'" % (folder_name)
            os.mkdir( folder_name )
        print "  - %s" % (file_name)
        k.get_contents_to_filename(k.name)
    
    
if __name__ == '__main__':
    xcopy();