### Connect to Server through SSH
- Get Server username and IP address
- Open Terminal and run
	- `ssh -i <path_to_pem_file> <instance-user-name>@<instance-public-dns-name or public IP address>`
    - Make `.pem` file read-only
        - `chmod 400 <filename.pem>`

### Transfer files to Server
`scp -i <key.pem> <file> hostname@IPaddress:<destination_path>`