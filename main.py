
def belongsToFinal(row, col, n) : 
    #         row>2*k - 1 and row < n-k
    isFinal = row>3 and row<n-2
    isFinalLeft = ( col == n-1- (row-4)  ) and isFinal
    isFinalRight = ( col == n-1+(row-4)  ) and isFinal
    isFinalBase = ( ( (row+2) == n-1 ) and ( col%2 == 0 ) and (col>4 and col<2*n-2) )
    
    return ( isFinalLeft or isFinalRight or isFinalBase )
  
def belongsToInner(row, col, n) :
    
    isInner = row>0 and row<n-1
    isInnerLeft = ( col == n-1- (row-2)  ) and isInner
    isInnerRight = ( col == n-1+(row-2)  ) and isInner
    isInnerBase = ( ( (row+1) == n-1 ) and ( col%2 == 1 ) and ( col>2 and col<2*n-1 ) )

    return isInnerLeft or isInnerRight or isInnerBase
    
def belongsToPerimeter(row, col, n) :
    
    isLeft = ( col == n-1-row  )
    isRight = ( col == n-1+row  )
    isBase = ( ( row == n-1 ) and ( col%2 == 0 ) )

    return isLeft or isRight or isBase
   


def condition( row, col, n ) :
    
    case = 0
    
    if( belongsToFinal(row, col, n) ) :
        case = 3
    if( belongsToInner(row, col, n) ) :
        case =  2
    if (belongsToPerimeter(row, col, n) ) :
        case =  1
    
    return case
    
def createCanvas( checkCondition, n ) :
    
    length = n
    height = 2*n - 1
    arr = []
    
    for i in range(length) :
        row = []
        for j in range(height) :
            row.append( checkCondition(i, j, n) )
        arr.append(row)
            
    return arr
        
def printCanvas( arr ) :
    for row in range( len(arr) ) :
        
        for col in range( len(arr[0]) ) :
        
            if ( arr[row][col] == 1  ) : 
                print( "*", end="" )
            
            elif ( arr[row][col] == 2 ) :
                print( "#", end ="" )
                
            elif ( arr[row][col] == 3 ) :
                print( "+", end="" )
            
            else :
                print( " ", end="" )
        
        print("\n")
        
n = 11        
canvas = createCanvas( condition, n )
printCanvas( canvas )

        
