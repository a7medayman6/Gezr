## SENTENCE LEVEL

1. Tokenization
2. Stop Words Removal


3. for each token
	3.1 Normalization
	3.2 Remove non-letters
	3.3 Remove articles based on algo.1
	3.4 Remove suffixes 
	3.5 Remove prefixes
	3.6 Remove suffixes of len = 1

	After each step, check if current token is a root against roots.json corpus. 
	If so stop any further processing for current token.