# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_array.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 13:34:48 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 13:36:43 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

Original_array = [5, 7, 3, 9]
result_set= set()

for value in Original_array: 
    if value > 5:
        result_set.add(value + 2)

print(Original_array)
print(result_set)


