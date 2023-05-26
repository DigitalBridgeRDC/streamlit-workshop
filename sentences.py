import random

def generate_sentence(language, num_samples=50):
    sentences = []
    if language == "English":
        subjects = ["I", "You", "He", "She", "They", "We", "It", "The dog", "The cat", "My friend",
                    "The children", "The teacher", "The book", "The movie", "The car", "The house",
                    "A bird", "The computer", "The city", "The restaurant", "The music", "The game",
                    "The team", "The company", "A student", "The doctor", "The actor", "The artist",
                    "The parent", "The child", "The boss", "The employee", "The customer", "The project",
                    "The problem", "The solution", "The question", "The answer", "The idea", "The goal",
                    "The opportunity", "The challenge", "The result", "The event", "The party", "The holiday",
                    "The journey", "The experience", "The success", "The failure"]
        verbs = ["run", "eat", "sleep", "play", "read", "study", "write", "sing", "dance", "work",
                 "talk", "listen", "learn", "teach", "watch", "drive", "travel", "create", "solve",
                 "ask", "answer", "help", "meet", "invite", "celebrate", "enjoy", "visit", "explore",
                 "plan", "dream", "achieve", "fail", "succeed", "experience", "remember", "forget",
                 "imagine", "believe", "understand", "discover", "change", "grow", "inspire", "motivate",
                 "challenge", "contribute", "improve", "learn", "develop", "support"]
        objects = ["books", "games", "food", "movies", "music", "sports", "art", "nature", "technology",
                   "science", "history", "mathematics", "language", "culture", "friends", "family",
                   "colleagues", "customers", "students", "teachers", "pets", "cities", "countries",
                   "vacations", "adventures", "dreams", "goals", "projects", "problems", "solutions",
                   "questions", "answers", "ideas", "opportunities", "challenges", "results", "events",
                   "parties", "holidays", "journeys", "experiences", "successes", "failures", "relationships",
                   "skills", "knowledge", "creativity"]
        adverbs = ["quickly", "happily", "silently", "eagerly", "carefully", "boldly", "patiently", "kindly",
                   "excitedly", "calmly", "passionately", "freely", "simply", "successfully", "loudly",
                   "quietly", "efficiently", "effectively", "honestly", "bravely", "beautifully", "wisely",
                   "generously", "gracefully", "joyfully", "gratefully", "humorously", "curiously",
                   "creatively", "intelligently", "diligently", "positively", "optimistically",
                   "confidently", "politely", "responsibly", "sincerely", "thoughtfully", "warmly",
                   "wholeheartedly", "unconditionally", "vigorously", "willingly", "zealously", "naturally",
                   "faithfully", "fearlessly"]

        for _ in range(num_samples):
            subject = random.choice(subjects)
            verb = random.choice(verbs)
            object = random.choice(objects)
            adverb = random.choice(adverbs)

            sentence = f"{subject} {verb} {object} {adverb}."
            sentences.append(sentence)

    elif language == "French":
        subjects = ["Je", "Tu", "Il", "Elle", "Ils", "Elles", "Nous", "Vous", "Le chien", "Le chat",
                    "Mon ami", "Les enfants", "Le professeur", "Le livre", "Le film", "La voiture",
                    "La maison", "Un oiseau", "L'ordinateur", "La ville", "Le restaurant", "La musique",
                    "Le jeu", "L'équipe", "L'entreprise", "Un étudiant", "Le docteur", "L'acteur", "L'artiste",
                    "Le parent", "L'enfant", "Le patron", "L'employé", "Le client", "Le projet", "Le problème",
                    "La solution", "La question", "La réponse", "L'idée", "Le but", "L'opportunité", "Le défi",
                    "Le résultat", "L'événement", "La fête", "Les vacances", "Le voyage", "L'expérience",
                    "Le succès", "L'échec"]
        verbs = ["mange", "dors", "joue", "lis", "écoute", "étudie", "écris", "chante", "danse", "travaille",
                 "parle", "écoute", "apprends", "enseigne", "regarde", "conduis", "voyage", "crée", "résous",
                 "demande", "réponds", "aide", "rencontre", "invite", "fête", "apprécie", "visite", "explore",
                 "planifie", "rêve", "réalise", "échoue", "réussis", "expérimente", "souviens", "oublie",
                 "imagine", "crois", "comprends", "découvre", "change", "grandis", "inspire", "motive",
                 "défie", "contribue", "améliore", "apprends", "développe", "soutiens"]
        objects = ["des livres", "des jeux", "de la nourriture", "des films", "de la musique", "des sports",
                   "de l'art", "la nature", "la technologie", "la science", "l'histoire", "les mathématiques",
                   "la langue", "la culture", "les amis", "la famille", "les collègues", "les clients",
                   "les étudiants", "les professeurs", "les animaux de compagnie", "les villes", "les pays",
                   "les vacances", "les aventures", "les rêves", "les objectifs", "les projets", "les problèmes",
                   "les solutions", "les questions", "les réponses", "les idées", "les opportunités",
                   "les défis", "les résultats", "les événements", "les fêtes", "les vacances", "les voyages",
                   "les expériences", "les succès", "les échecs", "les relations", "les compétences",
                   "les connaissances", "la créativité"]
        adverbs = ["rapidement", "joyeusement", "silencieusement", "avec impatience", "prudemment", "audacieusement",
                   "patiemment", "gentiment", "excitément", "calmement", "passionnément", "librement", "simplement",
                   "avec succès", "bruyamment", "tranquillement", "efficacement", "effectivement", "honnêtement",
                   "courageusement", "magnifiquement", "sagement", "généreusement", "gracieusement", "joyeusement",
                   "grâce", "humour", "curiosité", "créativité", "intelligemment", "diligemment", "positivement",
                   "optimistiquement", "avec confiance", "poliment", "responsablement", "sincèrement",
                   "avec réflexion", "chaleureusement", "entièrement", "inconditionnellement", "vigoureusement",
                   "volontiers", "avec zèle", "naturellement", "fidèlement", "sans peur"]

        for _ in range(num_samples):
            subject = random.choice(subjects)
            verb = random.choice(verbs)
            object = random.choice(objects)
            adverb = random.choice(adverbs)

            sentence = f"{subject} {verb} {object} {adverb}."
            sentences.append(sentence)

    else:
        return ["Language not supported."]

    return sentences

# Example usage
random_sentences = generate_sentence("English", num_samples=50)
for sentence in random_sentences:
    print(sentence)

random_sentences = generate_sentence("French", num_samples=50)
for sentence in random_sentences:
    print(sentence)
