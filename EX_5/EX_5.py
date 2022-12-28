import ftplib

ftp = ftplib.FTP('ftp.ibiblio.org')
ftp.login()

# show welcome respond from server
print(f"Welcome: {ftp.getwelcome()}")

# pwd - Current working directory.
print("Current working directory: ", ftp.pwd())
print("Current file working in path: ")
print(ftp.nlst())

print("\n ------------------------------------------------------------- \n")

# cwd - Change current working directory to path.
ftp.cwd('/pub/linux/kernel')
print("Current path: ", ftp.pwd())


print("Current file working in path: ")
# The method dir() prints the directory listing as returned by the FTP command LIST.
ftp.dir()

data = []
ftp.dir(data.append)
print("5th file: ", data[5])
stringg =  data[5].split(' ')
print(f"Last modified date of the 5th file: {stringg[20]}, {stringg[22]}, {stringg[24]}")
ftp.quit()
