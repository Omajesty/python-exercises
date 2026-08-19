# 3-4. Guest List
guest_list = ["Robert", "Johnson", "Smith"]

for guests in (guest_list):
    print(f"Hello {guests}! I wish to invite you to a dinner at my house by 6pm")

# 3-5. Changing Guest List
print (f"Announcement: {guest_list[0]} will not make it to the dinner")

guest_list[0]="Bridget"

for guests in (guest_list):
    print(f"Hello {guests}! I wish to invite you to a dinner at my house by 6pm")

# 3-6. More Guests
print(f"Announcement: We just got a bigger table for the dinner, there's space for more people")

guest_list.insert(0,"Banita")
guest_list.insert(2,"Gbenga")
guest_list.append("Bimbo")

for guests in (guest_list):
    print(f"Hello {guests}! I wish to invite you to a dinner at my house by 6pm")

# 3-7. Shrinking Guest List
print(f"Announcement: Unfortunately, our big table won't arrive on time, only two people can come.")
for guests in (guest_list):
    while len(guest_list) > 2:
        delete_guest = guest_list.pop()
        print(f"{delete_guest}, sorry your reservation is cancelled")

for guests in (guest_list):
    print(f"Hello {guests}! You are still invited to the by 6pm")

del guest_list[:]

print(guest_list)


