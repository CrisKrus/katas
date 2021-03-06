import unittest


def break_out_rooms(participants, room_sizes, rounds):
    rooms = []
    room_size = room_sizes[0]

    room_amount = int(len(participants) / room_size)

    group_start = 0
    group_end = room_size
    for i in range(room_amount):
        rooms.append(participants[group_start:group_end])
        group_start = group_end
        group_end += room_size

    return rooms


class Kata(unittest.TestCase):

    def test_should_create_rooms_on_a_single_round(self):
        participants = ['Jose Angel', 'Sara', 'Airan', 'Sosa', 'Ruben', 'Manu M', 'Cristian', 'Nazaret', 'Juan Antonio',
                        'Jorge', 'F. Mesa', 'Manuel P.', 'Noe', 'Kevin', 'Maria', 'Michael', 'Ulises', 'Ricardo',
                        'Ivan', 'Yazmina', 'Mireia']

        expected_rooms = [
            ['Jose Angel', 'Sara', 'Airan'],
            ['Sosa', 'Ruben', 'Manu M'],
            ['Cristian', 'Nazaret', 'Juan Antonio'],
            ['Jorge', 'F. Mesa', 'Manuel P.'],
            ['Noe', 'Kevin', 'Maria'],
            ['Michael', 'Ulises', 'Ricardo'],
            ['Ivan', 'Yazmina', 'Mireia'],
        ]
        rooms = break_out_rooms(participants, [3], 1)
        self.assertEqual(expected_rooms, rooms)

    def test_should_create_rooms_on_multiple_rounds(self):
        participants = ['Jose Angel', 'Sara', 'Airan', 'Sosa', 'Ruben', 'Manu M', 'Cristian', 'Nazaret', 'Juan Antonio',
                        'Jorge', 'F. Mesa', 'Manuel P.', 'Noe', 'Kevin', 'Maria', 'Michael', 'Ulises', 'Ricardo',
                        'Ivan', 'Yazmina', 'Mireia']

        expected_rooms = [
            [
                ['Jose Angel', 'Sara', 'Airan'],
                ['Sosa', 'Ruben', 'Manu M'],
                ['Cristian', 'Nazaret', 'Juan Antonio'],
                ['Jorge', 'F. Mesa', 'Manuel P.'],
                ['Noe', 'Kevin', 'Maria'],
                ['Michael', 'Ulises', 'Ricardo'],
                ['Ivan', 'Yazmina', 'Mireia'],
            ],
            [
                ['Sosa', 'Maria'],
                ['Noe', 'Ruben', 'Yodra'],
                ['Mireia', 'Ricardo'],
                ['Juan Antonio', 'Sara'],
                ['F. Mesa', 'Nazaret'],
                ['Crisitian', 'Manuel P.'],
                ['Airan', 'Ulises'],
                ['Jorge', 'Manu M.'],
                ['Ivan', 'Kevin'],
                ['Jose Angel', 'Michael'],
            ]
        ]
        rooms = break_out_rooms(participants, [3, 2], 2)
        self.assertEqual(expected_rooms, rooms)


# Round 3 - Rooms with 2+ people:
#
# Maria - Sara
# Nazaret - Noe
# Mireia - Yodra
# Ricardo - Cristian
# Airan - Manu M.
# Juan Antonio - Jose Angel
# Kevin - Ruben
# Manuel P. - Ivan
# Sosa - F. Mesa
# Ulises - Michael


if __name__ == '__main__':
    unittest.main()
