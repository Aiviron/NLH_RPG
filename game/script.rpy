# В процессе переписывания союзников как объектов. Основная задача сейччас реализовать участие союзников в боевой системе

init python:
    import random as r             


    class TItem:
        def __init__(self, name):
            self.name = name

        def use(self, user):
            pass

    class THealthPotion(TItem):
        def __init__(self, name, heal_amount, cost):
            self.name = name
            self.heal_amount = heal_amount
            self.cost = cost

        def use(self, target):
            if target.hp + self.heal_amount > target._hp_max:
                self.heal_amount = target._hp_max - target.hp    
            target.hp += self.heal_amount
            renpy.say(None, f"{target.name} использует {self.name} и восстанавливает {self.heal_amount} очков здоровья!")

    # class Weapon(Item):
    #     def __init__(self, name, damage):
    #         super().__init__(name)
    #         self.damage = damage

    #     def use(self, user, target):
    #         target.hp -= self.damage
    #         renpy.say(None, f"{user.name} использует {self.name} и наносит {self.damage} урона {target.name}!")

    # class Weapon:
    # def __init__(self, name, damage, rarity, cost):
    #     self.name = name
    #     self.damage = damage
    #     self.rarity = rarity
    #     self.cost = cost

    # def __str__(self):
    #     return f"{self.name} - {self.damage} урона (редкость: {self.rarity}, цена: {self.cost})"


    class TCreature:
        def __init__(self, new_type, new_name, new_hp, new_dmg, new_lvl, new_armor_value, new_isAlive, new_coins, new_inventory, new_score, new_game_class):
            self._type = new_type
            self._name = new_name
            self._hp_max = new_hp
            self._hp = new_hp
            self._dmg = new_dmg
            self._lvl = new_lvl
            self.armor_value = new_armor_value
            self._isAlive = new_isAlive
            self.coins = new_coins
            self.inventory = new_inventory
            self.score = new_score
            self.game_class = new_game_class



        # def add_item(self, item):
        #     self.inventory.append(item)

        # def remove_item(self, item):
        #     self.inventory.remove(item)

        # def use_item(self, index):
        #     item = self.inventory[index]
        #     item.use(self)
        #     #Только для зелий self.inventory.remove(item)

        @property
        def hp(self):
            return self._hp

        @property
        def name(self):
            return self._name


        @hp.setter
        def hp(self, new_hp):
            if new_hp <= 0:
                self._isAlive = False
                self._hp = 0
            else:
                self._hp = new_hp

        def attack(self, target: TCreature):
            hit_dmg = max(self._dmg - target.armor_value, 0)
            target.hp -= hit_dmg
            return hit_dmg

        def add_potion_to_inventory(self, potion: Potion):
            self.inventory.append(potion)

            renpy.say(None, f"{self._name} получает {potion.name}!")
            

        def use_potion(self, potion: Potion):
            if potion in self.inventory:
                self.inventory.remove(potion)
                potion.use(self)
            else:
                renpy.say(None, f"{self._name} не имеет {potion.name} в инвентаре!")
                


    

    class TCreature_main(TCreature):
        pass

    class TCreature_enemy(TCreature):
        pass

    class TCreature_ally(TCreature):
        def __init__(self, new_type, new_name, new_hp, new_dmg, new_lvl, new_armor_value, new_isAlive, new_coins, new_inventory, new_score, new_game_class, new_ally_cost):
            self._type = new_type
            self._name = new_name
            self._hp_max = new_hp
            self._hp = new_hp
            self._dmg = new_dmg
            self._lvl = new_lvl
            self.armor_value = new_armor_value
            self._isAlive = new_isAlive
            self.coins = new_coins
            self.inventory = new_inventory
            self.score = new_score
            self.game_class = new_game_class
            self._ally_cost = new_ally_cost



     
            
            




    def update_weapon_assortment(): # Систему характеристик оружия в будущем необходимо будет переделать аналогично системе характеристик брони
        weapon = r.choice(weapons)
        weapon_rarity = r.choice(weapon_raritis)

        if weapon_rarity == 'Spoiled':
            weapon_lvl = 1
            weapon_cost = r.randint(17, 26)
            weapon_dmg = r.randint(3, 9)
        elif weapon_rarity == 'Rare':
            weapon_lvl = 2
            weapon_cost = r.randint(20, 36)
            weapon_dmg = r.randint(10, 16)
        elif weapon_rarity == 'Epic':
            weapon_lvl = 3
            weapon_cost = r.randint(30, 56)
            weapon_dmg = r.randint(17, 23)
        elif weapon_rarity == 'Legendary':
            weapon_lvl = 4
            weapon_cost = r.randint(70, 100)
            weapon_dmg = r.randint(24, 30)

        return {'weapon_lvl': weapon_lvl, 'weapon_cost': weapon_cost, 'weapon_dmg': weapon_dmg, 'weapon_rarity': weapon_rarity,'weapon': weapon}
    
    
    def update_armor_assortment():

        armors = ["Легкие доспехи", "Средние доспехи", "Тяжелые доспехи"]

        armor = r.choice(armors)

        if armor == "Легкие доспехи":
            armor_cost = r.randint(10, 20)
            armor_def = 1
        elif armor == "Средние доспехи":
            armor_cost = r.randint(20, 30)
            armor_def = 2
        elif armor == 'Тяжелые доспехи':
            armor_cost = r.randint(30, 40)
            armor_def = 3

        
        armor_rarity = r.choice(armor_raritis)

        if armor_rarity == 'Spoiled':
            armor_lvl = 1
            armor_cost += 0
            armor_def += 0
        elif armor_rarity == 'Rare':
            armor_lvl = 2
            armor_cost += 10
            armor_def += 1
        elif armor_rarity == 'Epic':
            armor_lvl = 3
            armor_cost += 20
            armor_def += 2
        elif armor_rarity == 'Legendary':
            armor_lvl = 4
            armor_cost += 30
            armor_def += 3


        

    
        return {'armor_lvl': armor_lvl, 'armor_cost': armor_cost, 'armor_def': armor_def, 'armor_rarity': armor_rarity, 'armor': armor}




    def use_hp_potion(potion_target_hp, potion_target_initial_hp, inventory):
        if "Зелье здоровья" in inventory:
            inventory.remove("Зелье здоровья")
            health_restored = potion_target_initial_hp - potion_target_hp
            potion_target_hp += min(potion_target_initial_hp - potion_target_hp, 50)
            return potion_target_hp, health_restored
        else:
            return potion_target_hp, 0


