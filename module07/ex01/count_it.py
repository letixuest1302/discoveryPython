# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 16:25:58 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 17:08:22 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")
