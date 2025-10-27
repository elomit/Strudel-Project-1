"""
This script should help to document and find back strudel vocabulary.

Simply run:
python vocab.py 'strudle_code_you_are_looking_for'

If it is a new entry, just follow this instructions.
"""


import pandas as pd
import argparse


# arg parser
def create_argparser():
    """Argument parser setup."""
    parser = argparse.ArgumentParser(description='look for strudel pattern')
    parser.add_argument('vocab', help='Look for this pattern')

    args = parser.parse_args()

    return args


def main():
	"""Store new entries for strudle vocabulary."""
      
	# read vocab excel and turn into dictionary
	vocab_dict = {}
	vocab_excel = pd.read_excel('vocab_list.xlsx')
	for i in range(0,len(vocab_excel)):
		vocab_dict[vocab_excel.loc[i,'vocab']] = vocab_excel.loc[i,'strudle code']

	# look for vocabulary
	args = create_argparser()
	vocab = args.vocab
	if vocab in vocab_dict:
		print(f'\n{vocab_dict[vocab]}\n')

	# if it does not exist yet, add it to the list
	else:
		print('It seems the patter you are looking for is not yet in the list.')
		print('Do you want to add it? (y/n)')
		answer = input()

		if answer == 'y':
			print(f"Please give me the strudle code you want to save for '{vocab}':")
			strudle_code = input()
			vocab_dict[vocab] = strudle_code

			new_df = pd.DataFrame(list(vocab_dict.items()), columns=['vocab', 'strudle_code'])
			new_df.to_excel('vocab_list.xlsx')

			print("\nNew vocab saved to the list.\nWhup whup! Our strudle vocabulary is growing!\nDon't forget to commit and push.")


if __name__ == '__main__':
    main()