define system = Character('system', color='#651277')

#----------------------Инициализация переменных--------------------------------------------------------------------

init:

    #author "Author"

    $ coins = 0
    $ hp = 1
    $ damage = 0

    #$ score = 0

    $ armor_raritis = ["Spoiled", "Rare", "Epic","Legendary"] 
    $ weapon_raritis = ["Spoiled", "Rare", "Epic","Legendary"] 

    $ weapon_lvl = 0
    $ weapon_dmg = 0
    $ weapons = ["Меч", "Лук", "Посох", "Кинжал", "Боевой молот", "Алебарда", "Копье"]
    $ current_weapon = None
    $ weapon_cost_multiplier = 0
    $ weapon = None

    $ current_enemy_names = ['wolf', 'maroderin', 'medurazza', 'strangulla', 'shiporog', 'shadow_beast']
    $ current_enemy_name = ' '

    $ shop_entered = False
    $ update_assortment_cost = 0  #Эта переменная отвечает за стоимость смены ассортимента в магазине

    $ armor_def_value = 0
    $ armor_lvl = 0
    $ armor_def = 0
    $ armors = ["Легкие доспехи", "Средние доспехи", "Тяжелые доспехи"]
    $ current_armor = None
    $ armor = None
    
 
    $ companion = None
    $ PlayerAlly1 = None




    #$ item_rarity = r.choice(item_raritis)
    


    $ inventory = []
    $ player_class = None
    $ player_hp = 0
    $ player_atk = 0
    $ lvl_of_difficulty = 0
    

    

    #$ player_def = 0

#-------------------Начало игры------------------------------



label start:
    
    stop music fadeout 1
    scene bg black with fade
    #scene bg rules with fade
    "Цель игры - набрать как можно больше очков.\n Очки даются за убийство монстров и покупку снаряжения"
    "Вы можете путешествовать по разным локациям, встречаясь с монстрами и торговцами."
    "В бою с монстрами вы можете атаковать или пытаться бежать."
    "У торговцев вы можете покупать оружие и другие предметы, которые помогут вам в бою."
    "В случае гибели вы теряете все."

    menu:

        "Начать игру":
            'Выберите уровень сложности'
            menu:
                'Легкий':
                    $ lvl_of_difficulty = 1
                    if lvl_of_difficulty == 1:
                        $ ememy_koef = 0.8
                        jump class_selection
                'Средний':
                    $ lvl_of_difficulty = 2
                    if lvl_of_difficulty == 2:
                        $ ememy_koef = 1
                        jump class_selection
                'Сложный':
                    $ lvl_of_difficulty = 3
                    if lvl_of_difficulty == 3:
                        $ ememy_koef = 1.3
                        jump class_selection



