# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 13:24:09 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 13:30:04 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

Original_array = [5, 7, 3, 9]
New_array = []

for value in Original_array:
    New_array.append(value + 2)

print(f"Original_array : {Original_array}")
print(f"New_array: {New_array}")
