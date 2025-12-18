# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 14:24:19 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 14:26:50 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/env/bin python3

def famous_births(persons_dict):
    sorted_persons = sorted(persons_dict.values(), key=lambda x: x['date_of_birth'])

    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

if __name__ == "__main__":
    historical_figures = {
        "einstein": { "name": "Albert Einstein", "date_of_birth": "1879" },
        "newton": { "name": "Isaac Newton", "date_of_birth": "1643" },
        "curie": { "name": "Marie Curie", "date_of_birth": "1867" },
        "tesla": { "name": "Nikola Tesla", "date_of_birth": "1856" }
    }
    famous_births(historical_figures)
