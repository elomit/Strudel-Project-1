"""
This script should help to document and find back strudel vocabulary.

Simply run:
python vocab.py 'strudel_code_you_are_looking_for'

If it is a new entry, just follow the instructions.
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


def read_multiline_input(prompt):
    """Read a multi-line code block from stdin until the user ends it."""
    print(prompt)
    print("(Paste your code, then type --- on its own line and press Enter)")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "---":
            break

        lines.append(line)

    return "\n".join(lines)


def main():
	"""Store new entries for strudel vocabulary."""
      
	# read vocab excel and turn into dictionary
	vocab_dict = {}
	vocab_file = pd.read_csv('vocab_list.csv')
	for i in range(0,len(vocab_file)):
		vocab_dict[vocab_file.loc[i,'vocab']] = vocab_file.loc[i,'strudel_code']

	# look for vocabulary
	args = create_argparser()
	vocab = args.vocab

	if vocab == 'show-all':
		for key in vocab_dict.keys():
			print(key)

	elif vocab in vocab_dict:
		code = vocab_dict[args.vocab]
		code = bytes(code, "utf-8").decode("unicode_escape")
		print(f"\n{code}\n")
	

	# if it does not exist yet, add it to the list
	else:
		print('It seems the pattern you are looking for is not yet in the list.')
		print('Do you want to add it? (y/n)')
		answer = input()

		if answer == 'y':
			strudel_code = read_multiline_input(f"Please give me the strudel code you want to save for '{vocab}':")
			if strudel_code:
				vocab_dict[vocab] = strudel_code

				new_df = pd.DataFrame(list(vocab_dict.items()), columns=['vocab', 'strudel_code'])
				new_df.to_csv('vocab_list.csv')

				print("\nNew vocab saved to the list.\nWhup whup! Our strudel vocabulary is growing!\nDon't forget to commit and push.")

			else:
				print("No code was entered. Nothing was saved.")


if __name__ == '__main__':
    main()

