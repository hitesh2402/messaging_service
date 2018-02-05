#!/usr/bin/env/python

import datetime



def get_current_time():
    return datetime.datetime.now()

def generate_next_msg_id():
    if 'current' not in generate_next_msg_id.__dict__:
        generate_next_msg_id.current = 1

    generate_next_msg_id.current += 1
    return generate_next_msg_id.current


if __name__ == '__main__':
    main()

