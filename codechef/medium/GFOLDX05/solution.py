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
