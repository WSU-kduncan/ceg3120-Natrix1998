# Setup
Step 1. Create a user named git on your AWS Ubuntu instance.
Step 2. Sign in as git, create a directory called ".ssh/" and a file called "authorized_keys" in ".ssh/". 
Step 3. Run "chmod 700 .ssh && chmod 600 .ssh/authorized_keys" to set the permissions. 
Step 4. Add your github public key to the "authorized_keys" file. Reference https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key
Step 5. Run git init.
Step 6. Add the private key created on the AWS instance to your ssh-agent on the host machine. https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent
  Note: Make sure you add the public SSH key to your github account. 

# Usage
