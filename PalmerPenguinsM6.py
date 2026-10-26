# PalmerPenguinsM6.py
# J. Andrew Yurick
# October 26, 2026
# Use functions to organize Palmer Penguin analysis

# Two screenshots provided because the complete program output
# could not fit in a single screenshot.

# import modules
import math

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"
NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

# functions for penguin analysis
def calculate_percentage(count, total):
    percentage = count / total * 100
    return percentage

def classify_species(percent):
    if percent < 25:
        size_category = "small"
    elif percent >= 25 and percent < 40: 
        size_category = "medium"
    else:
        size_category = "large" 
    return size_category

def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        position_description = "largest"
    elif selected_species == smallest_species:
        position_description = "smallest"
    else:
        position_description = "middle-sized"
    return position_description

def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} " f"({percentages[index]:.2f}%)")
    print()

def main():
    # lists containing related penguin data
    species_names = [SP_CHINSTRAP, SP_GENTOO, SP_ADELIE]
    species_counts = [NUM_CHINSTRAP, NUM_GENTOO, NUM_ADELIE]

    # calculate dataset statistics
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)
    chinstrap_percent = calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = calculate_percentage(species_counts[2], total_penguins)

    # list containing the percentage of each species
    species_percentages = [chinstrap_percent, gentoo_percent, adelie_percent]

    # determine largest and smallest species groups
    largest_count = max(species_counts)
    smallest_count = min(species_counts)
    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)
    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output the species names with introductory text
    print("Introducing the Palmer Penguins:")
    print()
    print(f"\t{species_names[0]}!")
    print(f"\t{species_names[1]}!")
    print("and last but not least...")
    print()
    print(f"\t{species_names[2]}!")
    print()

    # output dataset statistics
    print(f"There are a total of {total_species} penguin species in this dataset.")
    print(f"There are a total of {total_penguins} penguins in the dataset.")
    print(f"The average number of penguins per species is " f"{average_penguins:.1f}.")
    print(f"The average rounded up is {average_penguins_rounded_up} penguins.")

    # display species statistics using a loop
    display_species_statistics(species_names, \
        species_counts, species_percentages)

    # display the species with the most and fewest observations
    print(f"The species with the most observations is {largest_species} with {largest_count} penguins.")
    print(f"The species with the fewest observations is {smallest_species} with {smallest_count} penguins.")

    # Counter for Valid Species
    valid_selections = 0

    # Explore a species based on user input
    print()
    print("Explore a species")
    species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")
    print()

    # repeatedly prompt the user to explore species
    while species_choice != "Done":
        # validate species selection
        if species_choice not in species_names:
            print(f"{species_choice} is not one of the species in this dataset.")

        # Determine selected species
        else:
            # update the number of valid selections
            valid_selections += 1
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # classify selected species
            size_category = classify_species(selected_percent)

            # Determine species position
            position_description = get_position_description(
                selected_species, 
                largest_species, 
                smallest_species)

            average_position = "above" if selected_count > average_penguins else "below"

            # Output selected species statistics
            print(f"{selected_species} has {selected_count} observations, representing {selected_percent:.2f}% of the dataset.")
            print(f"{selected_species} is classified as a {size_category} species group.")
            print(f"{selected_species} is the {position_description} species group.")
            print(f"Its observation count is {average_position} the dataset average of {average_penguins:.1f}.")

        print()
        print("Explore a species")
        species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")
        print()

    # display the exploration summary
    print(f"You explored {valid_selections} valid species.")
    print()
    print("Exploration complete.")

main()