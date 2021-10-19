# Number of Vaccinations
# We have a report on the number of flu vaccinations in a class of 20 people.
# It has the following numbers:
# never: 5
# once: 8
# twice: 4
# 3 times: 3
#
# What is the mean number of times those people have been vaccinated?
# Output the result using the print() statement.

vac = {
    'never': 5,
    'once': 8,
    'twice': 4,
    '3 times': 3
}

num_vac =[]
num_vac.append(vac['once'])
num_vac.append(vac['twice']*2)
num_vac.append(vac['3 times']*3)

sum_people = vac['once'] + vac['twice'] + vac['3 times'] + vac['never']

mean_vac = sum(num_vac)/sum_people
print(mean_vac)
