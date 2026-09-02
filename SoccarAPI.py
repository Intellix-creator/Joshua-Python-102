PlayerList = {
    1: {
        'name': 'Iker Casillas',
        'position': 'Goalkeeper',
        'citizenship': 'Spain',
        'appearances': '725',
        'goals': '0'
    },

    2: {
        'name': 'Dani Carvajal',
        'position': 'Right-Back Defender',
        'citizenship': 'Spain',
        'appearances': '400+',
        'goals': '10+'
    },

    3: {
        'name': 'Roberto Carlos',
        'position': 'Left-Back Defender',
        'citizenship': 'Brazil',
        'appearances': '527',
        'goals': '69'
    },

    4: {
        'name': 'Sergio Ramos',
        'position': 'Centre-Back Defender',
        'citizenship': 'Spain',
        'appearances': '671',
        'goals': '101'
    },

    5: {
        'name': 'Zinedine Zidane',
        'position': 'Attacking Midfielder',
        'citizenship': 'France',
        'appearances': '230',
        'goals': '49'
    },

    6: {
        'name': 'Fernando Hierro',
        'position': 'Centre-Back / Defensive Midfielder',
        'citizenship': 'Spain',
        'appearances': '601',
        'goals': '127'
    },

    7: {
        'name': 'Cristiano Ronaldo',
        'position': 'Left-Winger / Forward',
        'citizenship': 'Portugal',
        'appearances': '438',
        'goals': '450'
    },

    8: {
        'name': 'Toni Kroos',
        'position': 'Central Midfielder',
        'citizenship': 'Germany',
        'appearances': '465',
        'goals': '28'
    },

    9: {
        'name': 'Karim Benzema',
        'position': 'Striker',
        'citizenship': 'France',
        'appearances': '648',
        'goals': '354'
    },

    10: {
        'name': 'Luka Modric',
        'position': 'Central Midfielder',
        'citizenship': 'Croatia',
        'appearances': '590+',
        'goals': '40+'
    },

    11: {
        'name': 'Gareth Bale',
        'position': 'Right-Winger / Forward',
        'citizenship': 'Wales',
        'appearances': '258',
        'goals': '106'
    },

    12: {
        'name': 'Marcelo Vieira',
        'position': 'Left-Back Defender',
        'citizenship': 'Brazil',
        'appearances': '546',
        'goals': '38'
    },

    13: {
        'name': 'Keylor Navas',
        'position': 'Goalkeeper',
        'citizenship': 'Costa Rica',
        'appearances': '162',
        'goals': '0'
    },

    14: {
        'name': 'Casemiro',
        'position': 'Defensive Midfielder',
        'citizenship': 'Brazil',
        'appearances': '336',
        'goals': '31'
    },

    15: {
        'name': 'Raul Gonzalez',
        'position': 'Striker / Forward',
        'citizenship': 'Spain',
        'appearances': '741',
        'goals': '323'
    },

    16: {
        'name': 'Claude Makelele',
        'position': 'Defensive Midfielder',
        'citizenship': 'France',
        'appearances': '145',
        'goals': '2'
    },

    17: {
        'name': 'Luis Figo',
        'position': 'Right-Winger',
        'citizenship': 'Portugal',
        'appearances': '245',
        'goals': '57'
    },

    18: {
        'name': 'Fernando Morientes',
        'position': 'Striker',
        'citizenship': 'Spain',
        'appearances': '272',
        'goals': '100'
    },

    19: {
        'name': 'Vinicius Junior',
        'position': 'Left-Winger',
        'citizenship': 'Brazil',
        'appearances': '300+',
        'goals': '100+'
    },

    20: {
        'name': 'Gonzalo Higuain',
        'position': 'Striker',
        'citizenship': 'Argentina',
        'appearances': '264',
        'goals': '121'
    },

    21: {
        'name': 'David Beckham',
        'position': 'Right Midfielder',
        'citizenship': 'England',
        'appearances': '159',
        'goals': '20'
    },

    22: {
        'name': 'Angel Di Maria',
        'position': 'Winger / Attacking Midfielder',
        'citizenship': 'Argentina',
        'appearances': '190',
        'goals': '36'
    },

    23: {
        'name': 'Mesut Ozil',
        'position': 'Attacking Midfielder',
        'citizenship': 'Germany',
        'appearances': '159',
        'goals': '27'
    },

    24: {
        'name': 'Pepe',
        'position': 'Centre-Back Defender',
        'citizenship': 'Portugal',
        'appearances': '334',
        'goals': '15'
    }
}


def getPlayerData(jerseyNumber):

    return PlayerList.get(
        jerseyNumber,
        {
            'name': '???',
            'position': '???',
            'citizenship': '???',
            'appearances': '???',
            'goals': '???'
        }
    )


