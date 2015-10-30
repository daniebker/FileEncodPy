import argparse
import codecs
import os

__author__ = 'dbaker'


BLOCKSIZE = 1048576 # or some other, desired size in bytes


parser = argparse.ArgumentParser()
parser.add_argument("-o", help='Output directory', required=True)
parser.add_argument("-i", help='Input Directory', required=True)
parser.add_argument("-oe", help='Original Encoding', required=True)
parser.add_argument("-ne", help='New Encoding', required=True)
args = parser.parse_args()

for dirName, subdirList, fileList in os.walk(args.i):
    print('+---- %s\n|\t\t|' % dirName)
    for fname in fileList:
        with codecs.open(dirName + os.path.sep + fname, "r", args.oe) as sourceFile:
            print ('|\t\t|---- Opening %s as %s ' % (fname, args.oe))

            targetDir = args.o + os.path.sep + os.path.basename(dirName)

            if not os.path.exists(targetDir):
                os.makedirs(targetDir)

            with codecs.open(targetDir + "\\" + fname, "w", args.ne) as targetFile:
                print ('|\t\t|\tWriting %s as %s' % (targetDir + os.path.sep + fname, args.ne))
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)
