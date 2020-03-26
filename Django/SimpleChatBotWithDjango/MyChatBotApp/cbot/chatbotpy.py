def runbot(inp, train_bot=False):
    from chatterbot import ChatBot
    from chatterbot.trainers import ChatterBotCorpusTrainer


    chatbot = ChatBot("mychatbot")

    if train_bot:
        print("Training")
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    response = chatbot.get_response(inp)
    return response

