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
print(ftp.nlst())

ftp.quit()
