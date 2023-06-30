from replit import clear
from art import logo
print(logo)

bids =  {}
biding_finish = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for i in bidding_record:
    amount = bidding_record[i]
    if amount > highest_bid:
      highest_bid = amount
      winner = i
  clear()
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not biding_finish:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if should_continue == "no":
    biding_finish = True
    find_highest_bidder(bids)
  elif should_continue =="yes":
    clear()
  
