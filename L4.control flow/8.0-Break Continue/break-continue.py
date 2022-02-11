'''Break, Continue
Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

break terminates a loop
continue skips one iteration of a loop'''
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("my solution")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    if weight >= 100: # don't forget equal to
        print("  the cargo is full")
        break

    elif cargo_weight + weight > 100:
        print("  skipping: {}".format(cargo_name))
        continue

    else:
        print("  adding: {}".format(cargo_name))
        weight += cargo_weight
        items.append(cargo_name)

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

'''
output:
my solution
    adding: bananas
    adding: mattresses
    adding: dog kennels
    skipping: machine
    adding: cheeses

Final Weight: 86
Final Items: ['bananas', 'mattresses', 'dog kennels', 'cheeses']
'''
''' Quiz: Break, Continue
Quiz: Break the String
Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

my solution:

make sure the length of news_ticker never more than 140'''

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
            "Legislature Announces New Laws",
            "Peasant Discovers Violence Inherent in System",
            "Cat Rescues Fireman Stuck in Tree",
            "Brave Knight Runs Away",
            "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for headline in headlines:
    if (len(news_ticker) == 140):
        break

    elif (len(news_ticker) + len(headline) >= 140):
        news_ticker += headline[:140-len(news_ticker)]
        break

    else:
        news_ticker += headline + " "

print(news_ticker)
print(len(news_ticker))

'''
output:
Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
140
'''
#answer:

#concatenate first, then truncate it

headlines = ["Local Bear Eaten by Man",
            "Legislature Announces New Laws",
            "Peasant Discovers Violence Inherent in System",
            "Cat Rescues Fireman Stuck in Tree",
            "Brave Knight Runs Away",
            "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
print(len(news_ticker))

'''
output:
Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
140
'''