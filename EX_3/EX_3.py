import ftplib
import os

ftp = ftplib.FTP('ftp.ibiblio.org')
ftp.login()

# show welcome respond from server
print(f"Welcome: {ftp.getwelcome()}")

# pwd - Current working directory.
print("Current working directory: ", ftp.pwd())

print("\n ------------------------------------------------------------- \n")

if os.path.exists('getkernel-1.1.1.tar.gz'):
  raise IOError('refusing to overwrite your getkernel-1.1.1.tar.gz file')

# cwd - Change current working directory to path.
ftp.cwd('/pub/linux/kernel')
print("Current path: ", ftp.pwd())

# mode wb - Creates a new file if it does not exist or truncates the file if it exists - binary mode.
with open('getkernel-1.1.1.tar.gz', 'wb') as f:
  # retrbinary - retrieve a file or listing of the contents of a directory - binary mode of transfer.
  ftp.retrbinary('RETR COPYING', f.write())

ftp.quit()
