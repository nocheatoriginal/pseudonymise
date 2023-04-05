'''
This file contains the scripts pseudonymise.py, generate.py and distinct.py
and lets them work together.
by nocheatoriginal
'''
import pseudonymise
import generate
import distinct

def main():
	try:
		generate.main()
	except Exception as e:
		raise

	try:
		distinct.main()
	except Exception as e:
		raise

	try:
		pseudonymise.main()
	except Exception as e:
		raise

if __name__ == '__main__':
	main()