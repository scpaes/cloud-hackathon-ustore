#!../env_desafio/bin/python
import sys

COMMAND_SOPTIONS = [
    ('Resumo simples de gastos', 'resumo-gastos', ''),
    ('Detalhamento de gastos', 'detalhe-gastos', '<tipo-gasto>'),
    ('Sugestão para redução de gastas', 'sugestoes', '')
]


def help() -> str:
    """ Helper function """
    print('{:40} | {:^20} | {:^9}'.format('', 'Commands', 'Options'))
    fmt = '{:40} | {:^20} | {:^9}'

    for description, command, option in COMMAND_SOPTIONS:
        print(fmt.format(description, command, option))


if __name__ == '__main__':
    arg = None

    try:
        arg = sys.argv[1]
    except IndexError:
        print('Informe um argumento.')
        help()

    if arg is not None:
        arg = arg.lower()

        if arg == 'help' or arg == 'h':
            help()
