# OneClickDeployment
Making one click deployment, literally.

### Setting Up on AWS Side

##### GitHub Key

This will create a key that can be used from AWS to read this specific repo, but not push anything back to it.
To create ssh key, created a deploy key locally by typing:
```
$ ssh-keygen
# determine a file to save it to, then press enter, and it will output the location that it got sent to
$ vi <location in output>
# copy that key
```
Now follow [these instructions (under Deploy Keys)](https://developer.github.com/guides/managing-deploy-keys/). (perhaps screenshot and put it here just to make sure that people don't get confused). Paste in what you copied above in Step 6.  

### Notes

* http://blog.teamtreehouse.com/install-node-js-npm-linux
* http://linuxbrew.sh/
* https://gist.github.com/iMilnb/df47cd6aea9eeac153ff#file-ec2-py-L129
