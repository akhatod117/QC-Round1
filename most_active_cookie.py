import csv


def main():

    #goal of this function is to ensure validity of the input - boolean (T - if valid, F - if not)
    def valid_input(input_array):
        #check length
        if len(input_array) != 4:
            return False
        
        #now check the two statements that should be consistent regardless of day

        if input_array[0] != './most_active_cookie' or input_array[2] != '-d':
            return False

        #simple checking of date, should have length of 10 including dashes

        if len(input_array[3]) != 10:
            return False
        
        return True
    
    #this function runs through csv file and returns a dictionary
    #key: cookie id, value: number of occurences

    def log_dictionary(csv_file):

        cookie_dict = {}

        with open(csv_file, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:

                
                #row is a list seperated on , 
                #row[0] = cookie id
                #row[1] = timestamp
            

                #get the date in yyyy-mm-dd format (don't need time)
                date = row[1][:10]

                #check if the date is what our user wants

                if date == input_array[3]:

                    #increment count if we've seen cookie before
                    #otherwise, new entry into dictionary
                    try:
                        cookie_dict[row[0]] += 1
                    except KeyError:
                        cookie_dict[row[0]] = 1
                else:
                    continue
                
        
        #after entire log file has been parsed, return final dictionary

        return cookie_dict
    

    #this function will find the most active cookie(s) from the constructed dictionary

    def most_active(cookie_dict):
        
        #solutions list
        active = []

        #max occurences of a cookie seen so far
        max_occurrences = -1

        #iterate through each cookie in the dictionary
        for cookie in cookie_dict.keys():
            
            #get the # of occurences in the specific cookie
            current_occurrences = cookie_dict[cookie]

            #set max_occurences to the max of itself and the current # of occurences
            max_occurrences = max(max_occurrences, current_occurrences)

            #if current occurences is the same as the max we've seen so far, most active cookie seen so far...add it to solutions list.
            if current_occurrences == max_occurrences:
                active.append(cookie)

        #now have gone through all relevant cookies, return the solutions

        return active



    
    #get command that's passed in
    input_string = input("Enter command here:")

    #split command using default delimiter as space to parse each section

    input_array = input_string.split()


    #only continue if input is valid
    if valid_input(input_array):
        
        #established valid input
        #now need to run through the csv file
        
        #get .csv file name
        csv_name = input_array[1]

        #create dictionary with cookie id as key, number of occurences as value
        cookie_dict = log_dictionary(csv_name)


        #get the most active cookies as a lsit
        most_active_cookies = most_active(cookie_dict)

        #extra print statement for increased readability on command line.
        print()

        #print each cookie deemed to be most active on the given date
        #if the list is empty, return 'No active cookies': this is also a valid output otherwise the user has no idea whether the program worked or not
        
        if most_active_cookies:
            for cookie in most_active_cookies:
                print(cookie)
        else:
            print('No active cookies')




    else:
        print('Invalid input...re-check and try again')
        return None
    
if __name__ == "__main__":
    main()






    
    
    

        

    

