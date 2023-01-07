import sys
import os

def main():
  # Check if a file was passed as an argument
  if len(sys.argv) < 2:
    # Print a message in bold, red text
    print('\033[1m\033[31m[+] You need to pass a list of username before running this script\033[0m')
    print('[-] Example: python3 sys.argv[0] username.txt')
    print('[-] Re-run this script again. Bye!!!')
    return

  # Open the file passed as an argument for reading
  with open(sys.argv[1], 'r') as f:
    # Keep asking the user to choose an option until a valid choice is made
    while True:
      # Ask the user to choose an option
      print('[1] Names will be kept in original format')
      print('[2] Names will be converted to lowercase')
      print('[3] Names will be converted to lowercase and appended with domain name')
      choice = input('Enter your choice: ')

      # Determine the name of the result file based on the user's choice
      if choice == '1':
        result_filename = 'result_original_names.txt'
        break
      elif choice == '2':
        result_filename = 'result_lowercase_names.txt'
        break
      elif choice == '3':
        domain_name = input('Enter the domain name (Ex: google.com): ')
        result_filename = 'result_lowercase_emails.txt'
        break
      else:
        print('Invalid choice, please try again')
        print('')

    # Open the result file for writing
    with open(result_filename, 'w') as result_file:
      # Iterate over each line in the file
      for line in f:
        # Strip leading and trailing whitespace from the line
        line = line.strip()

        # Split the line into first and last name
        first_name, last_name = line.split(' ')

        # Convert the names to lowercase if the user chose option 2 or 3
        if choice == '2' or choice == '3':
          first_name = first_name.lower()
          last_name = last_name.lower()

        # Generate the different variations of the username
        usernames = [
          first_name,
          last_name,
          first_name + last_name,
	  first_name[0] + last_name[0],
          first_name[0] + last_name,
          first_name + '.' + last_name,
          first_name + '-' + last_name,
          first_name + '_' + last_name,
          first_name[0] + '.' + last_name,
          first_name[0] + '-' + last_name,
          first_name[0] + '_' + last_name,
          last_name + first_name,
	  last_name[0] + first_name[0],
          last_name + '.' + first_name,
          last_name + '-' + first_name,
          last_name + '_' + first_name,
          last_name + '.' + first_name[0],
          last_name + first_name[0],
        ]

       # Append the domain name to the usernames if the user chose option 3
        if choice == '3':
          usernames = [username + '@' + domain_name for username in usernames]

        # Write the usernames to the result file
        for username in usernames:
          result_file.write(username + '\n')

if __name__ == '__main__':
  main()
