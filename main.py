link = input()
# Notice how the videos' IDs started at different places. I coded it off of that.

x = link.index("=") + 1 if "=" in link else 17
print(link[x:])
