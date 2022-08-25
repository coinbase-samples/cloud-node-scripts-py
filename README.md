# cloud-node-scripts-py

This repo is a collection of python scripts intended to show how to use the [Coinbase Cloud](https://www.coinbase.com/cloud) Node product. Each directory is for a specific protocol.

Current Protocols Supported:
- Ethereum

All scripts are written in Python3 and have been tested with versions that are not [end of life](https://endoflife.date/python)

## Configuration
The following environment variables expected for these scripts to work:

* NODE_USERNAME: the username associated with the Node access
* NODE_PASSWORD: the password associated with the Node access
8 NODE_ENDPOINT: the URL of the node endpoint

These need to be set before executing any scripts. You can do so for the current terminal session by the following:
```
export NODE_USERNAME=replacewithusername
export NODE_PASSWORD=replacewithpassword
export NODE_ENDPOINT=replacewithurl
```

And if you want to set these in your Bash profile (replace with .zshrc for ZSH):
```
echo "export NODE_USERNAME='<NODE_USERNAME>'" >> ~/.bash_profile
echo "export NODE_PASSWORD='<NODE_PASSWORD>'" >> ~/.bash_profile
echo "export NODE_ENDPOINT='<NODE_ENDPOINT>'" >> ~/.bash_profile
```