#------------------Выбор Класса-----------------------------------------------

label class_selection:
    #scene bg selection with fade
    "Выберите класс персонажа:"
    menu:
        "Воин":

            ### Инит для объекта
            $ new_type = 'human'
            $ new_name = 'Герой'
            $ new_hp = 15
            $ new_dmg = 3
            $ new_lvl = 1
            $ new_armor_value = 1
            $ new_isAlive = True
            $ new_coins = 10
            $ new_inventory = []
            $ new_score = 0
            $ new_game_class = "warrior"
            ###

       
        "Маг":



            ### Инит для объекта
            $ new_type = 'human'
            $ new_name = 'Герой'
            $ new_hp = 10
            $ new_dmg = 7
            $ new_lvl = 1
            $ new_armor_value = 0
            $ new_isAlive = True
            $ new_coins = 10
            $ new_inventory = []
            $ new_score = 0
            $ new_game_class = "mage"
            ###

        "Лучник":

            ### Инит для объекта
            $ new_type = 'human'
            $ new_name = 'Герой'
            $ new_hp = 12
            $ new_dmg = 5
            $ new_lvl = 1
            $ new_armor_value = 0
            $ new_isAlive = True
            $ new_coins = 10
            $ new_inventory = []
            $ new_score = 0
            $ new_game_class = "archer"
            ###


        "Купец":

            ### Инит для объекта
            $ new_type = 'human'
            $ new_name = 'Герой'
            $ new_hp = 10
            $ new_dmg = 2
            $ new_lvl = 1
            $ new_armor_value = 0
            $ new_isAlive = True
            $ new_coins = 25
            $ new_inventory = []
            $ new_score = 0
            $ new_game_class = "merchant"
            
            ###
  

        "TEST":
            ### Инит для объекта
            $ new_type = 'human'
            $ new_name = 'Герой'
            $ new_hp = 100
            $ new_dmg = 10
            $ new_lvl = 1
            $ new_armor_value = 1
            $ new_isAlive = True
            $ new_coins = 25
            $ new_inventory = []
            $ new_score = 0
            $ new_game_class = "TEST"
            ###
            

    $ PlayerMain = TCreature_main(new_type, new_name, new_hp, new_dmg, new_lvl, new_armor_value, new_isAlive, new_coins, new_inventory, new_score, new_game_class)
    #Создание объекта зелья временно находится тут
    $ potion = THealthPotion('Health Potion', 50, 20)


    
    #Создание объекта союзника временно находится тут

    $ new_type = 'human'
    $ new_name = 'Стражник'
    $ new_hp = 15
    $ new_dmg = 3
    $ new_lvl = 1
    $ new_armor_value = 1
    $ new_isAlive = False
    $ new_coins = 25
    $ new_inventory = []
    $ new_score = 0
    $ new_game_class = "archer"
    $ new_ally_cost = 50


    $ PlayerAlly1 = TCreature_ally(new_type, new_name, new_hp, new_dmg, new_lvl, new_armor_value, new_isAlive, new_coins, new_inventory, new_score, new_game_class, new_ally_cost)
    jump map
    
#-------------------------------------------------Инвернатрь--------------------------------------------------
#Репл кода, нужно переписать
#Зелье здоровья не используется, когда я хочу восстановить здоровье
label inventory_in_map:
    scene bg inventory with fade
    "Ваш инвентарь: [PlayerMain.inventory]"
    menu:
        "Использовать зелье здоровья":
            $ PlayerMain.use_potion(potion)
            jump inventory_in_map
        "Вернуться":
            jump map

label inventory_in_shop:
    scene bg inventory
    "Ваш инвентарь: [PlayerMain.inventory]"
    menu:
        "Использовать зелье здоровья":
            $ PlayerMain.use_potion(potion)
            jump inventory_in_shop
        "Вернуться":
            jump shop

label inventory_in_battle:
    scene bg inventory 
    "Ваш инвентарь: [PlayerMain.inventory]"
    menu:
        "Использовать зелье здоровья":
            $ PlayerMain.use_potion(potion)   
        "Вернуться":
            jump battle



