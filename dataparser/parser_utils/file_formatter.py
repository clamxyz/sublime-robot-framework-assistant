from hashlib import md5
from os import path


def rf_table_name(f_path):
    md5sum = md5(f_path.encode('utf-8')).hexdigest()
    return '{realname}-{md5}.json'.format(
        realname=path.basename(f_path)[-100:],
        md5=md5sum
    )


def lib_table_name(library):
    realname = library[-100:] if isinstance(library, str) else library[-100:].decode('utf-8')
    library = library.encode('utf-8') if isinstance(library, str) else library
    return '{realname}-{md5}.json'.format(
        realname=realname,
        md5=md5(library).hexdigest()
    )
