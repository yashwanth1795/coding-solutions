# GFOLDX05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create a playlist from song indices

You have a NumPy array containing the names of 20 songs. Your task is to create a playlist by selecting specific songs using their indices. Take indices as input from user. Use integer array indexing to extract the desired songs and create a new array representing your playlist.

### Sample 1:
Input
Output

```
3 6 8 13
```

```
['Song D' 'Song G' 'Song I' 'Song N']
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T03:15:48.649Z  

```py
import numpy as np

# Array of 20 songs
songs = np.array(['Song A', 'Song B', 'Song C', 'Song D', 'Song E',
                  'Song F', 'Song G', 'Song H', 'Song I', 'Song J',
                  'Song K', 'Song L', 'Song M', 'Song N', 'Song O',
                  'Song P', 'Song Q', 'Song R', 'Song S', 'Song T'])

indices=input().split()
indices=[int (sc) for sc in indices]
playlist=songs[indices]
print(playlist)

```

---

[View on CodeChef](https://www.codechef.com/problems/GFOLDX05)