#------------------------отображение статистики-----------------------

screen stats():
    zorder 95
    
    frame:
        xpos 1 ypos 1
        
        vbox:
            text PlayerMain._name
            text "Здоровье: [PlayerMain.hp]" xalign 0.5
            bar value StaticValue(PlayerMain.hp, PlayerMain._hp_max) xalign 0.5 xsize 180
           
            null height 15

            text "Урон: [PlayerMain._dmg]" xalign 0.5
            text "Монеты: [PlayerMain.coins]" xalign 0.5
            text "Очки: [PlayerMain.score]" xalign 0.5
            text "Защита: [PlayerMain.armor_value]" xalign 0.5 



screen enemy_stats():
    zorder 95
    
    frame:
        xalign 0.999 ypos 1
        
        vbox:
            
            text "[PlayerEnemy1._name]" xalign 0.5
            text "Здоровье: [PlayerEnemy1._hp]" xalign 0.5
            bar value StaticValue(PlayerEnemy1._hp, PlayerEnemy1._hp_max) xalign 0.5 xsize 180
           
            null height 15

            text "Урон: [PlayerEnemy1._dmg]" xalign 0.5 
            text "Защита: [PlayerEnemy1.armor_value]" xalign 0.5 
            text "Монеты: [PlayerEnemy1.coins]" xalign 0.5
            text 'Уровнь:[PlayerEnemy1._lvl]' xalign 0.5
            


screen ally_stats():
    zorder 95

    frame:
        xpos 1 ypos 220

        vbox:

            text "Стражник" xalign 0.5

            if PlayerAlly1._isAlive:   
                text "Здоровье: [PlayerAlly1.hp]" xalign 0.5
                bar value StaticValue(PlayerAlly1.hp, PlayerAlly1._hp_max) xalign 0.5 xsize 180

                null height 15

                text "Урон: [PlayerAlly1._dmg]" xalign 0.5
            else:
                text "Здоровье: -" xalign 0.5
                text "Урон: -" xalign 0.5





#-------------------------Карта-------------------------------

label map:
    play music 'audio/music/Breeze_sound.ogg'
    #$ random_event_chanse = r.randint(1,100)
    #if random_event_chanse < 5:
    #    jump event
    #else:
    show screen map
    show screen stats
    if PlayerAlly1._isAlive == True:
        show screen ally_stats
    


screen map:

    

    modal True

    zorder 90
    

    fixed:

        xsize 1280 ysize 720

        add "images/map/main_map.png" align (.5,.5)

    
    fixed:
        xsize 1280 ysize 720

# иконка Битва
        button:
            
            xpos 1000 ypos 185
            xsize 96 ysize 96
            idle_background "images/map/battle.png"
            hover_foreground "images/map/battle.png"
            tooltip "{b}Битва{/b}{p}{i}{size=14}"
            action Hide("map"), Jump("init_battle")
            
            
# иконка Таверна
        button:
            xpos 700 ypos 300    
            xsize 100 ysize 100
            idle_background "images/map/tavern.png"  
            hover_foreground "images/map/tavern.png"
            #focus_mask True
            tooltip "{b}Таверна{/b}{p}{i}{size=14}"
            action Hide("map"), Jump("tavern")



# иконка Магазин 
        button:
            xpos 300 ypos 170
            xsize 90 ysize 91
            idle_background "images/map/shop.png"
            hover_foreground "images/map/shop.png"
            #focus_mask True
            tooltip "{b}Магазин{/b}{p}{i}{size=14}"
            action Hide("map"), Jump("shop")

# иконка Казино
        button:
            xpos 445 ypos 125   
            xsize 100 ysize 100
            idle_background "images/map/casino.png"
            hover_foreground "images/map/casino.png"
            focus_mask True
            tooltip "{b}Казино{/b}{p}{i}{size=14}"
            action Hide("map"), Jump("timoha")

# иконка Инвентарь
        button:
            xpos 25 ypos 600
            xsize 100 ysize 100
            idle_background "images/map/inventory.png"
            hover_foreground "images/map/inventory.png"
            #focus_mask True
            tooltip "{b}Инвентарь{/b}{p}{i}{size=14}"
            action Hide("map"), Jump("inventory_in_map")



    $ tooltip = GetTooltip()

    if tooltip:
        fixed:
            xpos 885 ypos 570
            xsize 310 ysize 103
            add "images/map/about_icon.png"
            text "{color=#ffffff}[tooltip]{/color}" xsize 150 ysize 100 align (.5,.5) text_align .5


