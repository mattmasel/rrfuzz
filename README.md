# rrfuzz

Simple fuzzing tool that can handle login request rate timeouts.  

## Disclaimer: Ethical Use Only

This tool is intended for ethical uses only. Users are expected to adhere to responsible and legal security testing practices. The creators disclaim any responsibility for misuse. By using this tool, you agree to these terms.  

## Usage

1. Edit the constant variables at the top of rrfuzz.py such as url, timeout time, etc...
2. Edit the post request parameters to match the form you are fuzzing
3. Execute

~~~bash
python rrfuzz.py </path/to/wordlist>
~~~
