# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 16:20:22 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 16:23:28 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import sys
if len(sys.argv) != 2:
    print("none")
else:
    user_input = input("What was the parameter? ")
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