#---------------------------------------Случайные события-----------------------------------------------------

label event:
    scene bg village
    $ event = r.randint(1, 3)
    if event == 1 or 2:
        "Ты натыкаешься на старый сундук."
        menu:
            "Открыть сундук":
                $ trap_chance = r.random()
                if trap_chance < 0.2:  # 20% шанс, что сундук является ловушкой
                    "Ты открываешь сундук, и оказываешься в засаде!"
                    play sound "audio/sounds/click_button.ogg"
                    jump init_battle
                else:
                    $ gifted_coins = r.randint(10, 20)
                    $ PlayerMain.coins += gifted_coins
                    "Ты открываешь сундук и находишь [gifted_coins] монет."
                    $ health_loss_chansce = r.random()
                    if health_loss_chance < 0.2:  # 10% шанс потери здоровья
                        $ health_loss = r.randint(1, 5)  # Потеря от 1 до 5 единиц здоровья
                        $ hp -= health_loss
                        "Ты порезался о ржавый металл в сундуке и потерял [health_loss] единиц здоровья."
                        if health_loss > hp:
                            "Вы были настолько слабы, что даже простой порез сумел убить вас "
                            jump game_over
                        else:
                            $ PlayerMain.coins = PlayerMain.coins  # обновляем значение переменной $ PlayerMain.coins
                            hide bg village
                            jump map
                    hide bg village      
                    jump map
            "Не открывать сундук":
                "Ты решаешь не открывать сундук и продолжаешь путь."
                hide bg village
                jump map
    elif event == 3: 
        $ PlayerMain.inventory.append("Зелье здоровья")
        'Местный алхимик подарил тебе зелья здоровья!'
        hide bg village
        jump map







#------------------------------Магазин-----------------------------------------------------------

label shop:
    scene bg shop with fade
    $ hp_potion = 20
    $ ThreeHealthPotions = 50
    if shop_entered  == False:
        $ weapon_assortment = update_weapon_assortment()
        $ weapon = weapon_assortment['weapon']
        $ weapon_cost = weapon_assortment['weapon_cost']
        $ weapon_dmg = weapon_assortment['weapon_dmg']
        $ weapon_lvl = weapon_assortment['weapon_lvl']
        $ weapon_rarity = weapon_assortment['weapon_rarity']

        $ armor_assortment = update_armor_assortment()
        $ armor = armor_assortment['armor']
        $ armor_cost = armor_assortment['armor_cost']
        $ armor_def = armor_assortment['armor_def']
        $ armor_lvl = armor_assortment['armor_lvl']
        $ armor_rarity = armor_assortment['armor_rarity']
    $ shop_entered = True

    menu:
        "Купить зелье здоровья - [potion.cost] монет":
            if PlayerMain.coins >= potion.cost:
                $ PlayerMain.coins -= potion.cost
                $ PlayerMain.inventory.append(potion)
                play sound "audio/sounds/buy_in_shop.ogg"
                "Куплено зелье здоровья."
            else:
                "У вас не хватает монет!"
            jump shop

        # "Купить 3 зелья здоровья - [potion.cost] монет":
        #     if PlayerMain.coins >= potion.cost:
        #         $ PlayerMain.coins -= potion.cost
        #         $ PlayerMain.inventory.append(potion)
        #         $ PlayerMain.inventory.append(potion)
        #         $ PlayerMain.inventory.append(potion)
        #         play sound "audio/sounds/buy_in_shop.ogg"
        #         "Куплено 3 зелья здоровья."
        #     else:
        #         "У вас не хватает монет!"
        #     jump shop

        "[weapon_rarity] [weapon] - [weapon_cost] монет (урон: [weapon_dmg])":
            if PlayerMain.coins >= weapon_cost:
                $ PlayerMain.coins -= weapon_cost
                $ PlayerMain._dmg = weapon_dmg
                $ new_weapon = {'name': weapon, 'rarity': weapon_rarity, 'damage': weapon_dmg, 'cost': weapon_cost}
                #$ inventory.append(new_weapon)
                play sound "audio/sounds/buy_in_shop.ogg"
                $ "Куплено оружие: [weapon_rarity] [weapon] (урон: [damage])"
                $ PlayerMain.score = 3 * weapon_lvl
            else:
                "У вас не хватает монет!"
            jump shop

        
        "[armor_rarity] [armor] - [armor_cost] монет (защита: [armor_def])":
            if PlayerMain.coins >= armor_cost:
                $ PlayerMain.coins -= armor_cost
                $ PlayerMain.armor_value = armor_def
                $ new_armor = {'name': armor, 'rarity': armor_rarity, 'defense': armor_def, 'cost': armor_cost}
                $ current_armor = new_armor
                $ "Куплено доспехи: [armor_rarity] [armor] (защита: [armor_def])"
            else:
                "У вас не хватает монет!"
            jump shop




        
        "Обновить ассортимент(Стоимость: [update_assortment_cost])":
            if PlayerMain.coins < update_assortment_cost:
                "У вас не хватает монет!"
                jump shop
            else:
               
                $ weapon_assortment = update_weapon_assortment()
                $ weapon = weapon_assortment['weapon']
                $ weapon_cost = weapon_assortment['weapon_cost']
                $ weapon_dmg = weapon_assortment['weapon_dmg']
                $ weapon_lvl = weapon_assortment['weapon_lvl']
                $ weapon_rarity = weapon_assortment['weapon_rarity']



                $ armor_assortment = update_armor_assortment()
                $ armor = armor_assortment['armor']
                $ armor_cost = armor_assortment['armor_cost']
                $ armor_def = armor_assortment['armor_def']
                $ armor_lvl = armor_assortment['armor_lvl']
                $ armor_rarity = armor_assortment['armor_rarity']
                $ PlayerMain.coins -= update_assortment_cost
                $ update_assortment_cost += 1
            
                jump shop

        
        'Инвентарь':
            jump inventory_in_shop


        "Покинуть магазин":
            hide bg shop 
            jump map



