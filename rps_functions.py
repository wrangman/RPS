def gesture(hand):
    if hand == "ROCK":
        print("""
    
  
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/
        """)

    elif hand == "PAPER":
        print("""
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
        """)

    elif hand == "SCISSORS":
        print("""
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
        """)


def get_hand(hand_id):
    if hand_id == "R" or hand_id == "0":
        return "ROCK"
    elif hand_id == "P" or hand_id == "1":
        return "PAPER"
    elif hand_id == "S" or hand_id == "2":
        return "SCISSORS"


def splash_screen(state_of_play):
    if state_of_play == "START":
        print("""
~~~~´'{ W E L C O M E   T O }'`~~~~    
 #####.       #####.    ,##### v1.2   
 ##¨¨¨##      ##¨¨¨##   ##¨¨¨¨      
 #####¨¨      #####¨¨   ¨#####.    
 ##¨¨¨##      ##¨¨¨      ¨¨¨¨##   
 ##   ##  ##  ##     ##  #####¨ ##
 ¨¨   ¨¨  ¨¨  ¨¨     ¨¨  ¨¨¨¨¨  ¨¨
R O C K, P A P E R, S C I S S O R S
~~ Coded by: Johan Wrangö (2022) ~~
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Play against a state-of-the-art, 
next-gen, super-intelligent AI! 
Just hit the corresponding letter""")

    elif state_of_play == "QUIT":
        print("""
...................................
R O C K, P A P E R, S C I S S O R S
~~ Coded by: Johan Wrangö (2022) ~~
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Thanks for playing -- see you soon!""")
