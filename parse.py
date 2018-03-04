import string

single_commands = {'go': {'forward': ['forward', 'f'], 'back': ['back', 'b'], 'left': ['left', 'l'], 'right': ['right', 'r']}, 'check': {'inventory': ['inventory', 'i']}}

game_commands = ['help', 'exit', 'quit', 'look']

verbs = {'go': ['go', 'move', 'head', 'walk'],
        'attack': ['attack', 'kill', 'hit', 'fight'],
        'take': ['take', 'grab', 'pick up'],
        'look': ['look', 'check', 'examine'],
        'drop': ['drop', 'leave', 'let go']}
prepositions = ['with', 'to', 'on', 'from', 'at']
articles = ['a', 'an', 'the']

def identify_verbs(text):
    found_verb = False
    
    if(len(text)>0):
        for character in string.punctuation:
            text = text.replace(character, " ")
        for verb in verbs.keys():
            for synonym in verbs[verb]:
                if text.startswith(synonym):
                    text = text[len(synonym)]
                    text = verb + text
                    found_verb = True
					
    return [found_verb, text]
	
def strip_articles(text):
	
    if(len(text) > 0):
        text = text.split(" ")
		
        for index in range(len(text)):
            for article in articles:
                if(text[index] == article):
                    text[index] = ""
        text = list(filter(None, text))

    text = " ".join(text)
    return text
	
	
	
def parse_command(text, found_verb = True):
	if(len(text) > 0):
		text = text.split(" ")
		
		if(len(text) == 1):
			for command in game_commands:
				if(text[0] == command):
					return text

				
			for verb in single_commands.keys():
				for command in single_commands[verb].keys():
					for synonym in single_commands[verb][command]:
						if text[0] == synonym:
							text.insert(0, verb)
							text[1] = command
							return text
			if(found_verb):
				return text
			else:
				return None
				
						
		elif(len(text) == 2):
			if not found_verb:
				text[0] = None
			return text
																
		
		elif(len(text) > 2):
			if not found_verb:
				text[0] = None
				
			for preposition in prepositions:
				if (text[1] == preposition):
					return [text[0], None]
					
			index = 2
			while(index < len(text)):
				found_preposition = False
				for preposition in prepositions:
					if (text[index] == preposition):
						found_preposition = True
				if(found_preposition):
					text.pop(index)
					index += 1
				else:
					text[index - 1] += " " + text[index]
					text.pop(index)
			return text
			
		else:																		
			return None
        
def get_command():
	text = input('>> ').lower()
	
	[found_verb, user_input] = identify_verbs(text)
	
	user_input = strip_articles(user_input)
	
	user_input = parse_command(user_input, found_verb)
	
	return [text, user_input]