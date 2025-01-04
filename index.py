import random 

words = '''anticonstitutionnellement interdisciplinarite incommensurabilite desoxyhemoglobine electroencéphalogramme disproportionnellement 
hypercholesterolemie microspectrophotometrie anthropocentrisme internationalisation ultramicroscopique anticholinesterase psychophysiologique 
abracadabra aristocratie bibliotheque biodiversite catastrophique collaborateur constellation developpement environnement 
experimentation fonctionnaire fraternite hospitalite identificateur ingenierie intergalactique manifestation multinationale observatoire 
programmation rationalisation realisation reincarnation securite specialisation transformation ultramoderne universitaire volontariat 
communication revolutionnaire constructeur philosophique abondance agriculture alteration ambassadeur amplificateur analytique animation 
architecte automatique aventurier balayage categorie charitable creativité crocodile decouverte diffusion diplomate distributeur dynamique 
ecologique entreprise genetique gouvernement harmonie influenceur inspiration magnifique motivation officielle resilience symphonie technologie
abri ami banque bonheur chat chien choux cle cote étoile fete fleur fromage gateau glace haricot joie lait lune mer miel montagne moulin nuage 
ocean orange pain poisson pont riviere soleil table vent vin'''

words = words.upper()
words_list = words.split()

easy_word = [word for word in words_list if len(word) < 7]
medium_word = [word for word in words_list if len(word) >= 7 and len(word) <= 10]
hard_words = [word for word in words_list if len(word) > 10 and len(word) <= 14]
insane_words =[word for word in words_list if len(word) > 14]

word_of_the_day = 'harmonie'
word_of_the_day_list = word_of_the_day.upper()

composed_word = '''chou-fleur pomme-de-terre garde-manger porte-cles 
seche-cheveux tire-bouchon croque-monsieur lave-vaisselle monte-charge 
chasse-neige coupe-vent pese-personne rendez-vous sans-abri'''
composed_word = composed_word.upper()
composed_word_list = composed_word.split()

word_with_two_meanings = 'banque orange souris moule plan toile lettre livre avocat feuille'
word_with_two_meanings = word_with_two_meanings.upper()
word_with_two_meanings_list = word_with_two_meanings.split()

print("""Choississez une difficulté ou un mode de jeu :
       1. Easy
       2. Medium
       3. Hardcore
       4. Insane
       
       5. Mot du jour
       6. Mode composé
       7. Mode à deux sens
       """)

while True:
    levels = int(input("Que voulez-vous ? : "))
    
    if levels == 1:
        selected_words = easy_word
        levels_life = 9
        break
    elif levels == 2:
        selected_words = medium_word
        levels_life = 6
        break
    elif levels == 3:
        selected_words = hard_words
        levels_life = 4
        break
    elif levels == 4:
        selected_words = insane_words
        levels_life = 3
        break
    elif levels == 5:
        selected_words = [word_of_the_day_list]
        levels_life = 7
        break
    elif levels == 6:
        selected_words = composed_word_list
        levels_life = 5
        break
    elif levels == 7:
        selected_words = word_with_two_meanings_list
        levels_life = 5
    else:
        print("Veuillez entrer un chiffre valide : 1 , 2 , 3 , 4 , 5 , 6 ou 7.")



secret = random.randint(0, len(selected_words) - 1)
secret_word = selected_words[secret]

game = {
    'secret_word' : secret_word,
    'guess_word' : '_' * len(secret_word),
    'life' : levels_life,
    'attempts' : 0,
    'stars' : 0,
    'error' : 0,
    'levels' : levels,
    'wrong_letters' : []
}

print(f"{game['guess_word']}, vie : {game['life']} ")

while True:
    letter = input('Entrez une lettre : ').upper()
    
    if not letter.isalpha() or len(letter) > 1:
        print("Erreur, veuillez entrer une lettre valide.")
        game['error'] += 1
    
    if letter in game['secret_word'] and letter not in game['guess_word']:
        guess_word_list = list(game['guess_word'])
        for index, current_letter in enumerate(game['secret_word']):
            if current_letter == letter:
                guess_word_list[index] = letter
        game['guess_word'] = ''.join(guess_word_list)
    else:
        if letter not in game['wrong_letters'] and letter not in game['secret_word']:
            game['wrong_letters'].append(letter)
        print(f"Voici les lettres fausses : {game['wrong_letters']}")
                   
    if letter in game['secret_word'] and letter in game['guess_word']:
        print("Cette lettre est déjà utilisée.")
    
    elif letter not in game['secret_word']:
        game['life'] -= 1
        game['error'] += 1
        print(f"Cette lettre n'est pas dans le mot cherché.")
    print(f"{game['guess_word']}, vie : {game['life']} ")
        
    game['attempts'] += 1
    print(f"Vous etes à {game['attempts']} tentative(s).")
    
    if "_" not in game['guess_word']:
        print("Vous avez gagné !")
        
        if game['levels'] == 7 and game['error'] == 0:
            game['stars'] += 5
        elif game['levels'] == 7 and game['error'] == 1:
            game['stars'] += 3.5
        elif game['levels'] == 7 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 6 and game['error'] == 0:
            game['stars'] += 5
        elif game['levels'] == 6 and game['error'] == 1:
            game['stars'] += 3
        elif game['levels'] == 6 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 5 and game['error'] == 0:
            game['stars'] += 5
        elif game['levels'] == 5 and game['error'] == 1:
            game['stars'] += 3
        elif game['levels'] == 5 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 4 and game['error'] == 0:
            game['stars'] += 7
        elif game['levels'] == 4 and game['error'] == 1:
            game['stars'] += 5
        elif game['levels'] == 4 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 3 and game['error'] == 0:
            game['stars'] += 3
        elif game['levels'] == 3 and game['error'] == 1:
            game['stars'] += 2
        elif game['levels'] == 3 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 2 and game['error'] == 0:
            game['stars'] += 2.5
        elif game['levels'] == 2 and game['error'] == 1:
            game['stars'] += 1.5
        elif game['levels'] == 2 and game['error'] >= 2:
            game['stars'] += 1
        if game['levels'] == 1 and game['error'] == 0:
            game['stars'] += 2
        elif game['levels'] == 1 and game['error'] == 1:
            game['stars'] += 1
        elif game['levels'] == 1 and game['error'] >= 2:
            game['stars'] += 0
            
        print(f"Il vous aura fallu {game['attempts']} tentative(s) et {game['error']} erreur(s) pour trouver le mot : {game['secret_word']}, de difficulté de niveau {game['levels']}, bien joué !")
        print(f"Vous avez gagné également gagné lors de ce mot, {game['stars']} étoile(s).")
        break
    
    elif game['life'] == 0:
        print("Vous avez perdu !")
        print(f"Le mot mystère était : {game['secret_word']}, de niveau {game['levels']}.")
        break
    
   
        
    
