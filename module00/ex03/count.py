import string
import sys

def text_analyzer(arg=None):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	if arg is None:
		print("What is the text to analyze?")
		arg = input()
	
	if not isinstance(arg, str):
		print("AssertionError: argument is not a string")
		return

	lowcase = len([x for x in arg if x.islower()])
	upcase = len([x for x in arg if x.isupper()])
	spaces = len([x for x in arg if x.isspace()])
	punctuation = len([x for x in arg if x in string.punctuation])
	chars = len(arg)

	print(f"The text contains {chars} printable characters:")
	print(f"- {upcase} : upper letter(s)")
	print(f"- {lowcase} : lower letter(s)")
	print(f"- {punctuation} : punctuation mark(s)")
	print(f"- {spaces} : space(s)")
	
if __name__ == "__main__":
	if (len(sys.argv) > 2):
		print("Usage: python count.py <string> or python count.py")
		sys.exit(1)
	elif (len(sys.argv) == 1):
		text_analyzer()
	else:
		text_analyzer(sys.argv[1])