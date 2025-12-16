# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 15:19:21 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 15:25:48 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for arg in reversed(sys.argv[1:]):
        print(arg)
