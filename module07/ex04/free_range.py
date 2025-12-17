# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 11:43:47 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/17 11:58:08 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        if start >= end:
            print("none")
        else:
            print(list(range(start, end +1)))
    except ValueError:
        print("none")
