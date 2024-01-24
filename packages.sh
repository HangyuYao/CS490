# Updating the system
sudo apt-get update -y

# Install htop and screen
sudo apt-get install -y htop screen

# Install Miniconda
# Define the installation folder and Miniconda installer script
MINICONDA_FOLDER=~/miniconda3
INSTALLER_SCRIPT=Miniconda3-latest-Linux-x86_64.sh

# Download the Miniconda installer script
wget https://repo.anaconda.com/miniconda/$INSTALLER_SCRIPT

# Run the installer script
bash $INSTALLER_SCRIPT -b -p $MINICONDA_FOLDER

# Check if conda was installed successfully
if [ -f "$MINICONDA_FOLDER/bin/conda" ]; then
    echo "Miniconda installed successfully."
    # Initialize conda for bash shell
    $MINICONDA_FOLDER/bin/conda init bash
else
    echo "Miniconda installation failed."
fi

# Clean up the installer script
rm $INSTALLER_SCRIPT
