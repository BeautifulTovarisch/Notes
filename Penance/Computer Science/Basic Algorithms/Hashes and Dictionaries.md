Hashes are one of the most versatile data structures and find their way into a wide variety of problems in computer science.  The core ideas are:

- Use a **hash function** to produce some numerical index representation of an object
- Configure an underlying table size such that collisions are minimized
- Mitigate the situation in which collisions occur

> [!tip]
> In practice, hashing is very expensive and a complicated (or invertible) hash function may be overkill. A pragmatic choice has been to use the memory address of the object when **structural** equality is not needed

## Hash Table Size

Generally, choosing a good hash table size requires an understanding of the distribution of hashed values (keys) to be inserted into the table. Some general recommendations of choosing a hash table size:

- Large, uncommon primes
- "reasonable" array size with respect to system memory
- Use modulo to compute final index of hashed value

## Bloom Filters

An interesting data structure that trades deterministic answers for both space and time complexity is called a bloom filter. 

> [!todo]
> Elaborate more on bloom filters later, or move to "advanced" section