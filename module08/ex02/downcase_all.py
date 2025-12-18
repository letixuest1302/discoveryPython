# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 10:29:43 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 10:32:14 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3
import sys

def downcase_it(s):
    return s.lower()

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        print(downcase_it(arg))
