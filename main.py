basic.show_leds("""
    . # . # .
        . # . # .
        . . # . .
        . # . # .
        . # . # .
""")
music.play_tone(330, music.beat(BeatFraction.WHOLE))
music.play_tone(523, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(494, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.WHOLE))

