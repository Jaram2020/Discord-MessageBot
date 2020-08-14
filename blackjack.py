import random, time

class BlackJack:
    def __init__(self, message, bot):
        self.bot = bot
        self.message = message
        
    def fresh_deck(self):
        suits = { "Spade","Heart","Diamond","Club" }
        ranks = { 2,3,4,5,6,7,8,9,10,"J","Q","K","A" }
        deck = []
        for suit in suits:
            for rank in ranks:
                card = (suit, rank)
                deck.append(card)
        random.shuffle(deck)
        return deck

    def hit(self, deck):
        if deck == []:
            deck = self.fresh_deck() 
        return (deck[0], deck[1:])

    def count_score(self, cards):
        score = 0
        number_of_ace = 0
        for card in cards:
            rank = card[1]
            if rank == "J" or rank == "Q" or rank == "K":
                score += 10
            elif rank == "A":
                score += 11
                number_of_ace += 1
            else:
                score += rank

        while score > 21 and number_of_ace > 0:
            # A의 점수를 11 -> 1로 조정
            score -= 10
            number_of_ace -= 1
            
        return score

    async def show_cards(self, cards, msg): 
        await self.message.channel.send(msg)
        for card in cards:
            if card[0] == 'Spade':
                emoji = "♠️"
            elif card[0] == "Heart":
                emoji = "♥"
            elif card[0] == "Diamond":
                emoji = "♦️"
            elif card[0] == "Club":
                emoji = "♣"
            await self.message.channel.send("`%s` `%s %s`" %(emoji, card[0], card[1]))
    
    
    async def more(self, msg):
        def check(m):
            return m.content == 'y' or m.content == 'n'
        
        await self.message.channel.send(msg)
        arg = await self.bot.wait_for('message', check = check)
        while not (arg.content == 'y' or arg.content == 'n'):
            arg = await self.bot.wait_for('message', check = check)
            # emoji로 반응하게 하는 것도 나쁘지 않아 보여요
            # await message.wait_for_message(author=message.author) 이런것도 사용할 수도 있고
        if arg.content == ('y'):
            answer = 'y'
        elif arg.content == ('n'):
            answer = 'n'
        return answer == 'y'
   
    async def start(self):
        await self.message.channel.send("🎰 자람 카지노에 어서오세요! 🎰") 
        deck = self.fresh_deck() 
        more_game = True

        while more_game:
            await self.message.channel.send("---------------")
            dealer = []
            player = []
            card, deck = self.hit(deck)
            player.append(card)
            card, deck = self.hit(deck)
            dealer.append(card)
            card, deck = self.hit(deck)
            player.append(card)
            card, deck = self.hit(deck)
            dealer.append(card) 
            await self.message.channel.send("😎 제 카드는...")
            await self.message.channel.send("`**** **`")
            if card[0] == 'Spade':
                emoji = "♠️"
            elif card[0] == "Heart":
                emoji = "♥"
            elif card[0] == "Diamond":
                emoji = "♦️"
            elif card[0] == "Club":
                emoji = "♣"
            await self.message.channel.send("`{0}` `{1} {2}`".format(emoji, dealer[1][0], dealer[1][1]))
            
            time.sleep(1)
            await self.show_cards(player, "당신의 카드는...") # 카드 어디서 보여주죠? 아 확인
            score_player = self.count_score(player)
            score_dealer = self.count_score(dealer)
            
            if score_player == 21:
                await self.message.channel.send("Black Jack!")
               
            else: #이 빨간 건 뭐지
                while score_player < 21 and await self.more("😎 Hit 하시겠습니까? "):
                    card, deck = self.hit(deck)
                    player.append(card)
                    score_player = self.count_score(player)
                    if card[0] == 'Spade':
                        emoji = "♠️"
                    elif card[0] == "Heart":
                        emoji = "♥"
                    elif card[0] == "Diamond":
                        emoji = "♦️"
                    elif card[0] == "Club":
                        emoji = "♣"
                    await self.message.channel.send("`%s` `%s %s`" %(emoji, card[0], card[1]))
                if score_player > 21:
                    await self.message.channel.send("😎 당신이 버스트됐습니다. 당신의 패배입니다. 👎")
                 
                else:
                    while score_dealer <= 16:
                        card, deck = self.hit(deck)
                        dealer.append(card)
                        score_dealer = self.count_score(dealer)
                    await self.show_cards(dealer, "제 카드는... ")
                    if score_dealer > 21:
                        await self.message.channel.send("😎 제가 버스트됐습니다. 당신의 승리입니다! 👍")
                     
                    elif score_player == score_dealer:
                        await self.message.channel.send("😎 점수가 같으므로 비겼습니다! 👊")
                    elif score_player >= score_dealer:
                        await self.message.channel.send("😎 당신의 점수가 더 높군요. 당신의 승리입니다! 👍")
                      
                    else:
                        await self.message.channel.send("😎 제 점수가 더 높군요. 당신의 패배입니다. 👎")
            time.sleep(1)
            more_game = await self.more("☝️ 한 판 더 하시겠습니까? ")