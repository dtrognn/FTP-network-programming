import ftplib
import os

ftp = ftplib.FTP('ftp.ibiblio.org')
ftp.login()

# show welcome respond from server
print(f"Welcome: {ftp.getwelcome()}")

# pwd - Current working directory.
print("Current working directory: ", ftp.pwd())

print("\n ------------------------------------------------------------- \n")

# cwd - Change current working directory to path.
ftp.cwd('/pub/linux/kernel')
print("Current path: ", ftp.pwd())

# mode w - Creates a new file if it does not exist or truncates the file if it exists.
with open('COPYING', 'w') as f:
  def writeline(data):
    f.write(data)
  # retrlines - retrieve a file or listing of the contents of a directory - ASCII mode of transfer.
  ftp.retrlines('RETR COPYING', writeline)

ftp.quit()
