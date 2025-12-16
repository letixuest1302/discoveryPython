# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameters.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 13:37:48 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/16 13:41:00 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python 3

import sys

num_params = len(sys.argv) - 1
print(f"Number of parameters: {num_params}.")
