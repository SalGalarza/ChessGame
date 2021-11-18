import pygame
from board import Board
from GraphErrors import GraphFormatError, NoSuchVertexError, DuplicateEdgeError
from pieces import King, Queen, Bishop, Knight, Rook, Pawn
from tile import Tile
from visitors import KingVisitor, QueenVisitor, BishopVisitor, KnightVisitor, RookVisitor, PawnVisitor

pygame.init()
pygame.font.init()
pygame.display.set_caption("Chess")

white = (255,255,255)
red = (255,0,0)

gameExit = False
window = pygame.display.set_mode((800,800)) #
bg = pygame.image.load('large800.jpg')
# bg = pygame.image.load('chess.jpg')
window.blit(bg, (0,0))
font = pygame.font.Font('COMIC.TTF', 25)
title =  font.render('Chess', 1, (0,0,0))
window.blit(title,(360,0))

# pygame.font.init()
# myfont = pygame.font.SysFont('Comic Sans MS', 30)
# textsurface = myfont.render('Chess', False, (0, 0, 0))
# window.blit(textsurface,(0,0))

board = None
xStep = 0
letter = 65
BlackPawns = []
WhitePawns = []
BlackKnights = []
WhiteKnights = []
WhiteRooks = []
BlackRooks = []
WhiteBishops = []
BlackBishops = []
WhiteQueens = []
BlackQueens = []
WhiteKings = []
BlackKings = []

with open("Tiles.txt", "r") as tilesSource :

    try :
        board = Board( tilesSource )
        tile = board.findVertex
        tile("A1").draw(window)


    except GraphFormatError as error :
        print( "Malformed graph file:", error )
    except NoSuchVertexError as error :
        print( "Reference to undefined vertex:", error )
    except DuplicateEdgeError as error:
        print( "Duplicate edge in graph description:", error )

for xcord in range(8):

    xpos = 40 + xStep

    blackTile = chr( 65 + xcord ) + "7"
    BlackPawns.append(Pawn(xpos+15,145,xpos,130,'b',blackTile))
    tile( blackTile ).piece = BlackPawns[xcord]

    whiteTile = chr( 65 + xcord ) + "2"
    WhitePawns.append(Pawn(xpos+15,595,xpos,580,'w',whiteTile))
    tile( whiteTile ).piece = WhitePawns[xcord]

    xStep += 90

BlackKnights.append(Knight(147,57,147,57,'b',"B8"))
tile("B8").piece = BlackKnights[0]
BlackKnights.append(Knight(600,60,600,60,'b',"G8"))
tile("G8").piece = BlackKnights[1]
WhiteKnights.append(Knight(148,688,148,688,'w',"B1"))
tile("B1").piece = WhiteKnights[0]
WhiteKnights.append(Knight(600,692,600,692,'w',"G1"))
tile("G1").piece = WhiteKnights[1]

WhiteRooks.append(Rook(60,690,60,690,'w',"A1"))
tile("A1").piece = WhiteRooks[0]
WhiteRooks.append(Rook(690,690,690,690,'w',"H1"))
tile("H1").piece = WhiteRooks[1]
BlackRooks.append(Rook(60,58,60,58,'b',"A8"))
tile("A8").piece = BlackRooks[0]
BlackRooks.append(Rook(690,58,690,58,'b',"H8"))
tile("H8").piece = BlackRooks[1]

WhiteBishops.append(Bishop(238,695,238,695,'w',"C1"))
tile("C1").piece = WhiteBishops[0]
WhiteBishops.append(Bishop(505,693,505,693,'w',"F1"))
tile("F1").piece = WhiteBishops[1]
BlackBishops.append(Bishop(240,58,240,58,'b',"C8"))
tile("C8").piece = BlackBishops[0]
BlackBishops.append(Bishop(510,56,510,56,'b',"F8"))
tile("F8").piece = BlackBishops[1]

WhiteQueens.append(Queen(328,690,328,690,'w',"D1"))
tile("D1").piece = WhiteQueens[0]
BlackQueens.append(Queen(325,57,325,57,'b',"D8"))
tile("D8").piece = BlackQueens[0]

