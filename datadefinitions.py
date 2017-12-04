# Data Definitiosn

Song = NamedTuple('Song', [('title', str),             # song title
                           ('artist', str),            # artist who performs the song
                           ('acousticness', float),    # Confidence that song is acoustic [0.0,1.0] determined by Spotify
                           ('danceability', float),    # Confidence that song is danceable [0.0,1.0] determined by Spotify
                           ('tempo', float),           # Estimated tempo of a track in beats per minute (BPM) (0.0, )
                           ('valence', float)])        # Estimated musical positiveness conveyed by a track [0.0,1.0] determined by Spotify

# interp. A song with its associated title, artist, acoustincness (A confidence measure from 0.0 to 1.0 of whether the
# track is acoustic), danceability (where 0.0 is least danceable and 1.0 is most danceable), tempo (in beats
# per minute), and valence (A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track)

S0 = Song('Redbone', 'Childish Gambino', 0.199, 0.743, 160.083, 0.588)
S1 = Song('Them Changes (feat. Flying Lotus & Kamasi Washington)', 'Thundercat', 0.555, 0.791, 81.678, 0.733)
S2 = Song('World In Motion', 'New Order', 0.0239, 0.603, 123.922, 0.773)

def fn_for_song(s: Song) -> ...:   # template based on compound
    return...(s.title,             # str
              s.artist,            # str
              s.acousticness,      # float [0.0,1.0]
              s.danceability,      # float [0.0,1.0]
              s.tempo,             # float (0.0...)
              s.valence)           # float [0.0,1.0]

# List[Song]
# interp. a list of Songs

LOS0 = []
LOS1 = [S0, S1]
LOS2 = [S0, S1, S2]

def fn_for_los(los: List[Song]) -> ...: # template from Arbitrary Sized Data and the reference rule
    # acc description
    acc = ...      # type: ...
    for s in los:
        ...(acc, fn_for_song(s))

    return acc

# List[str]
# interp. a list of strings

L0 = []
L1 = ["Jumpman", "Stronger", "Sweet Home Alabama"]

def fn_for_lost(lost: List[str]) -> ...: # template from Arbitrary Sized Data
    # acc description
    acc = ...      # type: ...
    for st in lost:
        ...(acc, st)

    return acc

# List[float]
# interp. a list of floats

LOF0 = []
LOF1 = [0.0,1.1,2.3,3.5,44.3,3.5,6.0]

def fn_for_lof(lof: List[float]) -> ...:  # template from Arbitrary Sized Data
    # acc description
    acc = ...      # type: ...
    for f in lof:
        ...(acc, f)

    return acc

# List[int]
# interp. a list of integers

LOI0 = []
LOI1 = [0,1,2,3]

def fn_for_loi(loi: List[int]) -> ...:  # template from Arbitrary Sized Data
    # acc description
    acc = ...      # type: ...
    for i in loi:
        ...(acc, i)

    return acc
