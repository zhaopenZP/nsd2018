import sys

def unix2dos(fname):
    dst_fname = fname + '.txt'
    with open(fname) as src_fobj:
        with open(dst_fname, 'w') as dst_fobj:
            for line in src_fobj:
                dst_fobj.write(line.rstrip() + '\r\n')

if __name__ == '__main__':
    unix2dos(sys.argv[1])
