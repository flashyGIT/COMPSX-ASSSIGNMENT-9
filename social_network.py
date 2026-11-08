
class Person:
    def __init__(self, name: str):
        self.name = name
        self.friends = []

    def add_friend(self, friend: "Person") -> None:
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name: str) -> None:
        if name in self.people:
            print(f"Error: {name} already exists in the network.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name: str, person2_name: str) -> None:
        if person1_name not in self.people:
            print(f"Error: {person1_name} does not exist.")
            return

        if person2_name not in self.people:
            print(f"Error: {person2_name} does not exist.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Prevent self-friendship
        if person1 == person2:
            print("Error: A person cannot be friends with themselves.")
            return

        # Create bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self) -> None:
        for name, person in self.people.items():
            friends = [friend.name for friend in person.friends]
            print(f"{name}: {', '.join(friends)}")


# Example usage
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")

# Print network
network.print_network()

"""
DESIGN MEMO: SOCIAL NETWORK GRAPH

This project implements a simple social networking system using
an undirected graph data structure in Python. The purpose of the
program is to represent people as nodes and friendships as
bidirectional edges.

The system uses two classes: Person and SocialNetwork. The
Person class represents an individual user and stores their
name and a list of friends. The add_friend() method allows a
person to connect with another person while preventing
duplicate friendships.

The SocialNetwork class manages all users through a dictionary
called people. Each dictionary key is a person's name, and
each value is the corresponding Person object. A dictionary
was chosen because it provides efficient average-case lookup
when searching for users by name.

The add_person() method creates new users and checks whether
a name already exists. This prevents duplicate users from
being added to the network. The add_friendship() method
establishes connections between two existing users. Since
friendships are mutual, both people are added to each other's
friend lists. The method also handles errors when users do
not exist and prevents a person from becoming friends with
themselves.

The print_network() method displays the entire network by
listing each person and their friends. This makes it easier
to understand the relationships represented by the graph.

One advantage of this design is that it is simple, organized,
and easy to expand. Future improvements could include removing
friendships, deleting users, searching for mutual friends,
and finding connection paths between people.

Overall, this project demonstrates how graph data structures,
Python classes, dictionaries, and lists can work together
to model real-world social relationships.
"""
