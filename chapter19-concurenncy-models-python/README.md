Files spinner_*.py show different implementations of a spinner while 
simulating a long computation. The original idea comes from this 
post: https://mail.python.org/pipermail/python-list/2009-February/675659.html

While getting deeper into the examples that show how spawning processes should be faster than threads while doing CPU intensive computation (prime_check_process.py), I was getting numbers that weren't consistent with this argument (spawning either processes or threads was ending in similar times)
Seems like the above is a known issue. There is an open issue [here](https://github.com/fluentpython/example-code-2e/issues/43)
The solution is to generate bigger numbers until the above difference can be seen
