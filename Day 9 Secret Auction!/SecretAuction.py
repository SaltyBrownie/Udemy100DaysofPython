# Secret Auction
from art import logo
import os
print(logo)


def find_highest_bidder(bidding_record):
    # {"ang":123,"Jam":234}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        # for loop in dictionary loops through the key
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: #comparing dic vs value is not possible [string[
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")


bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price
    choice = input("Is there another bidder?:")
    if choice == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif choice == "yes":
        os.system('cls')

print("bids")
