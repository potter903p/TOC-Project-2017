from transitions.extensions import GraphMachine

def isFloat(value):
        try:
            float(value)
            return True
        except:
            return False

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
        self.money = 0        
        self.main = []
        self.drink = []
        self.second = []
    
    def is_going_to_MC_main(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_MC_m_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.main = "Big Mac"
            self.money += 50
        return text.lower() == '1'
    def is_going_to_MC_m_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.main = "Chicken McNuggets"
            self.money += 40
        return text.lower() == '2'
    def is_going_to_MC_m_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.main = "McDouble"
            self.money += 45
        return text.lower() == '3'

    def is_going_to_MC_c_1(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_MC_c_2(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_MC_d_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.second = "Vanilla Cone"
            self.money += 15
        return text.lower() == '1'
    def is_going_to_MC_d_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.second = "Apple Pie"
            self.money += 20
        return text.lower() == '2'
    def is_going_to_MC_d_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.second = "McFlurry"
            self.money += 35
        return text.lower() == '3'

    def is_going_to_MC_s_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.second = "World Famous Fries"
            self.money += 35
        return text.lower() == '1'
    def is_going_to_MC_s_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.second = "Side Salad"
            self.money += 30
        return text.lower() == '2'

    def is_going_to_KFC_main(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_KFC_m_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.main = "Original Recipe Chicken"
            self.money += 20
        return text.lower() == '1'
    def is_going_to_KFC_m_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.main = "Chicken Ceaser Twister"
            self.money += 40
        return text.lower() == '2'
    def is_going_to_KFC_m_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.main = "Zinger Burger"
            self.money += 45
        return text.lower() == '3'

    def is_going_to_KFC_c(self, update):
        text = update.message.text
        if(isFloat(text)):
            self.money *= float(text)
        return isFloat(text)

    def is_going_to_KFC_s_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.second = "Popcron Chicken"
            self.money += 30
        return text.lower() == '1'
    def is_going_to_KFC_s_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.second = "Seasoned Chips"
            self.money += 20
        return text.lower() == '2'
    def is_going_to_KFC_s_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.second = "Egg Tart"
            self.money += 25
        return text.lower() == '3'

    def is_going_to_SUB_main(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_SUB_m_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.main = "Roast Beef Sandwich"
            self.money += 70
        return text.lower() == '1'
    def is_going_to_SUB_m_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.main = "Meatball Marinara Sandwich"
            self.money += 60
        return text.lower() == '2'
    def is_going_to_SUB_m_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.main = "Classic Tuna Sandwich"
            self.money += 65
        return text.lower() == '3'

    def is_going_to_SUB_s_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.second = "Roast Beef Salad"
            self.money += 45
        return text.lower() == '1'
    def is_going_to_SUB_s_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.second = "Oven Roasted Chicken Salad"
            self.money += 40
        return text.lower() == '2'
    def is_going_to_SUB_s_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.second = "Steak & Cheese Salad"
            self.money += 40
        return text.lower() == '3'


    def is_going_to_drink_1(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            self.drink = "Coca-Cola"
            self.money += 25
        return text.lower() == '1'
    def is_going_to_drink_2(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.drink = "Sprite"
            self.money += 25
        return text.lower() == '2'
    def is_going_to_drink_3(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.drink = "Iced Tea"
            self.money += 25
        return text.lower() == '3'
    def is_going_to_drink_4(self, update):
        text = update.message.text
        if(text.lower() == '4'):
            self.drink = "Coffee"
            self.money += 35
        return text.lower() == '4'

    def is_going_to_result(self, update):
        text = update.message.text        
        return text.lower() == '1'
    def is_going_to_init(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            self.main = ""
            self.second = ""
            self.drink = ""
            self.money = 0
        return text.lower() == '2'
        
    def on_enter_init(self, update):
        update.message.reply_text("What do you want to eat ?")       
        update.message.reply_text("1)McDonald's")
        update.message.reply_text("2)KFC")
        update.message.reply_text("3)SUBWAY")
        
    def on_exit_init(self, update):
        print('Leaving init')
    
    def on_enter_MC_main(self, update):
        update.message.reply_text("Welcome to McDonald's")
        update.message.reply_text("Choose your main course :")
        update.message.reply_text("1)Big Mac - $50")
        update.message.reply_text("2)Chicken McNuggets - $40")
        update.message.reply_text("3)McDouble - $45")
        
    def on_exit_MC_main(self, update):
        print('Leaving MC_main')

    def on_enter_MC_choose(self, update):
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("Choose for dessert or snack :")
        update.message.reply_text("1)dessert")
        update.message.reply_text("2)snack")
        
        
    def on_exit_MC_choose(self, update):
        print('Leaving MC_choose')

    def on_enter_MC_dessert(self, update):
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("Choose your dessert :")
        update.message.reply_text("1)Vanilla Cone - $15")
        update.message.reply_text("2)Apple Pie - $20")
        update.message.reply_text("3)McFlurry - $35")
        
    def on_exit_MC_dessert(self, update):
        print('Leaving MC_dessert')

    def on_enter_MC_snack(self, update):
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("Choose your snack :")
        update.message.reply_text("1)World Famous Fries - $35")
        update.message.reply_text("2)Side Salad - $30")
                
    def on_exit_MC_snack(self, update):
        print('Leaving MC_snack')

    def on_enter_KFC_main(self, update):
        update.message.reply_text("Welcome to KFC")
        update.message.reply_text("Choose your main course :")
        update.message.reply_text("1)Original Recipe Chicken - $20")
        update.message.reply_text("2)Chicken Ceaser Twister - $40")
        update.message.reply_text("3)Zinger Burger - $45")
        
    def on_exit_KFC_main(self, update):
        print('Leaving KFC_main')

    def on_enter_KFC_count(self, update):
        update.message.reply_text("How many pices do you want ?")        
        
    def on_exit_KFC_count(self, update):
        print('Leaving KFC_count')

    def on_enter_KFC_snack(self, update):
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("Choose your snack :")
        update.message.reply_text("1)Popcron Chicken - $30")
        update.message.reply_text("2)Seasoned Chips - $20")
        update.message.reply_text("3)Egg Tart - $25")
        
    def on_exit_KFC_snack(self, update):
        print('Leaving KFC_snack')


    def on_enter_SUB_main(self, update):
        update.message.reply_text("Welcome to SUBWAY")
        update.message.reply_text("Choose your main course :")
        update.message.reply_text("1)Roast Beef Sandwich - $70")
        update.message.reply_text("2)Meatball Marinara Sandwich - $60")
        update.message.reply_text("3)Classic Tuna Sandwich - $65")
        
    def on_exit_SUB_main(self, update):
        print('Leaving SUB_main')

    def on_enter_SUB_salad(self, update):   
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)     
        update.message.reply_text("Choose your salad :")
        update.message.reply_text("1)Roast Beef Salad - $45")
        update.message.reply_text("2)Oven Roasted Chicken Salad - $40")
        update.message.reply_text("3)Steak & Cheese Salad - $40")
        
    def on_exit_SUB_salad(self, update):
        print('Leaving SUB_salad')

    def on_enter_drink(self, update):
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("Choose your drink :")
        update.message.reply_text("1)Coca-Cola - $25")
        update.message.reply_text("2)Sprite - $25")
        update.message.reply_text("3)Iced Tea - $25")
        update.message.reply_text("4)Coffee - $35")
                
    def on_exit_drink(self, update):
        print('Leaving drink')

    def on_enter_final(self, update):
        update.message.reply_text("You order :")
        update.message.reply_text(self.main)
        update.message.reply_text(self.second)
        update.message.reply_text(self.drink)
        update.message.reply_text("--------------------")
        update.message.reply_text("Is this what you want ?")
        update.message.reply_text("1)Yes")
        update.message.reply_text("2)No")        
                
    def on_exit_final(self, update):
        print('Leaving final')

    def on_enter_result(self, update):
        update.message.reply_text("This is your order :")
        update.message.reply_text(self.main)
        update.message.reply_text(self.second)
        update.message.reply_text(self.drink)
        update.message.reply_text("--------------------")
        update.message.reply_text("Total prize :")
        update.message.reply_text(self.money)
        update.message.reply_text("--------------------")
        update.message.reply_text("Thank for your order ~ BYE~")              
                
    def on_exit_result(self, update):
        print('Leaving result')
