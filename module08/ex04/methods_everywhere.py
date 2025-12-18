# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 10:33:30 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 10:38:26 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/env/bin python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += 'Z'
    print(s)

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
