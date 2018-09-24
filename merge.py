import sys
import subprocess

pattern = sys.argv[1]

cat_command = 'cat ' + pattern + ' > merge.ts'
s1 = subprocess.Popen(cat_command, shell=True)

command = 'ffmpeg -i "concat:merge.ts" -c copy -bsf:a aac_adtstoasc -movflags +faststart output.mp4'
s2 = subprocess.Popen(command, shell=True)

s3 = subprocess.Popen('rm merge.ts', shell=True)
