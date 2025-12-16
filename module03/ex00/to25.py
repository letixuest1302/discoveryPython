# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 10:05:19 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 10:22:51 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env phyton3

number = int(input("Enter a number less than 25\n"))

if number > 25:
    print("Error")
else:
    while number <= 25:
          print("Inside the loop, y variable is", number)
          number += 1
