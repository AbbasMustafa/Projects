
# This will create capital.py files and Save this data into it
import pprint

data = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
			'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
			'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
			'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
			'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
			'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
			'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
			'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
			'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
			'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
			'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
			'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
			'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
			'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
			'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
			'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
			'Wyoming': 'Cheyenne'}

file = open("capitals.py",'w')
file.write(f"data = {pprint.pformat(data)}")
file.close()

# Import Capital Module
import capitals
import random
import copy

state_name = list(capitals.data.keys())
capitals_name = list(capitals.data.values())

# Create 2 quizes
files = []
for number in range(2):
	# Create Files
	quiz = open(f'Quiz_{(number+1)}.txt','w')
	ans = open(f'answer_{(number+1)}.txt','w')

	# Prepare Header
	quiz.write("Geography Quiz\n\nName:\nRoll No:\nDate\n\n")

	# Random shuffle of state
	states = random.sample(state_name, len(state_name))

	# Prepare Quiz Sheet 50 Quiz on Each txt files
	for index ,state in enumerate(states):
		cap = copy.deepcopy(capitals.data)
		answer = cap[state]
		
		# Remove Correct Answer From Temporary dict
		del cap[state]

		# Arrange Answer in Radom Form
		answers = random.sample(list(cap.keys()),3)
		answers += [answer]
		answers = random.sample(answers, len(answers))

		# Print In Answer Shhet
		quiz.write(f"\n\n{index+1}) What is the captial of {state}")
		for i in range(4):
			quiz.write(f"\n{'ABCD'[i]} : {answers[i]}")

		# Prepare Answeer Sheet
		idx_crr = answers.index(answer) 
		ans.write(f"\n{index+1}) {'ABCD'[idx_crr]}")