# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 10:27:06 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 10:47:21 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

number = int(input("Enter a number\n"))

print(f"Tabla de multiplicar del {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
