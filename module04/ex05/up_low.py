# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    up_low.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 13:00:20 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 13:10:25 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

test = input()
result = ""

for c in test:
    if c.islower():
        result += c.upper()
    elif c.isupper():
        result += c.lower()
    else:
        result += c

print(result)
