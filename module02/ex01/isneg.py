# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 15:56:19 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/15 16:46:33 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env phyton3
number = int(input())

if number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")
