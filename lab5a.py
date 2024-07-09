#!/usr/bin/env python3
# Author ID: askohri

def read_file_string(file_name):
    # Function to read the entire content of a file as a string
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    # Function to read the entire content of a file as a list of lines without new-line characters
    with open(file_name, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'  # Assuming data.txt exists in the same directory as this script
    print(read_file_string(file_name))
    print(read_file_list(file_name))