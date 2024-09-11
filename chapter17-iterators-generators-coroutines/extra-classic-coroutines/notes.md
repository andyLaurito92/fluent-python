Since Python 3.5 we have 3 types of coroutines:

1. Classic coroutines -> generator functions that consume data sent to it via send() | give data away using yield

2. Generator-based coroutines -> generator function decorated with @types.coroutine, which makes it compatible with the 
new await keyword

3. Native coroutines -> A coroutine defined with async def. You can delegate from a native coroutine to another or to a 
generatord-based coroutine using the await keyword (in a classic coroutine the analogous is to use yield from)

2 & 3 are meant for asyncrhonous I/O programming

