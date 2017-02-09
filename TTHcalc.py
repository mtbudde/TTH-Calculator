# Toy Tetragram Hash function
# Matthew Budde
# 2.9.17

def rotate( row, positions ):
    rotation = positions
    rotated = ''
    for i in range( len( row ) ):
        rotated += row[ ( rotation + i ) % len( row ) ]
    return rotated

def flip( row ):
    flipped = ''
    for i in range( len( row ) - 1, -1, -1 ):
        flipped += row[i]
    return flipped

def TTH( message ):
    rows = []
    transformedRows = []
    TTHresult = []

    # Pad the message out to a multiple of 16
    if( len( message ) % 16 != 0 ):
        for i in range( len( message ) % 16 ):
            message += 'a'

    # Split the message into tetragrams and rotate/flip the rows
    # based on the TTH rotate/flip pattern
    for i in range( 0, len( message ) - 3, 4 ):
        rows.append( message[i:i+4] )
        case = ( i / 4 ) % 4
        if( case == 0 ):
            transformedRows.append( rotate( message[i:i+4], 1 ) )
        elif( case == 1 ):
            transformedRows.append( rotate( message[i:i+4], 2 ) )
        elif( case == 2 ):
            transformedRows.append( rotate( message[i:i+4], 3 ) )
        else:
            transformedRows.append( flip( message[i:i+4] ) )

    # Compute the hash by summing up the columns of the normal and transformed
    # rows mod 26 and convert the totals back to characters
    runningtotals = [0, 0, 0, 0]
    for i in range( 4 ):
        for j in range( len( rows ) ):
            runningtotals[i] += ord( rows[j][i] ) + ord( transformedRows[j][i] ) - 194
        runningtotals[i] = runningtotals[i] % 26
        TTHresult.append( chr( runningtotals[i] + 97 ) )
    return TTHresult

message = raw_input( 'Enter the message to hash (no spaces): ' )
message = message.lower()
print( TTH( message ) )
