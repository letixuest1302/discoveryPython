# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 17:01:32 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/15 17:14:14 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env phyton3
user = input()

password = "Python is awesome"

if user == password:
    print("ACCESS GARANTED")
else:
    print("ACCESS DENIED")
