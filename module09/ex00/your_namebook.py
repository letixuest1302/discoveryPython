# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 14:11:28 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 14:16:08 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def array_of_names(persons):
    result = []
    for first_name, last_name in persons.items():
        # Se usa capitalize() para poner la primera letra en mayúscula
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        result.append(full_name)
    return result

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
