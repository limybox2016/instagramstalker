import os
from datetime import datetime

# get file names in the current directory that end with "subscribers.txt" and "subscriptions.txt"
subscribers_files = [f for f in os.listdir() if f.endswith("subscribers.txt")]
subscriptions_files = [f for f in os.listdir() if f.endswith("subscriptions.txt")]

# we create sets to store the data from the input files
subscribers_set = set()
subscriptions_set = set()

# add data from subscribers.txt and subscriptions.txt to the sets
for file in subscribers_files:
    with open(file, "r") as subscribers_file:
        subscribers_set.update(subscribers_file.read().split())
for file in subscriptions_files:
    with open(file, "r") as subscriptions_file:
        subscriptions_set.update(subscriptions_file.read().split())

# create sets to store data from subscribers1.txt and subscriptions1.txt
subscribers_1_set = set()
subscriptions_1_set = set()

# add data from subscribers1.txt and subscriptions1.txt to sets
for file in subscribers_files:
    subscribers_1_file = file.replace("subscribers.txt", "subscribers_1.txt")
    if os.path.exists(subscribers_1_file):
        with open(subscribers_1_file, "r") as subscribers_1_file:
            subscribers_1_set.update(subscribers_1_file.read().split())
for file in subscriptions_files:
    subscriptions_1_file = file.replace("subscriptions.txt", "subscriptions_1.txt")
    if os.path.exists(subscriptions_1_file):
        with open(subscriptions_1_file, "r") as subscriptions_1_file:
            subscriptions_1_set.update(subscriptions_1_file.read().split())

# get new entries in subscribers1_set and subscriptions1_set that are not in subscribers_set and subscriptions_set
new_subscribers = subscribers_1_set - subscribers_set
new_subscriptions = subscriptions_1_set - subscriptions_set

# create directory named "results" with current timestamp
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
directory = os.path.join(os.getcwd(), f"results_{timestamp}")
os.makedirs(directory)
    
# write new entries in the {username}_results.txt file inside the "results" directory
for file in subscribers_files:
    output_filename = file.replace("subscribers.txt", "_results.txt")
    output_file = os.path.join(directory, output_filename)
    with open(output_file, "w") as f:
        f.write("New subscribers:\n")
        f.write("\n".join(new_subscribers))
        f.write("\n\nNew subscriptions:\n")
        f.write("\n".join(new_subscriptions))
