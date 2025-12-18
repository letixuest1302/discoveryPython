# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 14:17:31 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 14:18:21 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3
def find_the_redheads(family_dict):
    redheads = filter(lambda name: family_dict[name] == "red", family_dict.keys())
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
