class triad():
    def __init__(self,first,third,fifth):
        self.first = first
        self.third = third
        self.fifth = fifth

#Major Chords
C_Major = triad('C','E','G') 
DFlat_Major = triad('Db','F','Ab')
D_Major = triad('D','F#','A')
EFlat_Major = triad('Eb','G','Bb')
E_Major = triad('E','G#','B')
F_Major = triad('F','A','C')
FSharp_Major = triad('F#','A#','C#')
GFlat_Major = triad('Gb','Bb','Db')
G_Major = triad('G','B','D')
AFlat_Major = triad('Ab','C','Eb')
A_Major = triad('A','C#','E')
BFlat_Major = triad('Bb','D','F')
B_Major = triad('B','D#','F#')

#Minor Chords
C_Minor = triad('C','Eb','G')
