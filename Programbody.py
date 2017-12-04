# Program Body

def check_tempo(s: Song, t: float) -> bool:
    '''
    Return True if the inputted song's tempo (s.tempo) is greater than or equal to the inputted float (0.0...)in beats
    per minute (BPM)
    '''
    # return True        # Body of Stub
    # return...(s, t)    # Template based on function composition for float
    if s.tempo >= t:
        return True
    else:
        return False

def create_song_list(los: List[Song], t: float) -> List[Song]:
    '''
    Given a list of songs, return a list of songs that have a tempo (s.tempo) greater than or equal to the
    inputted floats for tempo (t)
    '''
    # return []  # body of stub
    # template from List[Song] with one other float input
    # acc stores songs that meet the criteria so far
    acc = []      # type: List[Song]
    for s in los:
        if check_tempo(s, t)== True:
            acc.append(s)
        else:
            acc
    return acc

def list_valence(los: List[Song]) -> List[float]:
    '''
    Given a list of Songs, extract a list of the songs valences
    '''
    # return []  # Body of Stub
    # template from List[Song]
    # valences stores songs' valences so far
    valences = []      # type: List[float]
    for s in los:
            valences.append(s.valence)
    return valences

def list_title(los: List[Song]) -> List[str]:
    '''
    Given a list of Songs, extract a list of the songs titles
    '''
    # return []  # Body of Stub
    # template from List[Song]
    # titles stores song names so far
    titles = []      # type: List[str]
    for s in los:
        titles.append(s.title)
    return titles

def shorten_list_25(los: List[Song]) -> List[Song]:
    '''
    Given a list of songs, take the first 25 Songs into a new list
    '''
    # return []    # Body of the stub
    # template based on a call to a primitive list operator
    return los[:24]

def ascending_int_list(los: List[Song]) -> List[int]:
    '''
    Given a list of songs, create a list of n ascending integers (ex. [0,1,2,3,4,5,6]) where n is the number of songs
    in the inputted list
    '''
    # return []    # Body of the stub
    # template based on a call to a primitive list operator
    return list(range(len(los)))

def plot_valence_song(los: List[Song]) -> None:
    """
    Display a scatter plot of 25 songs with their corresponding titles (x axis) and valences (y axis)
    """
    # return None # body of the stub

    # set the x-axis label, y-axis label, and plot title
    pyplot.xlabel('Songs With Tempo Greater Than Input')
    pyplot.ylabel('Valence [0.0,1.0]')
    pyplot.title('Valence of Songs With Tempo Greater Than Input')

    # If list is longer than 25 songs, shorter list of songs to 25
    songs = shorten_list_25(los)

    # plot our data

    scatter = pyplot.scatter(ascending_int_list(songs), list_valence(songs), marker="o", s=100, color=('b', 'g', 'r', 'c', 'm', 'y', 'k'))

    # Set titles as labels on the x axis
    pyplot.xticks(ascending_int_list(songs), list_title(songs), rotation='vertical')

    # show the plot
    pyplot.show()

    return None

def main(filename: str, tempo: float) -> None:
    '''
    Given a filename and a tempo (0.0...), return a plot of the valences of 25 songs that have a tempo greater than
    the inputted float
    '''
    # template based on function composition
    return plot_valence_song(create_song_list(read(filename), tempo))

#Begin Testing
start_testing()

# Examples for check_tempo
expect(check_tempo(S0, 300), False)
expect(check_tempo(S1, 100), False)
expect(check_tempo(S0, 100), True)

# Examples for create_song_list
expect(create_song_list(LOS0, 100), [])
expect(create_song_list(LOS1, 100), [S0])
expect(create_song_list(LOS2, 100), [S0, S2])

# Examples for list_valence
expect(list_valence(LOS0), [])
expect(list_valence(LOS1), [0.588, 0.733])
expect(list_valence(LOS2), [0.588, 0.733, 0.773])

# Examples for list_title
expect(list_title(LOS0), [])
expect(list_title(LOS1), ["Redbone", "Them Changes (feat. Flying Lotus & Kamasi Washington)"])
expect(list_title(LOS2), ["Redbone", "Them Changes (feat. Flying Lotus & Kamasi Washington)", "World In Motion"])

# Examples for shorten_list 25
expect(shorten_list_25(LOS0), [])
expect(shorten_list_25(LOS1), [S0, S1])
expect(shorten_list_25(LOS2), [S0, S1, S2])

# Examples for ascending_int_list
expect(ascending_int_list(LOS0), [])
expect(ascending_int_list(LOS1), [0,1])
expect(ascending_int_list(LOS2), [0,1,2])

# Examples for plot_valence_song
expect(plot_valence_song(LOS0), None)
expect(plot_valence_song(LOS1), None)
expect(plot_valence_song(LOS2), None)

# Examples for main
main('spotifydata.csv', 10)
main('spotifydata.csv', 100)
main('spotifydata.csv', 150)

summary()
