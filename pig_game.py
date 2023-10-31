#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:46:17 2020

@author: will
"""

import random


def pig_game(c1_total = 0, c2_total = 0, c3_total = 0, h1_total = 0, h2_total = 0):
    game_choice = input('Hello!\nWhat type of game would you like to play?\nPress \"i\" for more information on the game types.\n')
    if game_choice != 'cvc' and game_choice != 'hvc' and game_choice != 'i' and game_choice != 'hvh':
        print('Error\nPlease input a game type or press \"i\" for information.')
        game_choice = input('Which game type would you like to play?\n')
    if game_choice == 'i':
        game_types = 'Game Types:\n     Computer vs. Computer (cvc)\n     Human vs. Computer (hvc)\n     Human vs. Human (hvh)'
        print(game_types)
        game_choice = input('Which game type would you like to play?\n')
    if game_choice == 'cvc':
        play_cvc()
    elif game_choice == 'hvc':
        play_hvc()
    elif game_choice == 'hvh':
        play_hvh()
    else:
        print('\nPlease enter a valid game choice.\nValid choices are \"cvc,\" \"hvc,\" and \"hvh.\"')
        pig_game()
    
def dice_roll():
    roll = random.randint(1,6)
    return roll

def play_cvc(c1_total = 0, c2_total = 0, c3_total = 0, c4_total = 0):
    player1 = pick_computer()
    player2 = pick_computer()
    if player1 == player2:
        player2 = pick_computer()
    if (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 1):
        print(f'\nThe players are Computer 1 and Computer 2')
        while c1_total < 100 and c2_total < 100:
            c1_total = c1_strat(c1_total)
            c2_total = c2_strat(c2_total)
        return check_win('Computer 1', 'Computer 2', c1_total, c2_total)
    elif (player1 == 1 and player2 == 3) or (player1 == 3 and player2 == 1):
        print(f'\nThe players are Computer 1 and Computer 3')
        while c1_total < 100 and c3_total < 100:
            c1_total = c1_strat(c1_total)
            c3_total = c3_strat(c3_total)
        return check_win('Computer 1', 'Computer 3', c1_total, c3_total)
    elif (player1 == 3 and player2 == 2) or (player1 == 2 and player2 == 3):
        print(f'\nThe players are Computer 2 and Computer 3')
        while c3_total < 100 and c2_total < 100:
            c3_total = c3_strat(c3_total)
            c2_total = c2_strat(c2_total)
        return check_win('Computer 3', 'Computer 2', c3_total, c2_total)
    elif (player1 == 1 and player2 == 4) or (player1 == 4 and player2 ==1):
        print(f'\nThe players are Computer 1 and Computer 4')
        while c1_total < 100 and c4_total < 100:
            c1_total = c1_strat(c1_total)
            c4_total = c4_strat(c4_total, c1_total)
        return check_win('Computer 1', 'Computer 4', c1_total, c4_total)
    elif (player1 == 2 and player2 == 4) or (player1 == 4 and player2 == 2):
        print(f'\nThe players are Computer 2 and Computer 4')
        while c2_total < 100 and c4_total < 100:
            c2_total = c2_strat(c2_total)
            c4_total = c4_strat(c4_total, c2_total)
        return check_win('Computer 2', 'Computer 4', c2_total, c4_total)
    elif (player1 == 3 and player2 == 4) or (player1 == 4 and player2 == 3):
        print(f'\nThe players are Computer 3 and Computer 4')
        while c3_total < 100 and c4_total < 100:
            c3_total = c3_strat(c3_total)
            c4_total = c4_strat(c4_total, c3_total)
        return check_win('Computer 3', 'Computer 4', c3_total, c4_total)

def play_hvc(c1_total = 0, c2_total = 0, c3_total = 0, c4_total = 0, h1_total = 0):
    choice = input('\nWould you like to choose your opponent or play a random computer?\nPlease type \"Choose\" or \"Random\"\n').lower()
    if choice == 'choose':
        player = int(input('\nPlease enter the opponent number.\nType 1, 2, 3, or 4\n'))
        if player != 1 and player != 2 and player != 3 and player != 4:
            player = int(input('\nError!\nPlease enter a number between 1 and 4\n'))
    elif choice == 'random':
        player = pick_computer()
    else:
        choice = input('\nError!\nPlease enter \"Choose\" or \"Random\"\n').lower()
        if choice == 'choose':
            player = int(input('\nPlease enter the opponent number.\nType 1, 2, 3, or 4\n'))
            if player != 1 and player != 2 and player != 3 and player != 4:
                player = int(input('\nError!\nPlease enter a number between 1 and 4\n'))
        elif choice == 'random':
            player = pick_computer()
    print(f'\nYour opponent is Computer {player}.')
    if player == 1:
        while h1_total < 100 and c1_total < 100:
            h1_total = h1_play(h1_total, c1_total)
            c1_total = c1_strat(c1_total)
        return check_win('Human', 'Computer 1', h1_total, c1_total)
    elif int(player) == 2:
        while h1_total < 100 and c2_total < 100:
            h1_total = h1_play(h1_total, c2_total)
            c2_total = c2_strat(c2_total)
        return check_win('Human', 'Computer 2', h1_total, c2_total)
    elif int(player) == 3:
        while h1_total < 100 and c3_total < 100:
            h1_total = h1_play(h1_total, c3_total)
            c3_total = c3_strat(c3_total)
        return check_win('Human', 'Computer 3', h1_total, c3_total)
    elif int(player) == 4:
        while h1_total < 100 and c4_total < 100:
            h1_total = h1_play(h1_total, c4_total)
            c4_total = c4_strat(c4_total, h1_total)
        return check_win('Human', 'Computer 4', h1_total, c4_total)

def play_hvh(h1_total = 0, h2_total = 0):
    while h1_total < 100 and h2_total < 100:
        print('\n\n\n\
              Player one turn')
        h1_total = h1_play(h1_total, h2_total)
        print('\n\n\n\
              Player two turn')
        h2_total = h2_play(h2_total, h1_total)
    return check_win('Human 1', 'Human 2', h1_total, h2_total)

def c1_strat(c1_total):
    turn_total = 0
    roll_count = 0
    while c1_total + turn_total < 100:
        if c1_total <= 75:
            if roll_count <= 3:
                r = dice_roll()
                if r == 1:
                    turn_total = 0
                    roll_count = 0
                    return c1_total
                else:
                    turn_total = turn_total + r
                    roll_count = roll_count + 1
            else:
                c1_total = c1_total + turn_total
                turn_total = 0
                roll_count = 0
                return c1_total
        else:
            if roll_count <= 2:
                r = dice_roll()
                if r == 1:
                    turn_total = 0
                    roll_count = 0
                    return c1_total
                else:
                    turn_total = turn_total + r
                    roll_count = roll_count + 1
            else:
                c1_total = c1_total + turn_total
                turn_total = 0
                roll_count = 0
                return c1_total
    c1_total = c1_total + turn_total
    return c1_total

def c2_strat(c2_total):
    turn_total = 0
    r = dice_roll()
    roll_count = 1
    if r == 1:
        turn_total = 0
        return c2_total
    else:
        turn_total = turn_total + r
    while c2_total + turn_total < 100:
        while roll_count < 4:
            r = dice_roll()
            if r == 1:
                turn_total = 0
                roll_count = 0
                return c2_total
            else:
                turn_total = turn_total + r
                roll_count = roll_count + 1
        while c2_total + turn_total < 100:
            choice = random.choice(['Roll', 'Stop'])
            if choice == 'Roll':
                r = dice_roll()
                if r == 1:
                    turn_total = 0
                    return c2_total
                else:
                    turn_total = turn_total + r
            else:
                c2_total = c2_total + turn_total
                turn_total = 0
                return c2_total
    c2_total = c2_total + turn_total
    return c2_total
        
def c3_strat(c3_total):
    turn_total = 0
    r = dice_roll()
    roll_count = 1
    if r == 1:
        turn_total = 0
        return c3_total
    else:
        turn_total = turn_total + r
    while c3_total + turn_total < 100:
        while c3_total < 85:
            while turn_total < 15:
                r = dice_roll()
                if r == 1:
                    turn_total = 0
                    return c3_total
                else:
                    turn_total = turn_total + r
            while turn_total >= 15:
                choice = random.choice(['Roll', 'Stop'])
                if choice == 'Roll':
                    r = dice_roll()
                    if r == 1:
                        turn_total = 0
                        return c3_total
                    else:
                        turn_total = turn_total + r
                else:
                    c3_total = c3_total + turn_total
                    turn_total = 0
                    return c3_total
        if roll_count < 3:
            r = dice_roll()
            if r == 1:
                turn_total = 0
                return c3_total
            else:
                turn_total = turn_total + r
                roll_count += 1
        else:
            c3_total = c3_total + turn_total
            return c3_total
    c3_total = c3_total + turn_total
    return c3_total

def c4_strat(c4_total, opp_total):
    turn_total = 0
    r = dice_roll()
    if r == 1:
        turn_total = 0
        return c4_total
    else:
        turn_total = turn_total + r
    while c4_total + turn_total < 100:
        if c4_total + turn_total < opp_total:
            r = dice_roll()
            if r == 1:
                turn_total = 0
                return c4_total
            else:
                turn_total = turn_total + r
        else:
            r = dice_roll()
            if r == 1:
                turn_total = 0
                return c4_total
            else:
                turn_total = turn_total + r
                c4_total = c4_total + turn_total
                return c4_total
    c4_total = c4_total + turn_total
    return c4_total
        
        
def h1_play(h1_total, c_total):
    turn_total = 0
    print(f'\nYour total is {h1_total}.\nYour opponent total is {c_total}.\n')
    r = dice_roll()
    print(f'You rolled a {r}')
    if r == 1:
        turn_total = 0
        print('Opponent turn now')
        return h1_total
    else:
        turn_total = turn_total + r
        while h1_total < 100:
            choice = input(f'Your turn total is {turn_total}.\n \
                           Would you like to roll or stop?\n').lower()
            if choice == 'roll':
                r = dice_roll()
                print(f'\nYou rolled a {r}.')
                if r == 1:
                    turn_total = 0
                    print('Opponent turn now')
                    return h1_total
                else:
                    turn_total = turn_total + r
            elif choice == 'stop':
                h1_total = h1_total + turn_total
                turn_total = 0
                return h1_total
            elif choice == 'break':
                break
            else:
                print('\nError.\nPlease input either \"roll\" or \"stop\".')

def h2_play(h2_total, c_total):
    turn_total = 0
    print(f'\nYour total is {h2_total}.\nYour opponent total is {c_total}.\n')
    r = dice_roll()
    print(f'You rolled a {r}')
    if r == 1:
        turn_total = 0
        print('Opponent turn now')
        return h2_total
    else:
        turn_total = turn_total + r
        while h2_total < 100:
            choice = input(f'Your turn total is {turn_total}.\n \
                           Would you like to roll or stop?\n').lower()
            if choice == 'roll':
                r = dice_roll()
                print(f'\nYou rolled a {r}.')
                if r == 1:
                    turn_total = 0
                    print('Opponent turn now')
                    return h2_total
                else:
                    turn_total = turn_total + r
            elif choice == 'stop':
                h2_total = h2_total + turn_total
                turn_total = 0
                return h2_total
            elif choice == 'break':
                break
            else:
                print('\nError.\nPlease input either \"roll\" or \"stop\".')

def pick_computer():
    player = random.randint(1,4)
    return player

def check_win(p1, p2, p1_score, p2_score):
    if p1_score >= 100 and p2_score <= 100:
        winner = print(f'\nThe winner was {p1}. \nThe final score was {p1_score} to {p2_score}.')
    elif p2_score >= 100 and p1_score <= 100:
        winner = print(f'\nThe winner was {p2}. \nThe final score was {p2_score} to {p1_score}.')
    elif p1_score >= 100 and p2_score >= 100:
        winner = print(f'\nThere was a tie. \nThe final score was {p1_score} to {p2_score}.')
    else:
        return
    return winner
        
    
pig_game()


