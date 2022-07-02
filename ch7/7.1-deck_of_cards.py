# We will assume that this is blackjack against an NPC. 

# CLASS: DECK OF CARDS

# ATTRIBUTES:
# - Pulled Cards
# - Available Cards Left

# ===============================================================

# CLASS: GAME OF BLACKJACK:

# ATTRIBUTES:
# PLAYERPOINTS = 0
# NPCPOINTS = 0

# FUNCTION SUMCARDS:
# Because there is a discrepancy between Aces and Jacks, custom summing function for the cards.

# FUNCTION DRAW: 
# The player will draw a random card.
# If the NPC is less than 5 away from hitting 21, they won't draw. 
# Otherwise, the NPC will draw one card.
# If the player has exceeded 21 cards, it will assess between whether the NPC or player won, lost, or tied. 

# FUNCTION FOLD:
# The player will then fold. 
# The NPC will then go through a while loop, such that the sum of their cards never exceed 18 (for example)
# Then in the loop, the NPC will keep drawing cards. 
# It will then call the function to win. 

# FUNCTION RESULT:
# Will take in the person who wins. 
# Points will be updated. 
# The CARD class will be reset with nothing in pulled, and the full deck of cards there. 