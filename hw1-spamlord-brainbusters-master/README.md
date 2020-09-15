## Spamlord 
On the web, many people who want to give their email addresses or phone numbers for people to contact them will try to make it hard for spammers to automatically search text for email addresses and phone numbers by giving non-standard forms of them, sometimes called obfuscation. You may have seen examples like:
* jurafsky(at)cs.stanford.edu
* jurafsky at csli dot stanford dot edu

In the spamlord.py there are regular expressions that help identify these obscured emails and phone numbers.

## Running this project
Step 1. Clone/download this repo. 
Step 2. Use a regex editor to add match patterns to the startercode in SpamLord.py https://regex101.com (make sure you select Python from the left side of screen). One pattern for email and one for phone number has been given to you already, e.g.:
```
my_first_pat = '(\w+)@(\w+).edu'
```
You then can add additional patterns, like: 

```
my_second_pat = '[your regex here]'
```

To run the code and get an accuracy score (against the devGOLD set of target email addresses), use terminal on MacOS or Command prompt on windows and run the python file as follows: 

```
python SpamLord.py ..data/dev ..data/devGOLD
```

This will return a count of your true positive matches (tp), false positives (fp), and false negatives (fn). 

Try to improve your tp score by adding additional match patterns to Spamlord.py.