#---------------------------------------------Таверна--------------------------------------------------------


label tavern:
    scene bg tavern with fade  
    menu:
        "Нанять стражника за [PlayerAlly1._ally_cost] монет. Здорвье: 12. Урон: 4": #Заменить показатели урона и здоровья на динмические
            
            if PlayerMain.coins >= PlayerAlly1._ally_cost:
                $ PlayerMain.coins -= PlayerAlly1._ally_cost
                $ PlayerAlly1._isAlive = True
                # $ companion = {'hp': 12, 'damage': 4}
                # $ companion_hp = companion['hp']
                # $ companion_dmg = companion['damage']
                # $ initial_companion_hp = companion_hp
                # if companion == None:
                #     $ initial_companion_hp = companion_hp

                "Вы наняли спутника!"
            else:
                "У вас не хватает монет!"
            jump tavern
        "Выйти":
            hide bg tavern
            jump map





#----------------------------------------------Битва--------------------------------------------------





label init_battle:
    # play music 'audio/music/NamelessHeroesFightTheme.ogg' fadein 2
    $ enemy_names = ['wolf','shiporog','maroderin','shadow_beast','medurazza','strangulla']
    $ current_enemy_name = r.choice(enemy_names)
    # $ battle_stats = init_battle_stats(current_enemy_name, score)
    # $ enemy_lvl = battle_stats['enemy_lvl']
    # $ enemy_hp = battle_stats['enemy_hp']
    # $ enemy_dmg = battle_stats['enemy_dmg']
    # $ loot = battle_stats['loot']
    # $ initial_enemy_hp = enemy_hp
    if current_enemy_name == 'wolf':
        $ new_type = 'beast'
        $ new_name = 'Волк'
        $ new_hp = 8
        $ new_dmg = 3
        $ new_lvl = 1
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 25
        $ new_inventory = []
        $ new_score =   10
        $ new_game_class = "None"
        scene bg wolf with fade
    elif current_enemy_name == 'shiporog':
        $ new_type = 'beast'
        $ new_name = 'Шипорог'
        $ new_hp = 6
        $ new_dmg = 2
        $ new_lvl = 1
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 25
        $ new_inventory = []
        $ new_score = 10
        $ new_game_class = "None"
        scene bg shiporog with fade

    elif current_enemy_name == 'maroderin':
        $ new_type = 'goblin'
        $ new_name = 'Мародерин'
        $ new_hp = 10
        $ new_dmg = 2
        $ new_lvl = 2
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 35
        $ new_inventory = []
        $ new_score = 20
        $ new_game_class = "None"
        scene bg maroderin with fade
    
    elif current_enemy_name == 'shadow_beast':
        $ new_type = 'shadow'
        $ new_name = 'Теневой зверь'
        $ new_hp = 25
        $ new_dmg = 7
        $ new_lvl = 3
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 50
        $ new_inventory = []
        $ new_score = 30
        $ new_game_class = "None"
        scene bg shadow_beast with fade

    elif current_enemy_name == 'medurazza':
        $ new_type = 'beast'
        $ new_name = 'Медрузза'
        $ new_hp = 12
        $ new_dmg = 4
        $ new_lvl = 2
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 25
        $ new_inventory = []
        $ new_score = 20
        $ new_game_class = "None"
        scene bg medurazza with fade

    elif current_enemy_name == 'strangulla':
        $ new_type = 'beast'
        $ new_name = 'Странгулла'
        $ new_hp = 14
        $ new_dmg = 3
        $ new_lvl = 2
        $ new_armor_value = 0
        $ new_isAlive = True
        $ new_coins = 27
        $ new_inventory = []
        $ new_score = 20
        $ new_game_class = "None"
        scene bg strangulla with fade


    $ PlayerEnemy1 = TCreature_enemy(new_type, new_name, new_hp, new_dmg, new_lvl, new_armor_value, new_isAlive, new_coins, new_inventory, new_score, new_game_class)
    jump battle


