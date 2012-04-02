import _winreg

tpNames = {
    _winreg.REG_BINARY: "REG_BINARY",
    _winreg.REG_DWORD: "REG_DWORD",
    _winreg.REG_DWORD_LITTLE_ENDIAN: "REG_DWORD_LITTLE_ENDIAN",
    _winreg.REG_DWORD_BIG_ENDIAN: "REG_DWORD_BIG_ENDIAN",
    _winreg.REG_EXPAND_SZ: "REG_EXPAND_SZ",
    _winreg.REG_LINK: "REG_LINK",
    _winreg.REG_MULTI_SZ: "REG_MULTI_SZ",
    _winreg.REG_NONE: "REG_NONE",
    _winreg.REG_RESOURCE_LIST: "REG_RESOURCE_LIST", 
    _winreg.REG_FULL_RESOURCE_DESCRIPTOR: "REG_FULL_RESOURCE_DESCRIPTION",
    _winreg.REG_RESOURCE_REQUIREMENTS_LIST: "REG_RESOURCE_REQUIREMENTS_LIST",
    _winreg.REG_SZ : "REG_SZ"
    
    }

def tpName(tp):
    try:
        return tpNames[tp]
    except KeyError:
        return tp

def enumEnv():
    key = _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment' )
    i = 0
    try:
        while True:
            name, value, tp = _winreg.EnumValue(key, i)
            print "%s(%s) - %s" % ( name, tpName(tp), value )
            i += 1
    except WindowsError:
        pass       
    
def getPath():
    key = _winreg.OpenKey( _winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment' )
    value, tp = _winreg.QueryValueEx(key,'path')
    assert tp == _winreg.REG_SZ or tp == _winreg.REG_EXPAND_SZ
    for d in value.split( ';' ):
        print d
    

if __name__ == '__main__':
    print 'readpath.py'
    enumEnv()
    print '\n\n'
    getPath()
