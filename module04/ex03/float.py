# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 12:17:40 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 12:41:40 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

n = float(input("Give me a number: "))

if n.is_integer():
    print("his number is an integer.")
else:
    print("This number is a decimal.")
