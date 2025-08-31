"""
Created on 11/11/2024
@author: Matthew Lassiter

This program demonstrates lists of Integer and String objects.
It should print out the volcano and VEI The volcanic explosivity index (VEI) 
is a relative measure of the explosiveness of volcanic eruptions.
It should print out the volcano with the highest VEI and its VEI
You must use the find_highest_VEI() method within your solution.
You must also use the display_VEI() method within your solution.
This is what should display when the program runs as it should
Ulawun had a VEI of 1.
Chikurachki had a VEI of 2.
Lascar had a VEI of 3.
Kerinci had a VEI of 2.
Nishinoshima had a VEI of 2.
"""

def main():
    volcanoes = ["Ulawun", "Chikurachki", "Lascar", "Kerinci", "Nishinoshima"]
    vei = [1, 2, 3, 2, 2]

    # Function to display VEI of each volcano
    def display_VEI(volcanoes, vei):
        for i in range(len(volcanoes)):
            print(f'{volcanoes[i]} had a VEI of {vei[i]}')

    # Function to find the index of the volcano with the highest VEI
    def find_highest_vei(volcanoes, vei):   
        highest_vei_index = 0
        # loops through starting at 1 to the length of the vei list
        for i in range(1, len(vei)):
            if vei[i] > vei[highest_vei_index]:
                # rename the iterable within if block
                highest_vei_index = i
        # display the value 
        return highest_vei_index
    
    # Function to display the volcano with the highest VEI
    def display_vei(volcanoes, vei):
        # store the result of the highest vei in highest vei index / this lets us work with the result
        highest_vei_index = find_highest_vei(volcanoes, vei)
        # output the what we stored in the var then pull that index value from the vei list
        print(f'{volcanoes[highest_vei_index]} has the highest VEI of {vei[highest_vei_index]}.')

    # when calling the functions both volcanoes and vei are taken as arguments
    # Display all volcanoes and their VEI values
    display_VEI(volcanoes, vei)
    
    # Display the volcano with the highest VEI
    display_vei(volcanoes, vei)

# Call the main function
if __name__ == '__main__':  
    main()
