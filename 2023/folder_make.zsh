#!/bin/zsh

# Specify the base directory where you want to create the folders
base_directory="/Users/bolt/Desktop/code/advent-of-code"

# Loop through days 1 to 25 and create folders
for day in {1..25}; do
    folder_name="day_${day}"
    folder_path="${base_directory}/${folder_name}"

    # Check if the folder already exists
    if [ ! -d "$folder_path" ]; then
        # Create the folder
        mkdir "$folder_path"
        echo "Folder created: $folder_path"
    else
        echo "Folder already exists: $folder_path"
    fi
done
