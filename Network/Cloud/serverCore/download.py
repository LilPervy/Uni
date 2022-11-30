


def DownloadFile(serverSocket):
    print("[+] Downloading Files")

    filename = serverSocket.ReceiveData()
    serverSocket.ReceiveFile(filename)
