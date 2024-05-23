import random

def print_dragon():
    print('                \||/')
    print('                |  @___oo')
    print('      /\  /\   / (__,,,,|')
    print('     ) /^\) ^\/ _)')
    print('     )   /^\/   _)')
    print('     )   _ /  / _)')
    print(' /\  )/\/ ||  | )_)')
    print('<  >      |(,,) )__)')
    print(' ||      /    \)___)\ ')
    print(' | \____(      )___) )___')
    print('  \______(_______;;; __;;;')

print_dragon()


game_start = 'yes'

while game_start == 'yes':
    magician = input('Name of an evil person? ')
    princess = input('Name of a girl you like? ')
    horse = input('Name of a friend? ')
    print()
    print('You are brave knight on a mission to save princess ' + princess)
    print(f'The princess has been kidnapped by Lord {magician}, an evil and powerful magician!')

    adjective = random.choice(['Dashing', 'Sleepy', 'Gracious', 'Fearless'])
    print(f'You call out the name of your most trusted companion, {adjective} {horse}!')
    print('The horse begin running towards you, when it hears your voice.')
    print('Then you jump on its back, ready to continue your journey!')
    answer_1 = input('East or west? ')
    while answer_1 != 'east' and answer_1 != 'west':
        answer_1 = input('East or west? ')
        print_dragon()

    if answer_1 == 'east':
        print('You travel east and meet a dragon!')
        print_dragon()
    else:
        print('You fall off a cliff and die.')

    game_start = input('Do you want to start over? ')
