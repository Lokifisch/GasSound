music.play(music.createSoundExpression(WaveShape.Sawtooth, 1, 496, 255, 255, 9999, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
music.play(music.createSoundExpression(WaveShape.Sawtooth, 496, 917, 255, 255, 9999, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
while (true) {
    music.play(music.createSoundExpression(WaveShape.Sawtooth, 917, 917, 255, 255, 9999, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
}
