#!/usr/bin/python3

# 2015

import random
import os

class londy(object):
	def __init__(self):
		suits = ['diamond', 'clubs', 'spades', 'hearts']
		numbs = ['2','3','4','5','6','7','8','9', '10', 'jack','queen','king','ace']
		self.cards = []
		self.df = 0

		for suit in suits:
			for numb in numbs:
				self.cards.append(numb + ' of ' + suit)

	def dec(self, number_of_cards):
		random.shuffle(self.cards)
		list_of_cards = []
		while number_of_cards:
			list_of_cards.append( self.cards.pop() )
			number_of_cards -= 1
		return list_of_cards

	def count_score(self, tcards):
		
		score = {'clubs': 0, 'pictures': 0}

		for card in tcards:
			if 'clubs' in card:
				score['clubs'] += 1
			elif card[0] in "jqk":
				score['pictures'] += 1

		return score

	# plc player cards
	# pcc pc cards
	# select a card that user does'nt have
	def ccard(self, plc, pcc):

		if self.df == 1:
			return random.choice(pcc)
		
		select_from = []

		for x in pcc:
			status = False
			for z in plc:
				if x[0] == z[0]:
					status = True
			if status == False:
				select_from.append(x)

		# user has all of our cards
		if select_from == []:
			return random.choice(pcc)

		if self.df == 2 or len(self.cards) < 10:
			return random.choice(select_from)

		# so df is 3
		tmp = select_from
		select_from = []

		for x in tmp:
			status = False
			c = -1
			while c > -5:
				if x[0] == self.cards[c][0]:
					status = True		
				c -= 1

			if status == False:
				select_from.append(x)

		if select_from != []:
			return random.choice( select_from )
		else:
			return random.choice(pcc)


# ------------------------------------------------------------------------->

find_status = False # switch for the times pc don't haeve a right card
player_score = 0 # times player won
pc_score = 0 # times pc won
cards_count = 52 # num of cards for loop into turns
cpt = []# cards player taked
cct = []# cards computer taked
cs = 0 # number of computer sours
ps = 0 # number of player sours

game = londy()

while game.df < 1 or game.df > 3:
	game.df = int( input("{1}Easy\n{2}Hard\n{3}Kill me\n:") )

# dec 4 card on the ground
cards = game.dec(4)

cards_count -= 4

while cards_count: 

	# dec for player
	player_cards = game.dec(4)
	
	# dec for computer
	pc_cards = game.dec(4)

	cards_count -= 8

	# 4 times counter
	f = 4
	while f:
		# Show the topest card
		if len(cards) > 0:
			print("top card: " + cards[-1])
		else:
			print("no card on the table");
		
		# show player cards
		print("\nyour cards:")

		c_counter = 1
		for c in player_cards:
			print( "{" + str(c_counter) + "} " + c)
			c_counter +=1

		# player select a card
		selected_card_id = 0
		while selected_card_id < 1 or selected_card_id > len(player_cards):
			selected_card_id = int( input('select your card: ') )

		selected_card = player_cards[selected_card_id -1]

		if cards == []:
			cards.append(selected_card)
		else:
			# if selected card == top card ([1] of spades == [1] of clubs)
			if selected_card[0] == cards[-1][0]:
				player_score += 1
				# Sour
				if len(cards) == 1:
					ps += 1
				cpt += cards
				cards = []
			else:
				# put the card on the others
				cards.append(selected_card)

		# remove the selected cards from player cards
		player_cards.remove(selected_card)

		os.system("clear")

		# computer turn, show the top card
		if len(cards) > 0:
			print("\nComputer turn-->\ntop card: " + cards[-1])
		else:
			print("\nComputer turn-->\nno card on the table");

		if cards == []:
			selected_card = game.ccard(player_cards, pc_cards)
			cards.append( selected_card )
			pc_cards.remove( selected_card )
			print("Computer played: " + selected_card )
		else:
			# loop into computer cards
			for x in pc_cards:
				# if computer had the top card
				# [1] of spade == [1] of clubs
				if x[0] == cards[-1][0]:
					selected_card = x
					print("Computer played: " + selected_card)
					# Sour
					if len(cards) == 1:
						cs += 1
					cct += cards
					cards = []
					pc_score += 1
					pc_cards.remove(selected_card)
					find_status = True
					break
			
			if find_status == False:

				selected_card = game.ccard(player_cards, pc_cards)
				cards.append( selected_card )
				pc_cards.remove( selected_card )
				print("Computer played: " + selected_card )

			find_status = False

			print("Number of cards on the table: " + str(len(cards)))

		# f-- [ while counter ]
		f -= 1


# Counting clubs for player
score = game.count_score(cpt)
print("\n\nPlayer Score:")
print("Won: " + str(player_score) + " times")
print(str(score['clubs']) + " Clubs");
print(str(score['pictures']) + " Pictures");
print("sour: " + str(ps))

# Counting clubs for computer
score = game.count_score(cct)
print("\n\nComputer Score:")
print("Won: " + str(pc_score) + " times" )
print(str(score['clubs']) + " Clubs");
print(str(score['pictures']) + " Pictures");
print("sour: " + str(cs))

input("press return to exit")