label battle:

    show screen enemy_stats

    if PlayerAlly1._isAlive:
        show screen ally_stats

    menu:

        "Атаковать":
            $ target_players = [PlayerMain]
            if PlayerAlly1._isAlive:
                $ target_players.append(PlayerAlly1)
            $ target_player = r.choice(target_players)
            if target_player._isAlive:
                $ damage_dealt = target_player.attack(PlayerEnemy1)
                if PlayerEnemy1.armor_value > 0:
                    'броня отразила [PlayerEnemy1.armor_value] урона'
                if target_player == PlayerMain:
                    "Вы нанесли противнику [damage_dealt] урона"
                else:
                    "Союзник нанес противнику [damage_dealt] урона"
                if not PlayerEnemy1._isAlive:
                    "Вы победили в битве. Ваша награда: [PlayerEnemy1.coins] золота."
                    $ PlayerMain.coins += PlayerEnemy1.coins
                    $ PlayerMain.score += PlayerEnemy1.score
                    if r.random() < 0.3:  # 30% шанс получить зелье здоровья
                        $ PlayerMain.add_potion_to_inventory(potion)
                    hide screen enemy_stats
                    jump map
                if PlayerEnemy1._isAlive:
                    if target_player.armor_value > 0:
                        'броня отразила [target_player.armor_value] урона'
                    $ damage_dealt = PlayerEnemy1.attack(target_player)
                    "[target_player._name] получил [damage_dealt] урона от [PlayerEnemy1._name]."
                    if not target_player._isAlive:
                        if target_player == PlayerMain:
                            hide screen stats
                            jump game_over
                        else:
                            "[target_player._name] погиб в бою"
                            $ target_players.remove(target_player)
                            hide screen ally_stats
                    jump battle

        "Использовать зелье здоровья":
            $ PlayerMain.use_potion(potion)
            jump battle

        'Попытка бегства':
            if PlayerEnemy1._isAlive:
                if r.random() < 0.4:
                    "Вам удалось убежать от противника."
                    hide screen enemy_stats
                    hide screen companion_stats
                    stop music fadeout 1
                    jump map
                else:
                    $ damage_dealt = PlayerEnemy1.attack(PlayerMain)
                    "Вы не смогли убежать и попали под удар противника. Вам нанесли [damage_dealt] урона."
                    if not PlayerMain._isAlive:
                        "Вы погибли при попытке бегства."
                        stop music fadeout 1
                        hide screen enemy_stats
                        hide screen companion_stats
                        jump game_over
                    jump battle


                    

        # 'Атаковать':

        #     $ player_dmg = damage + r.randint(2, 4)
        #     $ enemy_hp = max(enemy_hp - player_dmg, 0)
        #     "Вы нанесли противнику [player_dmg] урона."
        #     if enemy_hp == 0:
        #         $ coins += loot
        #         "Вы победили в битве. Ваша награда: [loot] золота."
        #         $ score += battle_stats['score']
        #         if r.random() < 0.2:  # 20% chance to receive a potion
        #             $ inventory.append("Зелье здоровья")
        #             "Вы получили зелье здоровья!"
        #         hide screen enemy_stats
        #         hide screen companion_stats
        #         stop music fadeout 1

        #         jump map
        #     else:
        #         $ target =  'player'
        #         if companion != None:
        #             $ target = r.choice(['player', 'companion'])
        #         if target == 'player':
        #             $ hero_damage_taken = max(enemy_dmg - armor_def_value, 0)
        #             $ hp -= hero_damage_taken
        #             if armor_def_value != 0:
        #                 'Доспех отразил [armor_def_value] урона '
        #             "Монстр атаковал вас! Вы получили [hero_damage_taken] урона."
        #         else:
        #             if companion:
        #                 $ companion_damage_taken = max(enemy_dmg, 0)
        #                 $ companion['hp'] -= companion_damage_taken
        #                 $ companion_hp = companion['hp']
        #                 "Монстр атаковал вашего спутника! Он получил [companion_damage_taken] урона."

        #         if companion and companion['hp'] <= 0:
        #             $ companion = None
        #             "Ваш спутник погиб в бою."

        #         if hp <= 0:
        #             "Вы погибли от сокрушительного удара [current_enemy_name] "
        #             hide screen enemy_stats
        #             hide screen companion_stats
        #             stop music fadeout 1

        #             jump game_over
        #         else:
        #             if companion:
        #                 $ companion_attack = companion_dmg + r.randint(1, 2)
        #                 $ enemy_hp = max(enemy_hp - companion_attack, 0)
        #                 "Ваш спутник нанес противнику [companion_attack] урона."
        #             jump battle

        # 'Использовать зелье здоровья на себе':
        #     $ hp, health_restored = use_hp_potion(hp, player_hp, inventory)
        #     "Вы использовали зелье здоровья и восстановили [health_restored] здоровья."
        #     jump battle
        # 'Использовать зелье здоровья на компаньоне':
        #     if companion:
        #         $ companion_hp, health_restored = use_hp_potion(companion_hp, initial_companion_hp, inventory)
        #     else:
        #         "У вас нет компаньона."
        #     jump battle
            

    

        # "Попытка бегства":
        #     if r.random() < 0.4:
        #         "Вам удалось убежать от противника."
        #         hide screen enemy_stats
        #         hide screen companion_stats
        #         stop music fadeout 1
        #         jump map
        #     else:
        #         $ hero_damage_taken = enemy_dmg - r.randint(1, 3)
        #         if hero_damage_taken >= hp:
        #             $ hp = 0
        #             "Вы не смогли убежать и попали под удар противника. У вас осталось 0 здоровья."
        #             stop music fadeout 1
        #             hide screen enemy_stats
        #             hide screen companion_stats
        #             jump game_over
        #         else:
        #             $ hp -= hero_damage_taken
        #             "Вы не смогли убежать и попали под удар противника. У вас осталось [hp] здоровья."
        #             jump battle




