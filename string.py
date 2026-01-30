str1 = "Ratikant"
str2 = "Patil"

final_str = str1 + " " + str2

print(final_str)  # Output: Ratikant Patil

print(len(str1))  # Output: 9
print(len(str2))  # Output: 5
print(len(final_str))  # Output: 15
print(final_str.upper())  # Output: RATIKANT PATIL
print(final_str.lower())  # Output: ratikant patil  
print(final_str.replace("Ratikant", "Rahul"))  # Output: Rahul Patil
print(final_str.split(" "))  # Output: ['Ratikant', 'Patil']
print(final_str.index("Patil"))  # Output: 10
print(final_str.index("Ratikant"))  # Output: 0
print(final_str.startswith("Ratikant"))  # Output: True
print(final_str.endswith("Patil"))  # Output: True
print(final_str.count("a"))  # Output: 3
print(final_str.find("Patil"))  # Output: 10
print(final_str.find("Ratikant"))  # Output: 0
print(final_str.isalnum())  # Output: False (because of the space)
print(final_str.isalpha())  # Output: False (because of the space)
print(final_str.isspace())  # Output: False
print(final_str.capitalize())  # Output: Ratikant patil
print(final_str.title())  # Output: Ratikant Patil
print(final_str.center(30, '-'))  # Output: -----------
print(final_str.count("t"))  # Output: 2
print(final_str.swapcase())  # Output: rATIKANT pATIL
print(final_str.strip())  # Output: Ratikant Patil (no leading/trailing spaces to remove)
print(final_str.replace(" ", "_"))  # Output: Ratikant_Patil
print(final_str[::-1])  # Output: litaP tnakitaR
print(final_str.index("a"))  # Output: 3
print(final_str.rindex("a"))  # Output: 7
print(final_str.partition(" "))  # Output: ('Ratikant', ' ', 'Patil')
print(final_str.rpartition(" "))  # Output: ('Ratikant',
# ' ', 'Patil')
print(final_str.encode())  # Output: b'Ratikant Patil'
print(final_str.expandtabs())  # Output: Ratikant Patil (no tabs to expand)
print(final_str.zfill(20))  # Output: 0000000Ratikant Patil
print(final_str.islower())  # Output: False
print(final_str.isupper())  # Output: False
print(final_str.endswith("t"))  # Output: False

print(final_str.startswith("P"))  # Output: False
print(final_str.endswith("l"))  # Output: False
print(final_str.replace("Patil", "Sharma"))  # Output: Ratikant Sharma
print(final_str.split("a"))  # Output: ['R', 'tik', 'nt P', 'til']
print(final_str.lower().startswith("ratikant"))  # Output: True