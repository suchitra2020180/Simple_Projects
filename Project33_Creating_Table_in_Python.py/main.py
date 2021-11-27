# importing package
# import prettytable
# from package importing class
from prettytable import PrettyTable
# Creating a PrettyTable object and saving it to a variable called table
table = PrettyTable()
print(table)
# Adding column names with their values
# PrettyTable.add_column("col_name",[])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# PrettyTable.add_column('Type',['Electric','Water','Fire'])
print(table)
# Changing object Attributes
# Alining
print("Current align",table.align)
table.align = "l"
print("After left alignment",table.align)
print(table)

# Adding a row