#----------------------------------------Казино----------------------------------------------------


label timoha:
    scene bg tim
    if coins < 10:
        'Накопи хотя бы 10 монет, тогда будем играть'
        jump map
    else:
        $ ded_mood = r.randint(0, 1)
        $ priz = r.randint(5, 10)
        if ded_mood == 0:
            play sound"audio/sounds/TimSayAllGood.ogg"
            $ coins += priz

            "Добрый дедушка Тимоха подарил тебе [priz] монет."
        else:
            play sound"audio/sounds/TimSayNo.ogg"
            if priz > coins:
                'С тебя нечего брать'
                jump map
            else: 
                $ coins -= priz
                "Злой дед Тимоха отжал у тебя [priz] монет."
        jump map



#---------------------------------------Игра проиграна---------------------------------------------------

label game_over:
    scene bg gameover with fade
    "Игра окончена. Вы набрали [PlayerMain.score] очков ."
    if 100 <= PlayerMain.score < 200 :
        'Ваше звание: Дохляк'
    if 200 <= PlayerMain.score < 300 :
        'Ваше звание: Оруженосец'
    if 300 <= PlayerMain.score < 400 :
        'Ваше звание: Рыцарь'
    if 400 <= PlayerMain.score < 500 :
        'Ваше звание: Знатный воин'
    if 500 <= PlayerMain.score < 600 :
        'Ваше звание: Герой'
    if 1000 <= PlayerMain.score:
        'Ваше звание: Тебе заняться больше нечем?'

    menu:
        "Начать сначала":
            $ PlayerMain.score = 0
            $ weapon_lvl = 1
            $ weapon_dmg = weapon_lvl * 2 - 1
            $ weapon_cost = r.randint(6, 15) * weapon_lvl
            $ PlayerMain.inventory = []
            jump start
        "Выйти из игры":
            "Goodbye!"