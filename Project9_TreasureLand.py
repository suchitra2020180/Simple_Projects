#Project9  Treasure land
###images are taken from ascii.co.uk/art


print("Welcome to Treasure land game")
print("Your mission is to find the treasure")
move=input("Now you are at cross road and where do  you want to move left or right:")

if move=='left':
    decision=input("You reached a lake. There is an island in the middle of the lake. Do you want to swim or wait?")
    if decision=='wait':
        door=input("There are different doors here. Select  a suitable door with gives path to treasure: ")
        if door=='red':
            print('''               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
            print("Burnt and game over")
        elif door=='yellow':
            print("WON the game")
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
        elif door=='blue':
            print(''' 
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
 ''')
            print("Eaten by beasts and game over ")
        else:
            
            print("GAME OVER")

    else:
        print('''          .----.                         ,----,
   ____    __\\\\\\__                  ___//////__    ____
   \___'--"          .-.            .-.           "--'___/
   /___<             '0'            '0'              >___\
  /____,--.       y     B          8     q        ,--.____\
          "".____  ___-"            "-___  ____,""
          //    / /                      \ \   \\     cgmm
                ]/   cgmm                 \[     
   ''')
        print("Atttacked by trout and game over")

else:
    print('''                                      +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \
             \                    \        \
              +-----------------------------+''')
    print("Fall into and game over")