# File Transfer Network
### Description:
This network is set up to send a a file from a client to a server
### Running:
Assuming python is installed
1. After downloading/cloning repo, open a terminal and cd into the file/directory where the repo is stored
2. Type `python fileServer.py` to launch the server
3. Open a new terminal window, cd into the file/directory where the repo is stored
4. Type `python fileClient.py` to launch the client
### List of assignment Requirements:
The "OLDREADME.md" outlines what my program should have.  I have included that same list here as a task list, 
as github refers to it, in order check criteria off as they are completed
- [ ] be in the file-transfer-lab subdir
- [ ] work with and without the proxy
- [ ] support multiple clients simultaneously using `fork()`
- [ ] gracefully deal with scenarios such as: 
    - [ ] zero length files
    - [ ] user attempts to transmit a file which does not exist
    - [ ] file already exists on the server
    - [ ] the client or server unexpectedly disconnect
- [ ] optional (unless you're taking this course for grad credit): be able to request ("get") files from server
