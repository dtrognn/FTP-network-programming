import ftplib
import os

# check if the file already exists
if os.path.exists('getkernel-1.1.1.tar.gz'):
  raise IOError('refusing to overwrite your getkernel-1.1.1.tar.gz file')

ftp = ftplib.FTP('ftp.ibiblio.org')
ftp.login()

# cwd - Change current working directory to path.
ftp.cwd('/pub/linux/kernel')

# check for errors during transmission
ftp.voidcmd('TYPE I')

socket, size = ftp.ntransfercmd("RETR getkernel-1.1.1.tar.gz")
nbytes = 0

# mode wb - Creates a new file if it does not exist or truncates the file if it exists - binary mode.
with open('getkernel-1.1.1.tar.gz', 'wb') as f:
  # retrbinary - retrieve a file or listing of the contents of a directory - binary mode of transfer.
  #ftp.retrbinary('RETR COPYING', f.write())
  while True:
    #receive only 2048 bytes at a time
    data = socket.recv(2048)
    if not data:
      break
    f.write(data)
    nbytes += len(data)
    print(f"Received {nbytes}", end=" ")
    if size:
      print(f"of {size} total bytes "
            f"{round(100 * nbytes / float(size),2)} %")
      pass
    pass
socket.close()
ftp.voidresp()
ftp.quit()
