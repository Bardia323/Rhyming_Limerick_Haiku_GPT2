import pandas as pd
import numpy as np
import pronouncing


def clean_haikus(haikus):
    """
    :param haikus: a dataframe of poems to be cleaned,
    so that we only deal with haikus of the syllabic form 5-7-5
    :return: good_haikus_df: a dataframe of all the valid haikus
    bad_haikus_df: a dataframe of all the haikus that aren't valid in form 5-7-5
    """
    indices_rows_to_drop = set()
    indices_actual_haikus = set()
    i = 0
    for index, row in haiku_df.iterrows():
        line_1 = row['line_1']
        line_2 = row['line_2']
        line_3 = row['line_3']
        lines = [line_1, line_2, line_3]
        to_drop = False
        for line in lines:
            split_line = line.split()
            line_syllable_count = 0
            for word in split_line:
                pronunciation_list = pronouncing.phones_for_word(word)
                # If a word in poem does not have any pronunciations (is not in CMU dictionary), drop poem.
                if len(pronunciation_list) == 0:
                    indices_rows_to_drop.add(index)
                    to_drop = True
                    break
                else:
                    line_syllable_count += pronouncing.syllable_count(pronunciation_list[0])
            # If poem contains line with wrong number of syllables, drop poem.
            if ((line == line_1 or line == line_3) and (line_syllable_count != 5)) \
                    or ((line == line_2) and (line_syllable_count != 7)):
                to_drop = True
                indices_rows_to_drop.add(index)
                break
        if not to_drop:
            indices_actual_haikus.add(index)

    # print(haiku_df.shape)
    good_haikus_df = haiku_df.drop(labels=indices_rows_to_drop, axis=0)
    bad_haikus_df = haiku_df.drop(labels=indices_actual_haikus, axis=0)

    return good_haikus_df, bad_haikus_df


file_name = '/Users/matthewkorahais/Desktop/COMP550/Final Project/just_haikus.csv'
haiku_df = pd.read_csv(file_name, encoding='latin-1')
print(haiku_df)

good_haikus, bad_haikus = clean_haikus(haiku_df)

print(good_haikus)
print(bad_haikus)

#
# # Creating CSV files of haiku
# compression_opts1 = dict(method='zip',
#                          archive_name='good_haikus.csv')
# good_haikus.to_csv('good_haikus.zip', index=False,
#                       compression=compression_opts1)
#
# compression_opts2 = dict(method='zip',
#                          archive_name='bad_haikus.csv')
# bad_haikus.to_csv('bad_haikus.zip', index=False,
#                      compression=compression_opts2)
