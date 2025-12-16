# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 15:27:38 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 15:40:50 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env pyhton3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(re.escape(keyword), text)

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))
