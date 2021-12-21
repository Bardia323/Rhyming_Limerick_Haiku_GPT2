import pandas as pd
import numpy as np
import pronouncing
import syllapy


def separate_poems(txt_file):
    sep_poems = []
    cur_poem = []
    for line in txt_file:
        if line != '====================\n':
            line = line.strip()
            cur_poem.append(line)
        else:
            sep_poems.append(cur_poem)
            cur_poem = []
    return sep_poems


# A haiku grader
# Checks that all three lines of the haiku have the
# correct number of syllables.
# Correct output: lines 1 and 3 have 5 syllables, line 2 has 7 syllables.

def haiku_grader(candidate):
    """
    :param candidate: LIST containing three strings (three lines in poem)
    :return: tuple: (True/False for whether it's a haiku,
            [int, int, int] representing num syllables away from correct
            for each word in the line)
    """

    # Make sure in haiku_doc_grader function that poems are three lines
    valid_haiku = True
    error = [0, 0, 0]
    for line_index in range(3):
        split_line = candidate[line_index].split()
        line_syllable_count = 0
        for word in split_line:
            pronunciation_list = pronouncing.phones_for_word(word)
            # If a word in poem does not have any pronunciations (is not in CMU dictionary), drop poem.
            if len(pronunciation_list) == 0:
                valid_haiku = False
                error[line_index] = -1  # -1 when line contains word whose pronunciation is unknown
                break
            else:
                line_syllable_count += pronouncing.syllable_count(pronunciation_list[0])

        if (line_index == 0) or (line_index == 2):  # If 1st or 3rd line
            if line_syllable_count != 5:
                error[line_index] = abs(line_syllable_count - 5)
                valid_haiku = False
        else:  # If 2nd line
            if line_syllable_count != 7:
                error[line_index] = abs(line_syllable_count - 7)
                valid_haiku = False

    return valid_haiku, error


def grade_all_poems(potential_haikus):
    valid_counter = 0
    poem_counter = 0
    wrong_num_lines = 0
    valid_haikus = []
    invalid_haikus = []
    errors = []
    for poem in separated_poems:
        poem_counter += 1
        if len(poem) == 3:
            valid_haiku, error = haiku_grader(poem)
            errors.append(error)
            # Keeping track of the average error for each of the
            if valid_haiku:
                valid_counter += 1
                valid_haikus.append(poem)
            else:
                invalid_haikus.append(poem)
            # print('Valid haiku?: ', valid_haiku)
            # print('error: ', error)
        else:
            # print('incorrect number of lines!')
            wrong_num_lines += 1

    return valid_counter, valid_haikus, invalid_haikus, errors


# Calculate average error by summing all the errors
def calculate_average_error(errors):
    total_error_line1 = 0
    total_error_line2 = 0
    total_error_line3 = 0

    # 'errors' is a list of lists 'error'
    # each list 'error' contains 3 integers
    for error in errors:
        for line_index in range(3):
            if line_index == 0:
                total_error_line1 += error[line_index]
            if line_index == 1:
                total_error_line2 += error[line_index]
            if line_index == 2:
                total_error_line3 += error[line_index]

    num_3line_poems = len(errors)
    average_error_line1 = total_error_line1 / num_3line_poems
    average_error_line2 = total_error_line2 / num_3line_poems
    average_error_line3 = total_error_line3 / num_3line_poems

    return average_error_line1, average_error_line2, average_error_line3


# /Users/matthewkorahais/Desktop/COMP550/Final Project/355M_1000steps.txt
file_name = "/Users/matthewkorahais/Desktop/COMP550/Final Project/3000steps/3000steps_temp1.0.txt"

f = open(file_name, "r")

separated_poems = separate_poems(f)

f.close()

num_valid_haikus, valid_haikus, invalid_haikus, poem_errors = grade_all_poems(separated_poems)
print('Number of valid haikus: ', num_valid_haikus)
print('Valid haikus: ', valid_haikus)
print('Invalid haikus: ', invalid_haikus)

avg_error_line1, avg_error_line2, avg_error_line3 = calculate_average_error(poem_errors)
print('Average error line 1: ', avg_error_line1)
print('Average error line 2: ', avg_error_line2)
print('Average error line 3: ', avg_error_line3)
