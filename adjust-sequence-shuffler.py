#!/usr/bin/env python3

"""
Description:
    adjust-sequence-shuffler
Abstract: 
    This uses a mix of LCG and Fisherman Yates algorithm 
    to generate a random series of numbers within a given interger range.
    if range not specified it defaults to the limit 10.
Author: 
    vakees.ilamaran@gmail.com
"""

import time
import sys
import argparse


class AdjustSequenceShuffler():

    def __init__(self, default_limit):
        self.data_to_shuffle = list(range(1,default_limit + 1))
        self.shuffled_list = self.fisher_yates_shuffle_enhanced(self.data_to_shuffle)

    def linear_congruential_generator(self, mod) -> int:
        """
        Using linear congruential generator algorithm to generate a pseudo-randomized number.
        
        :return: psedo random number
        """

        try:
            # The return value needed within the range is assigned to the modulus
            modulus = mod
            # Dummy variable used to store psedo random number for internal assignment
            value = ''

            # Generating a random seed value to be used for the calcuation using the time
            while True:
                seed = int(time.time() * 10000) % 10
                if seed > 0:
                    break
        
            # Generating a random multiplier value to be used for the calcuation using the time
            while True:
                multiplier = int(time.time()* 1000) % 10
                if multiplier > 0:
                    break
        
            # Generating a random increment value to be used for the calcuation using the time
            while True:
                increment = int(time.time() * 100) % 10
                if increment > 0:
                    break

            # Implements the algorithm to get a random number --> X_n+1 = (aX_n + c ) mod m
            for i in range(modulus):
                value= ((multiplier*seed)+increment) % modulus
                if value > 1:
                    break
                seed = seed + increment
            return value

        except Exception as e:
            print("----- There is some issue with the LCG algorithm computation -----")
            print("Please check the below logs")
            sys.exit(e)



    def fisher_yates_shuffle_enhanced(self, list_of_data) -> list:
        """
        This uses the famous fisher yates algorithm to shuffle with an improved version of using n-1
        
        :return: Array of a shuffled list within the given range.
        """

        try:
            number_of_values_to_shuffle = len(list_of_data)

            # Stopping when the iteration hits 1.
            # Using O(n-1) instead of O(n). In order to avoid going to the 0th position in an array.
            while number_of_values_to_shuffle > 1:
            # Indice must be an integer not a float and floor returns a float
                random_number = self.linear_congruential_generator(number_of_values_to_shuffle)  #int(floor(random() * number_of_values_to_shuffle))
        
                # Using the back of the list to store the already shuffled index,
                # Decreasing the number start value to an already shuffled element.
                number_of_values_to_shuffle -= 1

                # Exchanging the places of the values from the random number selected index to the original one
                list_of_data[random_number], list_of_data[number_of_values_to_shuffle] = list_of_data[number_of_values_to_shuffle], list_of_data[random_number]

            return list_of_data
        
        except Exception as e:
            print("----- There is some issue with the Fisher-yates algorithm computation -----")
            print("Please check the below logs")
            sys.exit(e)


def parsing_args():
    """
    We get the command line arguments and parse it to use it !!
    :return: returns the parse object
    """

    parser = argparse.ArgumentParser(
        prog='adjust-sequence-shuffler',
        epilog='Enjoy the CLI Adjust Team!' )

    parser.add_argument(
        '--limit', 
        metavar ='limit', 
        type = int,
        default= 10,
        required = False,
        help = 'The limit for the shuffling of numbers to be generated')

    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s V1.0.0')   
    
    return parser.parse_args()


def main():
    try:
        # Parsing if there are any command line arguments given.
        args = parsing_args()
        # Creating the instance where the constructor takes care of the computation
        adj_generate_random = AdjustSequenceShuffler(args.limit)
        # Prints the list of shuffled values accessing the list in the class.
        print(*adj_generate_random.shuffled_list, sep = ' ')

    except Exception as e:
        print("There is some issue with the main function")
        print("Please contact the GitHub Contributor for troubleshooting")
        sys.exit(e)

if __name__ == "__main__":
    main()