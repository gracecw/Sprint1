def deploy(path_to_ssh_key_private_key, server_address, prefix):   
    import paramiko
    
    ### SSH into EC2 and git clone repo 
    def connect():
        key = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
        print("Connecting to server") #Debug statement
        
        #Create a new ssh client
        ssh_client = paramiko.client.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
        
        #Connecting to the host
        ssh_client.connect(hostname = server_address, username = 'testtest', pkey = key)
        print("Connected to server")
        
        #Execute command to check if repository exists
        stdin, stdout, stderr = ssh_client.exec_command('ls Sprint1')
        #Delete if it exists
        if stdout.read() != b'':
            print("Deleting Sprint1 repository")
            ssh_client.exec_command('rm -rf Sprint1')
        
        #Clone the repo
        stdin, stdout, stderr = ssh_client.exec_command('git clone https://github.com/gracecw/Sprint1; yes | reload')
        if stderr.read() != b'':
            print("Successfully cloned repo") 
        else:
            print('Error: ' + stderr.read())
    
        stdin, stdout, stderr = ssh_client.exec_command('(crontab -l; echo "*/5 * * * * python /home/testtest/Sprint1/process.py %s") | crontab -' %prefix)
        print("Script excuted")
        
        ssh_client.close()
        print("Exited server")
        

    client = connect()