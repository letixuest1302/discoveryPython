# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 17:14:11 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 17:20:39 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import sys
if len(sys.argv) != 2:
    print("none")
else:
    count = 0
    for char in sys.argv[1]:
        if char == 'z':
            count += 1
        if count == 0:
            print ("none")
        else:
            print("z" * count)
