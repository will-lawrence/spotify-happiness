# Read function

def read(filename: str) -> List[Song]:
    """
    reads information from the specified csv file and returns a list of songs with associated title,
    artist, acoustincness [0.0,1.0], danceability [0.0,1.0], tempo ((0.0...) in beats per minute), and valence [0.0,1.0]
    """
    # return []
    # template from HtDAP
    # acc contains the result so far
    acc = [] # type: List[Song]

    with open(filename) as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip header line

        for row in reader:
            s = Song(row[0], row[1], parse_float(row[2]), parse_float(row[3]), parse_float(row[12]), parse_float(row[14]))
            acc.append(s)

        return acc

# Begin testing
start_testing()

# Examples for read

expect(read('spotifydata_test1.csv'), [('Mask Off', 'Future', 0.0102, 0.833, 150.062, 0.286),
                                       ('Redbone', 'Childish Gambino', 0.199, 0.743, 160.083, 0.588)])
expect(read('spotifydata_test2.csv'), [('World In Motion', 'New Order', 0.0239, 0.603, 123.922, 0.773),
                                       ('One Nation Under a Groove', 'Funkadelic', 0.233, 0.789, 122.415, 0.842),
                                       ('Bouncin', 'Chief Keef', 0.314, 0.713, 140.061, 0.783)])
# show testing summary
summary()
