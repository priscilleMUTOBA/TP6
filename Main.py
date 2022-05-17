temp = 0
rand = 0
lumiere = 0

def on_button_pressed_a():
    basic.show_number(temp)
    if temp >= 10 and temp <= 18:
        basic.show_string("Watering the plant")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global rand
    rand = randint(0, 100)
    if rand < 60:
        basic.show_string("Watering the plant")
    elif rand > 70:
        basic.show_string("Stopped watering the plant")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if lumiere > 120:
        for index in range(3):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
            basic.pause(200)
            basic.clear_screen()
            basic.pause(200)
    elif lumiere < 120:
        basic.show_string("Stopped watering the plant")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global lumiere
    lumiere = input.light_level()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global temp
    temp = input.temperature()
basic.forever(on_forever)
