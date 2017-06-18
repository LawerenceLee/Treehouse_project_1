import csv

if __name__ == '__main__':
    exp_players = []     # Experienced Players
    inexp_players = []   # Inexperienced Players
    teams = {
        'dragons': [],
        'sharks': [],
        'raptors': []
    }

    def read_csv_and_append():
        '''
        Reads each line (player data) of a csv file, checks for experience
        (either YES or NO) and appends the player to either the experienced
        players list or inexperienced players list.
        '''

        with open('soccer_players.csv') as csvfile:
            roster_reader = csv.reader(csvfile, delimiter=',')
            lines = list(roster_reader)
            for line in lines:
                if 'YES' in line:
                    exp_players.append(line)
                elif 'NO'in line:
                    inexp_players.append(line)

    def team_logic(list, player, team):
        # Grab a players index from a list
        player_index = list.index(player)
        # Uses that index to pop player from list and append them to a team.
        # Popping allows sampling without replacement.
        teams[team].append(list.pop(player_index))

    def dividing_up_players(list):
        '''
        Breaks up elements (players) embedded within a list into teams of
        equal size.
        '''

        dragons_counter = 0
        sharks_counter = 0
        raptors_counter = 0

        # While loop ensures that all players from a list are used.
        while len(list) != 0:
            for player in list:
                # If a team does not have three players add player,
                # if it does try next team.
                if dragons_counter != 3:
                    team_logic(list, player, 'dragons')
                    dragons_counter += 1
                elif sharks_counter != 3:
                    team_logic(list, player, 'sharks')
                    sharks_counter += 1
                elif raptors_counter != 3:
                    team_logic(list, player, 'raptors')
                    raptors_counter += 1

    def roster_writer():
        '''
        Generates the roster for each soccer team, and includes information
        such as whether a player is new to the sport and the names of thier
        parents.
        '''
        
        with open('teams.txt', 'w') as text_file:
            for team in teams:
                text_file.write(team.title() + '\n')
                for player in teams[team]:
                    player.remove(player[1])  # Remove Player's height
                    # Remove all quotes and brackets from string.
                    text_file.write(str(player).replace("'", "").replace('[', '').replace(']', '') + '\n')
                text_file.write('\n')

    def welcome_letter():
        '''
        Generates a welcome letter to a parent that includes which team
        thier child is on, when and where they will practice.
        '''

        for team in teams:
            for player in teams[team]:
                file_name = '{}.txt'.format(player[0].replace(' ', '_'))
                message = '''Dear {}, \n\n{} will be on the {} this year.
Your first practice will be on 9/13 @ 6pm.
\n*All practices will be conducted at:
\nRockville Field \n2542 Trenton Place \nOakdon, NY. 90253
                '''.format(player[2], player[0], team.title())
                letter_file = open(file_name, 'w')
                letter_file.write(message)

    read_csv_and_append()
    dividing_up_players(exp_players)
    dividing_up_players(inexp_players)
    roster_writer()
    welcome_letter()
