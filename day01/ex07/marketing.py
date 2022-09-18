#!/usr/bin/python3

import sys


def get_clients() -> set:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return set(clients)


def get_participants() ->set:
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return set(participants)


def get_recipients() -> set:
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(recipients)


def call_center_request(clients: set, recipients: set) -> list:
    return list(clients - recipients)


def potential_clients_request(clients: set, participants: set) -> list:
    return list(participants - clients)


def loyalty_program_request(clients: set, participants: set) -> list:
    return list(clients - participants)


def request_handler(name: str) -> None:
    clients = get_clients()
    participants = get_participants()
    recipients = get_recipients()

    if name == 'call_center':
        print(call_center_request(clients, recipients))
    elif name == 'potential_clients':
        print(potential_clients_request(clients, participants))
    elif name == 'loyalty_program':
        print(loyalty_program_request(clients, participants))
    else:
        raise ValueError('Invalid argument: argument must be one of: ' +
                         '["call_center", "potential_clients", "loyalty_program"]')


def main():
    if len(sys.argv) == 2:
        request_handler(sys.argv[1])


if __name__ == '__main__':
    main()
