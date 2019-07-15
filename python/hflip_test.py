import ffmpeg
(
    ffmpeg
    .input('v.mp4')
    .hflip()
    .output('hflip-out.mp4')
    .run()
)
