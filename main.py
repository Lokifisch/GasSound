def on_received_number(receivedNumber):
    player2.set(LedSpriteProperty.X, receivedNumber)
radio.on_received_number(on_received_number)

def on_button_a():
    player1.change(LedSpriteProperty.X, -1)
    radio.send_number(player1.get(LedSpriteProperty.X))
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    if player1.get(LedSpriteProperty.X) == player2.get(LedSpriteProperty.X):
        radio.send_string("gethit")
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                1600,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                200,
                1,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.IN_BACKGROUND)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    player1.change(LedSpriteProperty.X, 1)
    radio.send_number(player1.get(LedSpriteProperty.X))
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_received_string(receivedString):
    global health
    if receivedString == "gethit":
        music.play(music.string_playable("E D - - - - - - ", 1200),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        health += -1
        basic.pause(5)
        if health == 2:
            basic.set_led_colors(0xff0000, 0xff0000, 0x000000)
        else:
            if health == 1:
                basic.set_led_colors(0xff0000, 0x000000, 0x000000)
            else:
                radio.send_string("won")
                basic.set_led_color(0xff0080)
                basic.show_string("L")
                basic.pause(100)
                control.reset()
        basic.clear_screen()
    if receivedString == "won":
        basic.set_led_color(0x00ff00)
        basic.show_string("W")
        basic.pause(100)
        control.reset()
radio.on_received_string(on_received_string)

player1: game.LedSprite = None
player2: game.LedSprite = None
health = 0
basic.set_led_color(0xff0000)
health = 3
radio.set_group(3)
player2 = game.create_sprite(2, 0)
player1 = game.create_sprite(2, 4)