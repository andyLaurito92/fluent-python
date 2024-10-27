Related article talking about why you shouldn't use threads:

https://glyph.twistedmatrix.com/2014/02/unyielding.html


From the above article, important quote:

``` 
The main difference between lightweight and heavyweight threads is that it is that, with rigorous application of strict principles like “never share any state unnecessarily”, and “always write tests for every routine at every point where it might suspend”, lightweight threads make it at least possible to write a program that will behave deterministically and correctly, assuming you understand it in its entirety. When you find a surprising bug in production, because a routine that is now suspending in a place it wasn’t before, it’s possible with a lightweight threading system to write a deterministic test that will exercise that code path. With heavyweight threads, any line could be the position of a context switch at any time, so it’s just not tractable to write tests for every possible order of execution.
```


Event-driven networking engine that uses asyncio

https://twisted.org/