WhiteKings.append(King(418,685,418,685,'w',"E1"))
tile("E1").piece = WhiteKings[0]
BlackKings.append(King(416,55,416,55,'b',"E8"))
tile("E8").piece = BlackKings[0]

WhiteQueens[0].draw(window)
BlackQueens[0].draw(window)
WhiteKings[0].draw(window)
BlackKings[0].draw(window)

for i in range(2):
    BlackKnights[i].draw(window)
    WhiteKnights[i].draw(window)
    WhiteRooks[i].draw(window)
    BlackRooks[i].draw(window)
    WhiteBishops[i].draw(window)
    BlackBishops[i].draw(window)

for i in range(8):
    BlackPawns[i].draw(window)
    WhitePawns[i].draw(window)

# board.draw( window )


rectangle_draging = False
isBlackTurn = False
isWhiteTurn = True
blackMoved = False
whiteMoved = False
placingDown = False
placingPiece = False
grabbingPiece = True
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            kingV = KingVisitor(board)
            queenV = QueenVisitor(board)
            bishopV = BishopVisitor(board)
            knightV = KnightVisitor(board)
            rookV = RookVisitor(board)
            pawnV = PawnVisitor(board)
            print(event.pos)
            if grabbingPiece:
                grabbingPiece = True
                if event.button == 1 and isBlackTurn:
                    # turn =  font.render('Black', 1, (0,0,0))
                    # window.blit(turn,(360,0))
                    # print(event.pos)
                    for ii in range(8):
                        if BlackPawns[ii].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackPawns[ii].pawn_hold = True  # pawn picked up
                            placingDown = True
                            # Run the traversal
                            pawnV.go( tile(BlackPawns[ii].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackPawns[ii].x - mouse_x
                            offset_y = BlackPawns[ii].y - mouse_y
                        else:
                            pass
                    for k in range(2):
                        if BlackKnights[k].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackKnights[k].knight_hold = True
                            placingDown = True    # knight picked up
                            # Run the traversal
                            knightV.go( tile(BlackKnights[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackKnights[k].x - mouse_x
                            offset_y = BlackKnights[k].y - mouse_y
                        elif BlackRooks[k].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackRooks[k].rook_hold = True  # rook picked up
                            placingDown = True
                            # Run the traversal
                            rookV.go( tile(BlackRooks[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackRooks[k].x - mouse_x
                            offset_y = BlackRooks[k].y - mouse_y
                        elif BlackBishops[k].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackBishops[k].bishop_hold = True  # bishop picked up
                            placingDown = True
                            # Run the traversal
                            bishopV.go( tile(BlackBishops[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackBishops[k].x - mouse_x
                            offset_y = BlackBishops[k].y - mouse_y
                        else:
                            pass
                    for k in range(1):
                        if BlackQueens[k].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackQueens[k].queen_hold = True   # queen picked up
                            placingDown = True
                            # Run the traversal
                            queenV.go( tile(BlackQueens[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackQueens[k].x - mouse_x
                            offset_y = BlackQueens[k].y - mouse_y
                        elif BlackKings[k].collidepoint(event.pos,window) and isBlackTurn:
                            rectangle_draging = True
                            BlackKings[k].king_hold = True  # king picked up
                            placingDown = True
                            # Run the traversal
                            kingV.go( tile(BlackKings[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = BlackKings[k].x - mouse_x
                            offset_y = BlackKings[k].y - mouse_y
                        else:
                            pass
                elif event.button == 1 and isWhiteTurn:
                    # turn =  font.render('White', 1, (0,0,0))
                    # window.blit(turn,(360,0))
                    for ii in range(8):
                        if WhitePawns[ii].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhitePawns[ii].pawn_hold = True
                            placingDown = True
                            print(WhitePawns[ii].tile)
                            pawnV.go( tile(WhitePawns[ii].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhitePawns[ii].x - mouse_x
                            offset_y = WhitePawns[ii].y - mouse_y
                        else:
                            pass
                    for k in range(2):
                        if WhiteKnights[k].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhiteKnights[k].knight_hold = True
                            placingDown = True
                            knightV.go( tile(WhiteKnights[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhiteKnights[k].x - mouse_x
                            offset_y = WhiteKnights[k].y - mouse_y
                        elif WhiteRooks[k].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhiteRooks[k].rook_hold = True
                            placingDown = True
                            rookV.go( tile(WhiteRooks[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhiteRooks[k].x - mouse_x
                            offset_y = WhiteRooks[k].y - mouse_y
                        elif WhiteBishops[k].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhiteBishops[k].bishop_hold = True
                            placingDown = True
                            bishopV.go( tile(WhiteBishops[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhiteBishops[k].x - mouse_x
                            offset_y = WhiteBishops[k].y - mouse_y
                        else:
                            pass
                    for k in range(1):
                        if WhiteQueens[k].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhiteQueens[k].queen_hold = True
                            placingDown = True
                            queenV.go( tile(WhiteQueens[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhiteQueens[k].x - mouse_x
                            offset_y = WhiteQueens[k].y - mouse_y
                        elif WhiteKings[k].collidepoint(event.pos,window) and isWhiteTurn:
                            rectangle_draging = True
                            WhiteKings[k].king_hold = True
                            placingDown = True
                            kingV.go( tile(WhiteKings[k].tile) )
                            mouse_x, mouse_y = event.pos
                            offset_x = WhiteKings[k].x - mouse_x
                            offset_y = WhiteKings[k].y - mouse_y
                        else:
                            pass
            else:
                print("Passed")

        elif event.type == pygame.MOUSEBUTTONUP:
            # check if piece held is being placed on new tile
            print(whiteMoved)
            if placingPiece:
                placingPiece = False
                placingDown = False
                for BlackPawn in BlackPawns:
                    if BlackPawn.pawn_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackPawn.pawn_hold = False
                                if BlackPawn.tile == ttile.name:        # check if placed on OG tile
                                    print("OG")
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    print("Kill")
                                    # ttile.piece.visible = False #remove
                                    tile(BlackPawn.tile).piece = None
                                    BlackPawn.tile = ttile.name
                                    ttile.piece = BlackPawn                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    print("New")
                                    tile(BlackPawn.tile).piece = None
                                    BlackPawn.tile = ttile.name
                                    ttile.piece = BlackPawn
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackPawn.pawn_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for BlackKnight in BlackKnights:
                    if BlackKnight.knight_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackKnight.knight_hold = False
                                if BlackKnight.tile == ttile.name:        # check if placed on OG tile
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(BlackKnight.tile).piece = None
                                    BlackKnight.tile = ttile.name
                                    ttile.piece = BlackKnight
                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(BlackKnight.tile).piece = None
                                    BlackKnight.tile = ttile.name
                                    ttile.piece = BlackKnight
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackKnight.knight_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for BlackRook in BlackRooks:
                    if BlackRook.rook_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackRook.rook_hold = False
                                if BlackRook.tile == ttile.name:        # check if placed on OG tile
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(BlackRook.tile).piece = None
                                    BlackRook.tile = ttile.name
                                    ttile.piece = BlackRook
                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(BlackRook.tile).piece = None
                                    BlackRook.tile = ttile.name
                                    ttile.piece = BlackRook
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackRook.rook_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for BlackBishop in BlackBishops:
                    if BlackBishop.bishop_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackBishop.bishop_hold = False
                                if BlackBishop.tile == ttile.name:        # check if placed on OG tile
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(BlackBishop.tile).piece = None
                                    BlackBishop.tile = ttile.name
                                    ttile.piece = BlackBishop
                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(BlackBishop.tile).piece = None
                                    BlackBishop.tile = ttile.name
                                    ttile.piece = BlackBishop
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackBishop.bishop_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for BlackQueen in BlackQueens:
                    if BlackQueen.queen_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackQueen.queen_hold = False
                                if BlackQueen.tile == ttile.name:        # check if placed on OG tile
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(BlackQueen.tile).piece = None
                                    BlackQueen.tile = ttile.name
                                    ttile.piece = BlackQueen
                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(BlackQueen.tile).piece = None
                                    BlackQueen.tile = ttile.name
                                    ttile.piece = BlackQueen
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackQueen.queen_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for BlackKing in BlackKings:
                    if BlackKing.king_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                BlackKing.king_hold = False
                                if BlackKing.tile == ttile.name:        # check if placed on OG tile
                                    blackMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(BlackKing.tile).piece = None
                                    BlackKing.tile = ttile.name
                                    ttile.piece = BlackKing
                                    blackMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(BlackKing.tile).piece = None
                                    BlackKing.tile = ttile.name
                                    ttile.piece = BlackKing
                                    blackMoved = True
                                    grabbingPiece = True
                                else:
                                    BlackKing.king_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board

                for WhitePawn in WhitePawns:
                    if WhitePawn.pawn_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhitePawn.pawn_hold = False
                                if WhitePawn.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    print("kill")
                                    # ttile.piece.visible = False #remove
                                    tile(WhitePawn.tile).piece = None
                                    WhitePawn.tile = ttile.name
                                    ttile.piece = WhitePawn
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    print("moved")
                                    tile(WhitePawn.tile).piece = None
                                    WhitePawn.tile = ttile.name
                                    ttile.piece = WhitePawn
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhitePawn.pawn_hold = True
                                    print("Invalid Move")
                                    # WhitePawn.pawn_hold = True
                                    # whiteMoved = False
                            else:
                                pass         # not on board
                for WhiteKnight in WhiteKnights:
                    if WhiteKnight.knight_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhiteKnight.knight_hold = False
                                if WhiteKnight.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(WhiteKnight.tile).piece = None
                                    WhiteKnight.tile = ttile.name
                                    ttile.piece = WhiteKnight
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(WhiteKnight.tile).piece = None
                                    WhiteKnight.tile = ttile.name
                                    ttile.piece = WhiteKnight
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhiteKnight.knight_hold = True
                                    pass # invalid move
                            else:
                                pass         # not on board
                for WhiteRook in WhiteRooks:
                    if WhiteRook.rook_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhiteRook.rook_hold = False
                                if WhiteRook.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(WhiteRook.tile).piece = None
                                    WhiteRook.tile = ttile.name
                                    ttile.piece = WhiteRook
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(WhiteRook.tile).piece = None
                                    WhiteRook.tile = ttile.name
                                    ttile.piece = WhiteRook
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhiteRook.rook_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for WhiteBishop in WhiteBishops:
                    if WhiteBishop.bishop_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhiteBishop.bishop_hold = False
                                if WhiteBishop.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(WhiteBishop.tile).piece = None
                                    WhiteBishop.tile = ttile.name
                                    ttile.piece = WhiteBishop
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(WhiteBishop.tile).piece = None
                                    WhiteBishop.tile = ttile.name
                                    ttile.piece = WhiteBishop
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhiteBishop.bishop_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for WhiteQueen in WhiteQueens:
                    if WhiteQueen.queen_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhiteQueen.queen_hold = False
                                if WhiteQueen.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(WhiteQueen.tile).piece = None
                                    WhiteQueen.tile = ttile.name
                                    ttile.piece = WhiteQueen
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(WhiteQueen.tile).piece = None
                                    WhiteQueen.tile = ttile.name
                                    ttile.piece = WhiteQueen
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhiteQueen.queen_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
                for WhiteKing in WhiteKings:
                    if WhiteKing.king_hold == True:
                        for ttile in board.tiles.values():
                            if ttile.collidepoint(event.pos, window):
                                WhiteKing.king_hold = False
                                print(WhiteKing.tile)
                                print(ttile.name)
                                ttile.draw(window)
                                if WhiteKing.tile == ttile.name:        # check if placed on OG tile
                                    whiteMoved = False
                                elif ttile.mark and (ttile.piece != None):  # able to move and piece in new location
                                    ttile.piece.visible = False #remove
                                    tile(WhiteKing.tile).piece = None
                                    WhiteKing.tile = ttile.name
                                    ttile.piece = WhiteKing
                                    whiteMoved = True
                                    grabbingPiece = True
                                elif ttile.mark:
                                    tile(WhiteKing.tile).piece = None
                                    WhiteKing.tile = ttile.name
                                    ttile.piece = WhiteKing
                                    whiteMoved = True
                                    grabbingPiece = True
                                else:
                                    WhiteKing.king_hold = True
                                    print("Invalid Move")
                                    pass # invalid move
                            else:
                                pass         # not on board
            if placingDown:
                placingPiece = True
            # black and white moved == true

            # if piece valud and no action other than place piece
            if event.button == 1 and isBlackTurn and blackMoved:
                rectangle_draging = False
                isBlackTurn = False
                isWhiteTurn = True
                blackMoved = False
                turn =  font.render('White', 1, (0,0,0))
                window.blit(turn,(360,0))
                for BlackPawn in BlackPawns:
                    BlackPawn.pawn_hold = False
                for BlackKnight in BlackKnights:
                    BlackKnight.knight_hold = False
                for BlackRook in BlackRooks:
                    BlackRook.rook_hold = False
                for BlackBishop in BlackBishops:
                    BlackBishop.bishop_hold = False
                for BlackQueen in BlackQueens:
                    BlackQueen.queen_hold = False
                for BlackKing in BlackKings:
                    BlackKing.king_hold = False
                mouse_x = 0
                mouse_y = 0
                offset_x = 0
                offset_y = 0
                # print(BlackPawns[0].pawn_hold)
                # print(BlackPawns[1].pawn_hold)

                # del BlackPawns[curentPawnID]
                # BlackPawns.append(pawns)
            elif event.button == 1 and isWhiteTurn and whiteMoved:
                rectangle_draging = False
                isWhiteTurn = False
                isBlackTurn = True
                whiteMoved = False
                turn =  font.render('Black', 1, (0,0,0))
                window.blit(turn,(360,0))
                for WhitePawn in WhitePawns:
                    WhitePawn.pawn_hold = False
                for WhiteKnight in WhiteKnights:
                    WhiteKnight.knight_hold = False
                for WhiteRook in WhiteRooks:
                    WhiteRook.rook_hold = False
                for WhiteBishop in WhiteBishops:
                    WhiteBishop.bishop_hold = False
                for WhiteQueen in WhiteQueens:
                    WhiteQueen.queen_hold = False
                for WhiteKing in WhiteKings:
                    WhiteKing.king_hold = False
                mouse_x = 0
                mouse_y = 0
                offset_x = 0
                offset_y = 0

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging and isBlackTurn:
                # BlackPawns[0].draw(window)
                window.blit(bg, (0,0))
                # turn =  font.render('Black', 1, (0,0,0))
                # window.blit(turn,(360,0))
                for i in range(8):
                    BlackPawns[i].draw(window)
                    WhitePawns[i].draw(window)
                for i in range(2):
                    BlackKnights[i].draw(window)
                    WhiteKnights[i].draw(window)
                    WhiteRooks[i].draw(window)
                    BlackRooks[i].draw(window)
                    WhiteBishops[i].draw(window)
                    BlackBishops[i].draw(window)
                WhiteQueens[0].draw(window)
                BlackQueens[0].draw(window)
                WhiteKings[0].draw(window)
                BlackKings[0].draw(window)

                index = 0
                for pawns in BlackPawns:
                    if pawns.pawn_hold == True:
                        # blackMoved = True
                        curentPawnID = index
                        mouse_x, mouse_y = event.pos
                        pawns.x = mouse_x + offset_x
                        pawns.y = mouse_y + offset_y
                        pawns.hitbox[0] = pawns.x
                        pawns.hitbox[1] = pawns.y
                        # print(pawns.x)
                for knights in BlackKnights:
                    if knights.knight_hold == True:
                        # blackMoved = True
                        curentKnightID = index
                        mouse_x, mouse_y = event.pos
                        knights.x = mouse_x + offset_x
                        knights.y = mouse_y + offset_y
                        knights.hitbox[0] = knights.x
                        knights.hitbox[1] = knights.y
                for rooks in BlackRooks:
                    if rooks.rook_hold == True:
                        # blackMoved = True
                        curentRookID = index
                        mouse_x, mouse_y = event.pos
                        rooks.x = mouse_x + offset_x
                        rooks.y = mouse_y + offset_y
                        rooks.hitbox[0] = rooks.x
                        rooks.hitbox[1] = rooks.y
                for bishops in BlackBishops:
                    if bishops.bishop_hold == True:
                        # blackMoved = True
                        curentBishopID = index
                        mouse_x, mouse_y = event.pos
                        bishops.x = mouse_x + offset_x
                        bishops.y = mouse_y + offset_y
                        bishops.hitbox[0] = bishops.x
                        bishops.hitbox[1] = bishops.y
                for queens in BlackQueens:
                    if queens.queen_hold == True:
                        # blackMoved = True
                        curentQueenID = index
                        mouse_x, mouse_y = event.pos
                        queens.x = mouse_x + offset_x
                        queens.y = mouse_y + offset_y
                        queens.hitbox[0] = queens.x
                        queens.hitbox[1] = queens.y
                for kings in BlackKings:
                    if kings.king_hold == True:
                        # blackMoved = True
                        curentQueenID = index
                        mouse_x, mouse_y = event.pos
                        kings.x = mouse_x + offset_x
                        kings.y = mouse_y + offset_y
                        kings.hitbox[0] = kings.x
                        kings.hitbox[1] = kings.y
                index += 1
            elif rectangle_draging and isWhiteTurn:
                    # BlackPawns[0].draw(window)
                    window.blit(bg, (0,0))
                    # turn =  font.render('White', 1, (0,0,0))
                    # window.blit(turn,(360,0))
                    for i in range(8):
                        BlackPawns[i].draw(window)
                        WhitePawns[i].draw(window)
                    for i in range(2):
                        BlackKnights[i].draw(window)
                        WhiteKnights[i].draw(window)
                        WhiteRooks[i].draw(window)
                        BlackRooks[i].draw(window)
                        WhiteBishops[i].draw(window)
                        BlackBishops[i].draw(window)
                    WhiteQueens[0].draw(window)
                    BlackQueens[0].draw(window)
                    WhiteKings[0].draw(window)
                    BlackKings[0].draw(window)
                    index = 0
                    for pawns in WhitePawns:
                        if pawns.pawn_hold == True:
                            # whiteMoved = True
                            curentPawnID = index
                            mouse_x, mouse_y = event.pos
                            pawns.x = mouse_x + offset_x
                            pawns.y = mouse_y + offset_y
                            pawns.hitbox[0] = pawns.x
                            pawns.hitbox[1] = pawns.y
                            # print(pawns.x)
                    for knights in WhiteKnights:
                        if knights.knight_hold == True:
                            # whiteMoved = True
                            curentKnightID = index
                            mouse_x, mouse_y = event.pos
                            knights.x = mouse_x + offset_x
                            knights.y = mouse_y + offset_y
                            knights.hitbox[0] = knights.x
                            knights.hitbox[1] = knights.y
                    for rooks in WhiteRooks:
                        if rooks.rook_hold == True:
                            # whiteMoved = True
                            curentRookID = index
                            mouse_x, mouse_y = event.pos
                            rooks.x = mouse_x + offset_x
                            rooks.y = mouse_y + offset_y
                            rooks.hitbox[0] = rooks.x
                            rooks.hitbox[1] = rooks.y
                    for bishops in WhiteBishops:
                        if bishops.bishop_hold == True:
                            # whiteMoved = True
                            curentBishopID = index
                            mouse_x, mouse_y = event.pos
                            bishops.x = mouse_x + offset_x
                            bishops.y = mouse_y + offset_y
                            bishops.hitbox[0] = bishops.x
                            bishops.hitbox[1] = bishops.y
                    for queens in WhiteQueens:
                        if queens.queen_hold == True:
                            # whiteMoved = True
                            curentQueenID = index
                            mouse_x, mouse_y = event.pos
                            queens.x = mouse_x + offset_x
                            queens.y = mouse_y + offset_y
                            queens.hitbox[0] = queens.x
                            queens.hitbox[1] = queens.y
                    for kings in WhiteKings:
                        if kings.king_hold == True:
                            # whiteMoved = True
                            curentQueenID = index
                            mouse_x, mouse_y = event.pos
                            kings.x = mouse_x + offset_x
                            kings.y = mouse_y + offset_y
                            kings.hitbox[0] = kings.x
                            kings.hitbox[1] = kings.y
                    index += 1


    pygame.display.flip()
