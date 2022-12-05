#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Eslodysko, 2022-Dec-03, Added code for funcionality
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TO DONE Add Code to the CD class
    
# ------- Constructor-------#
    def __init__(self, cd_id, cd_title, cd_artist):
      
# ------- Attributes--------#
        self.__cdID = cd_id
        self.__cdtitle = cd_title
        self.__cdartist = cd_artist
    
# ------- Properties--------#
    @property
    def cdID(self):
        return self.__cdID
    
    @property
    def cdtitle(self):
        return self.__cdtitle
    
    @property
    def cdartist(self):
        return self.__cdartist
    
    @cdID.setter
    def cdID(self, value):
        if str(value).isalnum():
            raise Exception('The value must a number')
        else:
            self.__cdID = value

    @cdtitle.setter
    def cdtitle(self, value):
        if str(value).isnumeric():
            raise Exception('The value must be string type')
        else:
            self.__Title = value
            
    @cdartist.setter
    def cdartist(self, value):
        if str(value).isnumeric():
            raise Exception('The value must be string type')
        else:
            self.__Artist= value
    pass

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    @staticmethod
    def load_inventory(file_name,lst_Inventory):
        lstOfCDObjects.clear()
        objFile= open(file_name, 'r')
        for cd in objFile:
            data = cd.strip().split(',')
            lstOfCDObjects.append(data)
        objFile.close()
        
        
    # TO DONE Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory): 
        """Function for saving information to CDInventory.txt'"""
        objFile = open(file_name, 'w')
        for cd in lst_Inventory:
            objFile.write(str(cd.cdID) + ',' + cd.cdtitle + ',' + cd.cdartist)
        objFile.close()
        pass
    
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TO DONE add docstring
    # TO DONE add code to show menu to user

    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  
        return choice
    
    
    # TO DONE add code to captures user's choice
    @staticmethod
    def user_input(): # function for user input of CD
        """Function for getting user input for CDs (Cd Id, Album Name, Artist)
         
         args:
             None
         
         Returns: CD ID (int), Album Name (Title) (str) and Artist (str) '"""
         
         
        intID= int(input('Enter CD ID:').strip())
        strTitle= str(input('Enter Album Title: ')).strip()
        strArtist = str(input('Enter the Artist Name: ')).strip()
        return(intID,strTitle,strArtist)


    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of cds): that is defined by properties in class CD that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print('{}\t{} (by:{})'.format(cd.cdID,cd.cdtitle,cd.cdartist))
        print('======================================')

    # TODO add code to get CD data from user

pass

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
    
# 1. When program starts, read in the currently saved Inventory    
#FileIO.read_file(strFileName, lst_Inventory)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
        
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
        
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')

        continue
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        cdID, cdTitle, cdArtist = IO.user_input()
        cdInfo = CD(cdID, cdTitle, cdArtist) #creating an instance of the object, assigning to variable 
        lstOfCDObjects.append(cdInfo)
        # Call constructor, store returned cd object in variable, add to list of cd objects
        IO.show_inventory(lstOfCDObjects)
        # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        
        # 3.5 process delete a CD
    elif strChoice == 'd': 
        continue
        # 3.6 process save inventory to file
    elif strChoice == 's':
        
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODO move processing code into function
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
        # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
