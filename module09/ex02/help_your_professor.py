# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lesainz- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 14:19:41 by lesainz-          #+#    #+#              #
#    Updated: 2025/12/18 14:23:15 by lesainz-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/env/bin/usr python3
def average(scores_dict):
    if not scores_dict:
        return 0.0
    total_score = sum(scores_dict.values())
    return total_score / len(scores_dict)

if __name__ == "__main__":
    class_3B = {
        "marta": 19,
        "luis": 15,
        "victor": 29,
        "celia": 21
    }
    class_3C = {
        "vir": 36,
        "raquel": 23,
        "david": 25,
        "catencio": 25
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
