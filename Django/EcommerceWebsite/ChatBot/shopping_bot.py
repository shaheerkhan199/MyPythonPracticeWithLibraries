from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

shopping_bot = ChatBot(
        "My Shopping Bot",
        read_only=False,
        database="shop",
        storage_adapter="chatterbot.storage.SQLStorageAdapter"
    )
trainer = ChatterBotCorpusTrainer(shopping_bot)
trainer.train("chatterbot.corpus.english")

negotiation_data = [
    'I want to buy this product',
    'Okay! The price of this product is 2000',
    'I want to purchase this product',
    'Okay! The price of this product is 2000',
    'I want this in 1500',
    'Actually this product is imported',
    'I only pay 1500 for this product',
    'Okay Use this promo code AC65VA',
    'Thank you',
    'You are welcome',
    'Thanks',
    'Pleasure',
    'okay',
    'Thanks for contacting us'
]
# trainer.train("chatterbot.corpus.english")
# trainer_test = ListTrainer(shopping_bot)
# trainer_test.train(negotiation_data)