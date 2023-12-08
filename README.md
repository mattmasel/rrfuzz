# rrfuzz
Simple fuzzing tool that can handle login request rate timeouts.
## Usage
1. Edit the constant variables at the top of rrfuzz.py such as url, timeout time, etc...
2. Edit the post request parameters to match the form you are fuzzing
3. Execute
~~~bash
python rrfuzz.py </path/to/wordlist>
~~~
