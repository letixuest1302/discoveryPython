# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 17:16:36 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/15 17:29:46 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env phyton3
user1 = int(input("Enter the first number "))
user2 = int(input("Enter the second number "))

result = user1 * user2

print(result)

if result < 0:
    print("The result is negative")
elif result > 0:
    print("The result is positive")
else:
    print("The result is positive and negative")
