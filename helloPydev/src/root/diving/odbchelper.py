'''
Created on Mar 22, 2012

@author: uri
'''

def buildConnectionString(params):
    """Build a connection string from a dictionary
    returns string."""
    return ";" . join( ["%s=%s" % (k,v) for k,v in params.items()] )

if __name__ == "__main__":
    myParams = {
        "server" : "tower",                
        "database" : "master",
        "uid" : "sa",
        "pwd" : "secret"
    }
    #print buildConnectionString.__doc__
    print buildConnectionString( myParams )

    
