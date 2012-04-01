
def info(obj, spacing=10, collapse=1):
    """apihelper.info
    
    Print methods and doc strings. Takes module, class list, dictionary or string
    """

    methodList = [method for method in dir(obj) if callable(getattr(obj,method))]
    print methodList
    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s: s)
    print "\n".join( 
        ["%s %s" % ( method.ljust(spacing),
                     processFunc(str(getattr(obj,method).__doc__))
                     )
         for method in methodList]
        )


if __name__ == '__main__':
    print info.__doc__